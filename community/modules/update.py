# yes, the submodules are primarily community made, but its a lot easir to just make built-in ones here :/

import requests as rq
import os

@mk_command("update", "Updates the main handler.")
def install(*args):
    if args[0].startswith("-"):
        pass
    else:
        url = "https://raw.githubusercontent.com/zoeys-freind/JoveToolbox/main/jovetools/jovetools/shell/__init__.py"
        req = rq.get(url)
        print(f"Getting source...")
        ps = False
        if req.status_code == 200:
            print(f"Fetched")
            print("______ info ______")
            print(f"Name: __init__.py")
            print(f"Source: {url}")
            print(f"Trusted: True")
            cnf = input("Install? (y/n): ").lower()
            thisdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+"/shell"
            if cnf == "y":
                ps = True
            else:
                print("Aborting...")
        else:
            print(f"Error when fetching source. (Status code: {req.status_code})")

        if ps:
            print(f"Updating...")
            with open(thisdir+f"__init__.py", "w") as f:
                f.write(req.text)
            print(f"Updated!")
