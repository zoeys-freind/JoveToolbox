from ... import shell as shl
def test_cmd(*args):
  print("test")

cdict = {
  "test": {"func": test_cmd, "desc": "testing", "perams": ()}
}
shl.__add_cmd(cdict)
