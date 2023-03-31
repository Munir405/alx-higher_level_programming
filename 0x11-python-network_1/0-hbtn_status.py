#!/usr/bin/python3
"""
fetch https://alx-intranet.hbtn.io/status; display response
"""

import urllib.request

if __name__ == "__main__":
    response = urllib.request.urlopen("https://alx-intranet.hbtn.io/status").read()
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
    print(f"\t- utf8 content: {response.decode('utf-8')}")
