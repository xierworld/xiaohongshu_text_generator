from prompt import system_template_text, user_template_text
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from xiaohongshu_class import Xiaohongshu
# from dotenv import load_dotenv, find_dotenv
# import os

# load_dotenv(find_dotenv())

def xiaohongshu_generator(theme, api_key):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_template_text + "你必须只返回一段合法的 JSON，不要有任何解释、推理、markdown 代码块标记。"),
            ("user", user_template_text)
        ]
    )

    model = ChatOpenAI(model="deepseek-reasoner", api_key=api_key,
                       base_url="https://api.deepseek.com/v1")
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    parser_instruction = output_parser.get_output_schema()

    chain = prompt | model | output_parser
    chain_result = chain.invoke(
        {
            "parser_instructions": parser_instruction,
            "theme": theme
        }
    )

    return chain_result

# print(xiaohongshu_generator("大模型", os.getenv("deepseek_api_key")))