import json
import random
#随机打乱

# 原始的JSON文档
with open(r'final_version_database\mix.json', 'r', encoding='utf-8') as f:
    content = f.read()
data = json.loads(content)
random.shuffle(data)
with open("mix_sf.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

