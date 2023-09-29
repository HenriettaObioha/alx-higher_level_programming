#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/statu using urlib"""

if __name__ == "__main__":
    imort urlib.request

    with urlib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

