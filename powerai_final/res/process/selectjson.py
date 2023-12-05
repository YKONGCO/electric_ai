import json
from fuzzywuzzy import fuzz
#指令微调数据集去重

with open(r'mix_sf.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


new_data = []
import tqdm as td

qu_data=[]
chart=td.tqdm(range(len(data)))

for item in data:
    if not any(fuzz.token_sort_ratio(item['instruction'], new_item['instruction']) > 95 for new_item in new_data):
        new_data.append(item)
    else:
        qu_data.append(item)
    chart.update(1)

with open('op_new_data.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

with open('op_qu_data.json', 'w', encoding='utf-8') as f:
    json.dump(qu_data, f, ensure_ascii=False, indent=4)