import secrets

# Configuration parameters

omekas_api_url = secrets.omekas_api_url
input_dir = "data/omekas"
output_dir = "data/result"

# Define the list of API endpoints to harvest. A list of available endpoints can be found at the omekas_api_url defined above.
api_endpoints = [
    # "assets",
    "custom_vocabs",
    "data_types",
    "item_sets",
    "items",
    # "mapping_markers",
    # "mappings",
    "media",
    "properties",
    "resource_classes",
    "resource_templates",
    # "resources",
    # "site_pages",
    "sites",
    # "users",
    # "value_annotations"
    "vocabularies"
]