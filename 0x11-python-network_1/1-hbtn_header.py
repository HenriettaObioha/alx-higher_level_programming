#!/usr/bin/python3
"""script to display X-Request-Id header variable of a request to a given URL"""

import sys
import urlib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urlib.request.Request(url)
    with urlib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
