import json

source_keymap = "qwertyuiopasdfghjkl;'zxcvbnm,./:\"<>?"
dest_keymap = "vmlcpxfoujstrdy.naei;zkwgqbh'/,I:?\"<"

source_keymap = source_keymap + source_keymap.upper()
dest_keymap = dest_keymap + dest_keymap.upper()


with open("qwerty.json", "r") as f:
    before = json.load(f)


for menu in before["dance.menus"].values():
    new_items = {}
    for k, v in menu["items"].items():
        print(k)
        if k not in source_keymap:
            new_k = k
        elif "quotes" in v["text"]:
            new_k = k
        else:
            new_k = dest_keymap[source_keymap.index(k)]
        print(new_k)
        print()
        new_items[new_k] = v
    menu["items"] = new_items


with open("sturdy.json", "w") as f:
    json.dump(before, f, indent=4)
