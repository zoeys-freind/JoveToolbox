import sys
# command: jtools <command> <args>
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

    command_dict = {}
    # command creation decorator
    # this makes it really simple to make the commands
    def mk_command(name:str, desc:str="No description provided.", perams:tuple=()):
        def decor(func):
            command_dict[name] = {"func": func, "desc": desc, "perams": perams}
        return decor

    # perams beginning with '*' are required.

    # - command definitions - #

    @mk_command("help", "Shows the help menu")
    def _help(*args):
        print(usage)

    @mk_command("config", "Opens the config menu")
    def config(*args):
        cnfg = menu.replace(":[MENUNM]:", "  Config  ")
        settings = []

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
