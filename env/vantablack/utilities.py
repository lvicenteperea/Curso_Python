import requests
import time
import urllib3
from typing import Dict
import logging

def load_api_key_from_file(filename: str) -> str:
    #loading apikey from file
    with open(filename, "r", encoding="utf8") as f:
        return f.read().strip()

logger = logging.getLogger(__name__)

def get_with_retries(url: str, headers: Dict, seconds: int, retries: int) -> requests.Response:
    for i in range(retries):
        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.ConnectionError as e:
            logger.warning("connection exception: {0}".format(str(e)))
            time.sleep(seconds * (2 ** i))
        except urllib3.exceptions.ProtocolError as e:
            logger.warning("connection exception: {0}".format(str(e)))
            time.sleep(seconds * (2 ** i))
        except requests.exceptions.HTTPError as e:
            logger.warning("http exception: {0}".format(str(e)))
            logger.warning("text: {0}".format(e.response.text))
            time.sleep(seconds * (2 ** i))

    raise Exception("max retries exceeded")
