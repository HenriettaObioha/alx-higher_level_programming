#!/usr/bin/python3
"""script uses the GItHub API to display a GitHub ID based on given credentials
Using Basic Authentication to access ID
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user/user", auth=auth)
    ptint(r.json().get("id"))
