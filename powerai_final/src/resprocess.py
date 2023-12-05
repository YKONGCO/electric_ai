def result_process(result_dict,qtype):
    answer=result_dict["answer"]
    if(qtype!="问答"):
        import re
        try:
           pattern = re.compile(r'[^。！？]+[。！？]$',re.S)
           match = pattern.search(answer)
           text = match.group(0) 
           print(text,"\n")
           findre=re.compile(r'([A-D])(?!.*\1)',re.S)
           result = re.findall(findre, text)
           result.sort()   
           result = '、'.join(result)
           return result
        except Exception as e:
            print(e,"\n")
            return answer
    return answer



def classifition_re(result_dict):
    import re
    answer=result_dict["response"]
    try:
            pattern = re.compile(r'[^。！？\\n：:]+.$',re.S)
            match = re.findall(pattern,answer)
            text = match[-1]
            
            print(text,"\n")
            return text 
    except Exception as e:
        print(e)
        return answer
        


def result_process_lora(result_dict,qtype):
    answer=result_dict["response"]
    if(qtype!="问答"):
        import re
        try:
           pattern = re.compile(r'[^。！？\\n]+.$',re.S)
           match = re.findall(pattern,answer)
           text = match[-1]
           print(text,"\n")
           findre=re.compile(r'([A-D])(?!.*\1)',re.S)
           result = re.findall(findre, text)
           result.sort()   
           result = '、'.join(result)
           return result
        except Exception as e:
            print(e)
            try:
                pattern = re.compile(r'[^。！？\\n]+[。！？]$',re.S)
                match = re.findall(pattern,answer)
                text = match[-1]
                print(text,"\n")
                findre=re.compile(r'([A-D])(?!.*\1)',re.S)
                result = re.findall(findre, text)
                result.sort()   
                result = '、'.join(result)
                return result
            except:   
                return answer
            
    return answer


def result_process_openai(answer,qtype=None):
     if(qtype!="问答"):
        import re
        try:
           pattern = re.compile(r'[^。！？\\n]+.$',re.S)
           match = re.findall(pattern,answer)
           text = match[-1]
           print(text,"\n")
           findre=re.compile(r'([A-D])(?!.*\1)',re.S)
           result = re.findall(findre, text)
           result.sort()   
           result = '、'.join(result)
           return result
        except Exception as e:
            print(e)
            try:
                pattern = re.compile(r'[^。！？\\n]+[。！？]$',re.S)
                match = re.findall(pattern,answer)
                text = match[-1]
                print(text,"\n")
                findre=re.compile(r'([A-D])(?!.*\1)',re.S)
                result = re.findall(findre, text)
                result.sort()   
                result = '、'.join(result)
                return result
            except:   
                return answer  

     return answer

def result_local_lora(answer,qtype):
    if(qtype!="问答"):
        import re
        try:
           pattern = re.compile(r'[^。！？\\n]+.$',re.S)
           match = re.findall(pattern,answer)
           text = match[-1]
           print(text,"\n")
           findre=re.compile(r'([A-D])(?!.*\1)',re.S)
           result = re.findall(findre, text)
           result.sort()   
           result = '、'.join(result)
           return result
        except Exception as e:
            print(e)
            try:
                pattern = re.compile(r'[^。！？\\n]+[。！？]$',re.S)
                match = re.findall(pattern,answer)
                text = match[-1]
                print(text,"\n")
                findre=re.compile(r'([A-D])(?!.*\1)',re.S)
                result = re.findall(findre, text)
                result.sort()   
                result = '、'.join(result)
                return result
            except:   
                return answer
            
    return answer