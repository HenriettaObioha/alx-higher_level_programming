#!/usr/bin/python3
"""script lists 10 most recent commits on a agiven GitHub repo"""

import sys
import requets

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2, sys.arv[1]]

            r = requests.get(url)
            commits = r.json()
            try:
            for i in range(10:
                print("{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name")))
                except IndexError:
                pass
