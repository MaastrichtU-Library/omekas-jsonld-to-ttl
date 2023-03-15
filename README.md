# Omeka S JSON to TTL conversion


## Usage
1. Create a venv
2. Install packages from requirements.txt
3. Create a `secrets.py` file and set values like these:
    ```
    omekas_api_url = "https://your-omeka.hostname.org/api"
    ```
4. Set values in `config.py`
5. Run the `main.py` script
6. Find the `omekas.ttl` file in the `data/result` folder


## Acknowledgements
This code is adapted from the Colab notebook created by https://github.com/companje/auteursportaal-datamapping.git 