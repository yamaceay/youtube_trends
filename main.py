import json
import os
import re

paths = []
for file in os.walk("scripts"):
    files = file[-1]
    for file in files:
        path = "scripts/"+file
        paths.append(path)

ids = {int(re.findall("scripts/([0-9]{0,})", path)[0]): path for path in paths}

with open("ads.json", "r") as file:
    datas = json.loads(file.read())

for data in datas:
    for info in data["data"]:
        if info["link_id"] in list(ids.keys()):
            info.update({"script_link": ids[info["link_id"]]})

with open("ads.json", "w") as file:
    file.write(json.dumps(datas, indent=4))
