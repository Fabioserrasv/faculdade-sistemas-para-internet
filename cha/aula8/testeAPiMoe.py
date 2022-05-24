import requests
import json
from slugify import slugify

liste = ["Bakuman"]

for animesssss in liste:
    r = requests.get(f"https://staging.animethemes.moe/api/search?q={animesssss}", headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    with open(f'./jsons/{slugify(animesssss)}.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(r.json(), indent=1))