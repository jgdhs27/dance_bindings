import json

source_keymap = (
    "qwertyuiop"
    + "asdfghjkl;'"
    + "zxcvbnm,./"
    + "QWERTYUIOP"
    + 'ASDFGHJKL:"'
    + "ZXCVBNM<>?"
)
dest_keymap = (
    "vmlcpxfouj"
    + "strdy.naei;"
    + "zkwgqbh'/,"
    + "VMLCPXFOUJ"
    + "STRDY>NAEI:"
    + 'ZKWGQBH"?<'
)


with open("qwerty.json", "r") as f:
    before = json.load(f)


for menu in before.values():
    new_items = {}
    for k, v in menu["items"].items():
        if k not in source_keymap:
            new_k = k
        elif "quotes" in v["text"]:
            new_k = k
        else:
            new_k = dest_keymap[source_keymap.index(k)]
        print(k)
        print(new_k)
        print()
        new_items[new_k] = v
    menu["items"] = new_items


with open("sturdy.json", "w") as f:
    json.dump(before, f, indent=4)
