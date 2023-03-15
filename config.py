import secrets

# Configuration parameters

omekas_api_url = secrets.omekas_api_url     # This value is imported from the secrets.py file
input_dir = "data/omekas"
output_dir = "data/result"

# Define the query-URL to limit the amount of results
# The site_id can be found on <omekas_api_url>/sites
api_filter_query = "?site_id=4"

# Define the list of API endpoints to harvest. A list of available endpoints can be found at the omekas_api_url defined above.
api_endpoints = [
    "custom_vocabs",
    "data_types",
    "item_sets",
    "items",
    "media",
    "properties",
    "resource_classes",
    "resource_templates",
    "sites",
    "vocabularies"
]