#!/usr/bin/python3
"""script sends a request to a given URL and displays the response body"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))