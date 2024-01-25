import sys, os
# command: jtools <command> <args>
command_dict = {}
# command creation decorator
# this makes it really simple to make the commands
def mk_command(name:str, desc:str="No description provided.", perams:tuple=()):
    def decor(func):
        command_dict[name] = {"func": func, "desc": desc, "perams": perams}
    return decor

thisdir = os.path.dirname(os.path.abspath(__file__))

def main():
    command = ""
    cmd_args = []
    if len(sys.argv) == 1:
        command = "help"
    else:
        command = sys.argv[1]
        if len(sys.argv) > 2:
            cmd_args = sys.argv[2:]
        else:
            cmd_args = []

    menu = """
       ╭──────────╮
╭──────┤:[MENUNM]:├──────╮
│  ╲╱  ┕━━━━━━━━━━┙  ╲╱  │
├────────────────────────╯
│:[LISTING]:
│
├────────────────────────╮
╰────────────────────────╯
"""[1:-1] # recommended to have MENUNM at 10 characters always

    # perams beginning with '*' are required.

    # - command definitions - #

    @mk_command("help", "Shows the help menu")
    def _help(*args):
        print(usage)

    @mk_command("config", "Opens the config menu")
    def config(*args):
        cnfg = menu.replace(":[MENUNM]:", "  Config  ")
        settings = []

    try:
        global cma
        cma = "<importloop>"
        for cmm in os.listdir(f"{os.path.dirname(thisdir)}/submodules"):
            if not cmm.startswith("__"):
                cma = cmm
                with open(f"{os.path.dirname(thisdir)}/submodules/{cmm}", "r") as fm:
                    cmdict = {"mk_command": mk_command, "command_dict": command_dict, "__file__": f"{os.path.dirname(thisdir)}/submodules/{cmm}"}
                    exec(fm.read(), cmdict)
                    globals()["command_dict"] = cmdict["command_dict"]
    except Exception as e:
        print(f"Could not finish loading submodules!\n('{cma}' raised a {e.__class__.__name__})")

    usg = ""

    for cmd, info in command_dict.items():

        usg += "\n├┤ " + cmd + " ↴"
        usg += "\n│┃ '" + info["desc"] + "'"
        argindx = 0
        for peram in info["perams"]:
            argindx += 1
            usg += "\n│├─┤ " + peram[0] + (" (required)" if peram[0].startswith("*") else " (optional)")
            usg += f"\n││{argindx}┃ '" + peram[1] + "'"
            usg += "\n│├─╯"
        usg += "\n├┘"


    usage = menu.replace(":[LISTING]:", usg).replace(":[MENUNM]:", "Usage Tree")

    # - command execution - #
    if command in command_dict:
        command_dict[command]["func"](*cmd_args)
    else:
        print(f"\nCommand '{command}' not found.\n")
        print(usage)
