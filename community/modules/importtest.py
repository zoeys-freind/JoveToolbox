@mk_command("test2", "Test command 2", (("testarg", "test arg"),))
def test(*args):
    print(args)
