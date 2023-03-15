# Omeka S JSON-LD to TTL conversion


## Usage
1. Create a venv (1st time only!)
   ```
   # Example:
   cd /path/to/omekas-jsonld-to-ttl
   python3.10 -m venv venv
   ```
2. Activate the venv
   ```
   source venv/bin/activate
   ```
3. Install packages from requirements.txt (1st time only!)
   ```
   # Example:
   pip install -r requirements.txt
   ```
3. Create a `secrets.py` file and set values like these:
    ```
   # Define secrets, like URLs and API-keys
   # DO NOT COMMIT THIS FILE TO GIT 
   omekas_api_url = "https://your-omeka.hostname.org/api"
    ```
4. Change the values in `config.py`
5. Run the `main.py` script. 

   **IMPORTANT: remove the old files in `data/omekas` and `data/result` if the script has run before!**

   ```bash
   (venv) you@ubnt:~/omekas-jsonld-to-ttl$ python main.py
   ```
6. Find the `omekas.ttl` file in the `data/result` folder. This file can be used to upload to a triple store.


## Acknowledgements
This code is adapted from the Colab notebook created by https://github.com/companje/auteursportaal-datamapping.git 