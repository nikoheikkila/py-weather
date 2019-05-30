"""
Prints weather information for the given location.
"""

import os
import sys
import requests
from argparse import ArgumentParser

DEFAULT_LOCALE = "en"
DEFAULT_LOCATION = "Helsinki"


def get_location() -> str:
    print("Location not specified. Locating from IP address...")

    try:
        response = requests.get("https://ifconfig.co/json")
    except requests.RequestException:
        print(f"Error fetching location. Using '{DEFAULT_LOCATION}' instead.")
        return DEFAULT_LOCATION

    data = response.json()
    print(f"You are near the city of {data['city']}.")

    return f"{data['latitude']}+{data['longitude']}"


def get_args():
    args = ArgumentParser(__doc__)
    args.add_argument("location", type=str, nargs="?", metavar="LOCATION", help="Where to look weather from")

    return args.parse_args()


def parse_locale() -> str:
    try:
        return os.environ["LANG"][:2]
    except KeyError:
        return DEFAULT_LOCALE


def main():
    args = get_args()
    headers = {"Accept-Language": parse_locale()}
    params = {"0": "", "n": "", "q": ""}
    location = args.location or get_location()
    url = f"https://wttr.in/{location}"

    try:
        response = requests.get(url, headers=headers, params=params)
    except requests.Timeout:
        print("Request to wttr.in API timed out.")
        return 1

    print(response.text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
