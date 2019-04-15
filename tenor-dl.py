#!/usr/bin/env python3

import requests
from clint.textui import progress

from urllib.parse import urlparse
import argparse
import configparser
import sys
import os
import re

ERROR = "\033[91m" + "[ERROR]" + "\033[0m"

def argparse_init():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="the ID of the gif")
    parser.add_argument("-a", "--apikey", help="the Tenor api key")
    parser.add_argument("-d", "--download", help="download the gif", action="store_true")
    args = parser.parse_args()
    return args

def parse_config():
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')
        api_key = config['TENOR']['API_KEY']
    except KeyError:
        sys.exit("{ERROR} Please check config.ini".format(ERROR=ERROR))
    return api_key

def request_gif(gif_id, api_key):
    resp = requests.get("https://api.tenor.com/v1/gifs?ids={id}&key={key}"
                        .format(id=gif_id, key=api_key)).json()
    gif_url = resp['results'][0]['media'][0]['gif']['url']

    title = resp['results'][0]['title']
    url = resp['results'][0]['itemurl']

    if not title == "":
        gif_name = title
    else:
        # Get the filename from the URL path name.
        url_path = urlparse(url).path
        gif_name = re.search(r"/view/(.*)-gif", url_path).group(1)

    return gif_url, gif_name

def download_gif(gif_url, gif_name):
    req = requests.get(gif_url, stream=True)
    file_name = "{gif_name}.gif".format(gif_name=gif_name)

    with open(file_name, 'wb') as f:
        total_length = int(req.headers.get('content-length'))
        for chunk in progress.bar(req.iter_content(chunk_size=1024),
                                  expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

if __name__ == "__main__":
    args = argparse_init()
    gif_id = args.id

    if args.apikey:
        api_key = args.apikey
    elif os.path.isfile("config.ini"):
        api_key = parse_config()
    else:
        sys.exit("{ERROR} Must provide api key either as argument or in config.ini"
                 .format(ERROR=ERROR))

    gif_url, gif_name = request_gif(gif_id, api_key)

    if args.download:
        download_gif(gif_url, gif_name)

    print("TITLE: {name}".format(name=gif_name))
    print("URL: {url}".format(url=gif_url))
