prompt={
    "question":
    """
    <已知信息>{{ context }}</已知信息>
    参考已知信息，回答下面的问题，请将答案放在最后一句并以句号结尾：{{ question }}
    """,
    "empty":
    """{{ question }}""",
    "单选":
    """
    你现在是一位电气工程师，现在有一道单选题，请给出一个正确选项，必要时给出解析过程。
    {{question}}
    """,
    "问答":
    """
    你现在是一位电气工程师，以下是一道与电气相关的问答题，请给出一个正确的回答。
    {{question}}
    """,
    "多选":
    """
    你现在是一位电气工程师，现在有一道多选题，请选出二至三个正确选项，必要时给出解析过程。
    {{question}}
    """,
    "单选kb":
    """
    你现在是一位电气工程师，现在有一道单选题，请根据已知信息给出一个正确选项，必要时给出解析过程。
    已知信息：{{ context }}；
    问题：{{question}}。
    """,
    "问答":
    """
    你现在是一位电气工程师，以下是一道与电气相关的问答题，请根据已知信息给出一个正确的回答。
    已知信息：{{ context }}；
    问题：{{question}}。
    """,
    "多选":
    """
    你现在是一位电气工程师，现在有一道多选题，请根据已知信息选出二至三个正确选项，必要时给出解析过程。
    已知信息：{{ context }}；
    问题：{{question}}。
    """

}

def template_load(prompt_name=""):
    from jinja2 import Template
    template_string = prompt[prompt_name] # 定义模板字符串
    template = Template(template_string)# 加载模板
    return template


