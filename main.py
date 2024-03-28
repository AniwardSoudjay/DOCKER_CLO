import os
import requests
import logging
from fastapi import FastAPI
from requests.exceptions import RequestException
from dotenv import load_dotenv

load_dotenv('.venv')  # Charge les variables d'environnement à partir du fichier .env

app = FastAPI()
s = requests.Session()

log_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'my_log')
os.makedirs(log_directory, exist_ok=True)
log_path = os.path.join(log_directory, 'api_test.log')

# Configuration du logging
logging.basicConfig(filename=log_path, level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Ajout du gestionnaire de fichier
file_handler = logging.FileHandler('log.txt')
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

def test_content(api_address, version, endpoint, username, password, sentence):
    try:
        url = f"{api_address}/{version}/{endpoint}"
        logger.debug(f"Attempting to connect to: {url}")  # Utilisation du logger pour le débogage
        response = s.get(
            url=url,
            params={
                "username": username,
                "password": password,
                "sentence": sentence
            }
        )
        response.raise_for_status()

        expected_positive = True if version == "v1" else False
        actual_positive = response.json()["score"] > 0
        score_value = response.json()["score"]

        output = f"""
============================
 Content test
============================
request done at "/{version}/{endpoint}"
| username="{username}"
| password="{password}"
| sentence="{sentence}"
expected result positive = {expected_positive}
actual result positive = {actual_positive}
score value = {score_value}
==> {"SUCCESS" if actual_positive == expected_positive else "FAILURE"}
"""

        logger.debug(output)  # Utilisation du logger pour l'écriture dans le fichier de log

    except RequestException as e:
        logger.error(f"Request failed: {e}")
        print(f"Request failed: {e}")

def test_content_alice_v1(api_address):
    positive_sentence = os.getenv("pos_sentence_env")
    negative_sentence = os.getenv("neg_sentence_env")

    test_content(api_address, "v1", "sentiment", "alice", "wonderland", positive_sentence)
    test_content(api_address, "v1", "sentiment", "alice", "wonderland", negative_sentence)

def test_content_alice_v2(api_address):
    positive_sentence = os.getenv("pos_sentence_env")
    negative_sentence = os.getenv("neg_sentence_env")

    test_content(api_address, "v2", "sentiment", "alice", "wonderland", positive_sentence)
    test_content(api_address, "v2", "sentiment", "alice", "wonderland", negative_sentence)

def main():
    api_name = os.getenv("api_name")
    api_address = f"http://{api_name}:8000"

    logger.info("Starting script main.py.")

    # Tests...
    test_content_alice_v1(api_address)
    test_content_alice_v2(api_address)

    logger.info("Script main.py completed.")

if __name__ == "__main__":
    main()
