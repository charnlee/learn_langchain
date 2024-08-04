from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os

os.environ["NVIDIA_API_KEY"] = "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"

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser = StrOutputParser()

model = ChatNVIDIA(model = "meta/llama3-70b-instruct")

chain = prompt_template | model | parser