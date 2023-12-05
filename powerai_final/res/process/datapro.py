import re
import json
# with open(r'E:\chatglm2aicode\finetune_dataset_maker-main\电力题库.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
# # pattern = r'\d+\.([\s\S]+?)\n([\s\S]+?)(?=\n\d+\.|$)'
# # pattern = r'(\d+)\.(.*?)答：(.*?)(?=\n\d+\.|$)'
# pattern = r'(\d+)\、(.*?)答：(.*?)(?=\n\d+\.|$)'
# match = re.findall(pattern, content, re.S)

with open(r"选择.txt","r",encoding="utf-8") as f:
    linelist=f.readlines()
    
flag=1
question=""
answer=""
rightop=""
match=[]
for line in linelist:
    if(flag%2!=0):
        flag+=1
        question=re.findall(r"[^\d、.].*",line,re.S)
        rightop=re.findall(r"[\(][A-Za-z][\)]",question[0],re.S)[0].replace("(","").replace(")","")
        question[0].replace(rightop,"")
    else:
        flag+=1
        question[0]+="选项"+line
        options_dict = {}
        options = re.findall(r'\(([A-Z])\)([^；;\(]+)', line)
        
        for option in options:
            options_dict[option[0]] = option[1]
        answer="答案为"+rightop+"、"+options_dict[rightop]+"。"
        match.append([question[0],answer])
    
# import re
# match=[]
# for line in linelist:
#     text =re.findall(r"[^\d\.].*",line,re.S)[0]                                                                                                                                           
#     pattern = r"\(.*\)" 
#     patterns = r"[^\(].*[^\)]" 
#     matches = re.findall(pattern,text,re.S)
#     matches = re.findall(pattern,text,re.S)
#     answer="答："
#     if matches:
#         contents_in_parentheses = matches
#         for content_in_parentheses in contents_in_parentheses:
#             text = text.replace(content_in_parentheses,"()") 
#             answer+=content_in_parentheses.replace("(","").replace(")","")+" " 
#         answer+="。"
#         match.append([text,answer])
#         print("括号中的内容为：", answer)
#         print("外面的题目为：", text)
#     else:
#         print("未找到括号中的内容")    
 

# import re
# match=[]
# an=""
# qu=re.findall(r"[^\d、.].*[？?]",linelist[0],re.S)
# for line in linelist:
#     if(re.findall(r"[^\d、.].*[？?]",line,re.S)!=[]):
#         match.append([qu[0],an])
#         qu=re.findall(r"[^\d、.].*[？?]",line,re.S)
#         an=""
#     else:
#         an+=line
    
    
# import re
# match=[]
# an=""
# qu=re.findall(r"[^\d、].*[？?]",linelist[0],re.S)
# for line in linelist:
#     if(re.findall(r"[^\d、].*[？?]",line,re.S)!=[]):
#         match.append([qu[0],an])
#         qu=re.findall(r"[^\d、].*[？?]",line,re.S)
#         an=""
#     else:
#         an+=line







data = []
for data1 in match:
    question, answer=data1[0],data1[1]
    item = {
        "instruction": question,
        "input": "",
        "output": answer
    }
    data.append(item)

with open("test4.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)









