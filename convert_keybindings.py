import json
from convert_menus import source_keymap, dest_keymap


with open("qwerty_kb.json", "r") as f:
    before = json.load(f)


for item in before:
    k = item["key"]
    print(k)
    parts = k.split("+")
    if "ctrl" in parts:
        continue
    new_parts = []
    for part in parts:
        if part not in source_keymap:
            new_parts.append(part)
        else:
            new_part = dest_keymap[source_keymap.index(part)]
            new_parts.append(new_part)
    new_k = "+".join(new_parts)
    print(new_k)
    item["key"] = new_k


with open("graphite_kb.json", "w") as f:
    json.dump(before, f, indent=4)
