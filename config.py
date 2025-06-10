import secrets
from datetime import datetime

# Configuration parameters

# Data folders
ts = datetime.now().strftime("%Y%m%d-%H%M%S")
output_dir = "data/" + ts + "_output/"

# Omeka S API
omekas_api_url = secrets.omekas_api_url     # This value is imported from the secrets.py file

# Define the filter query to limit the amount of items to harvest.
# There are multiple ways to filter results on an API endpoints. Examples:
# - ?site_id=N          Returns all items belonging to this site. The site_id can be found on <omekas_api_url>/sites
# - ?item_set_id=3151   Returns all items that are part of this item set.
api_filter_query = "?item_set_id=3151"

# A list of available endpoints can be found at the omekas_api_url defined above.
# Define the list of API endpoints to harvest.
api_endpoints = [
    "items",
    "media",
    "item_sets",
    "sites",
    "resource_classes",
    "resource_templates",
    "users"
]

# Endpoints that are not referenced in a typical item's JSON-LD (and that can be skipped)
unused_api_endpoints = [
    "api_resources",
    "assets",
    "bulk_exporters",
    "bulk_exports",
    "csvimport_entities",
    "csvimport_imports",
    "custom_vocabs",
    "data_types",
    "hits",
    "jobs",
    "logs",
    "modules",
    "properties",
    "resources",
    "search_configs",
    "search_engines",
    "search_suggesters",
    "site_pages",
    "solr_cores",
    "solr_maps",
    "stats",
    "value_annotations",
    "vocabularies"
]