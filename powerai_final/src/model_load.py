from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained(r"/home/bingxing2/home/scx6d3v/chatglm/lora/LLaMA-Factory-main/pt/2023_final_v2", trust_remote_code=True)
model = AutoModel.from_pretrained(r"/home/bingxing2/home/scx6d3v/chatglm/lora/LLaMA-Factory-main/pt/2023_final_v2", trust_remote_code=True).cuda()
# 多显卡支持，使用下面两行代替上面一行，将num_gpus改为你实际的显卡数量
# from utils import load_model_on_gpus
# model = load_model_on_gpus("THUDM/chatglm2-6b", num_gpus=2)
model = model.eval()

def chat(query):
        response=""
        response, history = model.chat(tokenizer, query, history=[])
        #流式输出
        # for response, history, past_key_values in model.stream_chat(tokenizer, query, history=[],
        #                                                             past_key_values=None,
        #                                                             return_past_key_values=True):
        #     print(end="")
        return response