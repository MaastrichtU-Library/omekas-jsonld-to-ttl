from tqdm import tqdm
import requests
import json
from pathlib import Path
from rdflib import Graph

# Import values from the config file
import config as cfg


if __name__ == '__main__':

    # Folders
    json_dir = cfg.output_dir + "omekas_json"
    ttl_dir = cfg.output_dir + "triples_ttl"
    Path(json_dir).mkdir(parents=True, exist_ok=True)
    Path(ttl_dir).mkdir(parents=True, exist_ok=True)

    # Harvest data from Omeka
    types = cfg.api_endpoints

    print("Downloading data from Omeka S...")

    for t in tqdm(types):
        page = 1
        url = cfg.omekas_api_url + "/" + t + cfg.api_filter_query
        while url:
            filename = f"{json_dir}/{t}-{page}.json"
            response = requests.get(url)
            json.dump(response.json(), open(filename, "w"), indent=2)
            next = response.links.get("next")
            url = next["url"] if next else ""
            page += 1

    print("Download ready")

    # Convert JSON-LD to Turtle
    input_files = list(Path(json_dir).rglob("*.json"))
    output_filename = ttl_dir + "/omekas.ttl"

    # add all json files to one graph
    g = Graph()
    for input_file_path in tqdm(input_files):
        print(input_file_path)
        g.parse(input_file_path)

    # write graph to turtle file
    ttl = g.serialize(format="ttl")
    ttl = ttl.replace("<schema:>", "<http://schema.org/>")  # fix invalid schema prefix in header
    print(ttl, file=open(output_filename, "w"))
    print()
    print(output_filename)
