from langchain.chat_models.openai import ChatOpenAI

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os
from dotenv import load_dotenv
load_dotenv()


chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.2, max_tokens=3000)

def summarize_job_description(jd):
    """_summary____

    Args:
        jd (_type_): _description_
    """

    system_message_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
            template="You are summarizing a job description for a chatbot.\
                    Provide a concise summary of the job description in three parts.\
                    Each part has 5 bullet points. Make sure all the skills, technologies are covered.",
            input_variables=[]
            )
)

    human_message_prompt = HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                template="The following is the job description {jd}?",
                input_variables=["jd"],
            )
        )
    chat_prompt_template = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt_template)
    response = chain.run(jd)

    return response


def resume_jd_skill_match(resume, job_skills):

    system_message_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
            template="You are comparing the skills listed in a job description with the skills mentioned in a resume. \
                    Categorize skills in the job description skills into 1. Fully matched, 2. Partial matched, 3. Not matched \
                    ",
            input_variables=[]
            )
)

    human_message_prompt = HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                template="Job description skills: {job_skill_required} \n\
                        Resume {resume} ",
                input_variables=['resume','job_skill_required'],
            )
        )
    chat_prompt_template = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(llm=chat, prompt=chat_prompt_template)
    response = chain.run({'resume': resume, 
                            'job_skill_required': job_skills})

    return response


