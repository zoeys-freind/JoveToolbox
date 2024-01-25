# yes, the submodules are primarily community made, but its a lot easir to just make built-in ones here :/

import requests as rq
import os

@mk_command("install", "Installs a sub-module from the repo.", (("module name", "The identifier for the module you want to install."),))
def install(*args):
    if args[0].startswith("-"):
        pass
    else:
        name = args[0]
        url = "https://raw.githubusercontent.com/zoeys-freind/JoveToolbox/main/community/modules/"+name+".py"
        req = rq.get(url)
        print(f"Searching for '{name}'...")
        ps = False
        if req.status_code == 200:
            print(f"Found '{name}'!")
            print("______ info ______")
            print(f"Name: {name}.py")
            print(f"Source: {url}")
            print(f"Trusted: True")
            cnf = input("Install? (y/n): ").lower()
            thisdir = os.path.dirname(os.path.realpath(__file__))
            if name+".py" in os.listdir(thisdir):
                cnf = ("y" if input("File name conflicts with another sub-module. Overwrite? (y/n): ").lower() == "y" else "n")
            if cnf == "y":
                ps = True
            else:
                print("Aborting...")
        elif req.status_code == 404:
            print(f"Could not find '{name}' from the given source.")
        else:
            print(f"Error when finding '{name}' in the given source. (Status code: {req.status_code})")

        if ps:
            print(f"Installing '{name}'...")
            with open(thisdir+f"/{name}.py", "w") as f:
                f.write(req.text)
            print(f"Installed '{name}'!")
