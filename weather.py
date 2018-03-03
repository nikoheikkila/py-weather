"""
Prints weather information for the given location
"""

import os
import sys
import requests
from argparse import ArgumentParser

DEFAULT_LOCALE = "en"
SERVICE = "http://wttr.in/{}"


def get_args():
    args = ArgumentParser(__doc__)
    args.add_argument(
        'location',
        type=str,
        nargs="*",
        metavar="LOCATION",
        default="Helsinki",
        help="Where to look weather from"
    )

    return args.parse_args()


def parse_locale() -> str:
    try:
        return os.environ["LANG"][:2]
    except KeyError:
        return DEFAULT_LOCALE


def main():
    args = get_args()
    headers = {
        "Accept-Language": parse_locale()
    }
    params = {
        "0": "",
        "n": "",
        "q": ""
    }

    response = requests.get(
        SERVICE.format(args.location),
        headers=headers,
        params=params
    )

    print(response.text)


if __name__ == '__main__':
    sys.exit(main())