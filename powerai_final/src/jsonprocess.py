import json

# 给定的JSON数据
def read(json_path:str)->dict:
    """
    {"0":[prompt,type,question]}
    
    """
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # 创建包含选项的字符串列表
    questiondict={}
    for item in data :
        options = [f"{key}、{value} " for key, value in item.items() if key not in ["id", "question", "type"]]
        options_str = " ".join(options)
        # 创建prompt
        if(item['type']!="问答"):
            prompt = f"{item['question']} 选项：{options_str} 题型： {item['type']}"
        else:
            prompt = f"{item['question']}"
            
        questiondict["{}".format(item["id"])]=[prompt,item['type'],item['question']]
        # questiondict["{}".format(item["id"])]=prompt
    return questiondict




def out(input_dict:dict,json_name)->None:
    """
    dict格式
    {"0":"A、B、C"} 中文顿号
    or
    {0:"A、B、C"}
    """    
    # 转换数据格式并生成新的列表
    output_list = []
    for key, value in input_dict.items():
        if key.isdigit():
            if "、" in value:  # 处理多选题
                answer_list = value.split("、")
                answer_str = "、".join(sorted(answer_list))
                output_list.append({'ID': int(key), 'answer': answer_str})
            else:  # 处理单选和文字题
                output_list.append({'ID': int(key), 'answer': value})

    # 将列表转换为JSON字符串
    json_output = json.dumps(output_list, ensure_ascii=False, indent=4)
    with open('{}.json'.format(json_name), 'w', encoding='utf-8') as file:
        file.write(json_output)
        
