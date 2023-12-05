import src.faiss_kb as fb
import src.jsonprocess as jt
import src.resprocess as rp
import src.prompt as pr 
from jinja2 import Template
import tqdm as td
import src.model_load as lm
qu_data=jt.read(r"res/qu/question.json")
result_dict={}
log_dict={}
chart=td.tqdm(range(len(qu_data)))
for i in range(len(qu_data)):
    
    #如果出现中断添加如下代码
    #log_step=10
    #i+=log_step
    #chart.update(log_step)
    
    fullquery,qtype,query=qu_data["{}".format(i)]
    
    #知识库检索
    search_result=fb.do_search(query=query,top_k=1,score_threshold=1.2)
    try:
        contextlist,context=fb.create_context_prompt(search_result)
        print("搜索到的内容",context,"\n")
        output = pr.template_load(qtype+"kb").render(context=context,question=fullquery)
    except Exception as e:
        print("检索失败",e)
        output =pr.template_load(qtype).render(question=fullquery) 
    
    output =pr.template_load(qtype).render(question=fullquery) 
    
    
    #test不用管
    # template_string1 = prompt["empty"] 
    # template1 = Template(template_string1)
    # output1 = template1.render(question=query) 
    # print(context,"\n")
    # template_string = prompt["question"] 
    # template = Template(template_string)
    # output = template.render(context=context,question=fullquery) 

    # first_result=api.send_api_request(output,url="http://223.2.20.73:8001/",load=2)
    
    # #如使用本地模型请添加如下代码
    # import local_model as lm #添加至开头，注意更改路径
    first_result=lm.chat(output)
    
    log_dict["{}".format(i)]=[output,first_result]
    jt.out(log_dict,"log/RESULTLORA1128")
    final_result=rp.result_local_lora(first_result,qtype)
    result_dict["{}".format(i)]=final_result
    print(final_result)
    chart.update(1)
    jt.out(result_dict,"result/RESULTLORA128")
jt.out(result_dict,"result/RESULTLORA128")#
    
    
    