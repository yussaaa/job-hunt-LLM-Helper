from langchain.llms import OpenAI
from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os
from dotenv import load_dotenv
load_dotenv()


llm = OpenAI(temperature=0.1, max_tokens=3000)


def summarize_resume_skills(resume):

    prompt_template_resume_skill_summary = PromptTemplate(
    input_variables =['resume'],
    template = "List all the skills/ technoolgies mentioned in the follow resume {resume}"
)

    name_chain = LLMChain(llm=llm, prompt=prompt_template_resume_skill_summary)

    response = name_chain.run(resume)

    return response


def summarize_job_description(jd):

    prompt_template_JD_summary = PromptTemplate(
    input_variables =['jd'],
    template = "Summarize the following Job description {jd} into three parts. 1. What this role need to do 2. What skills does this role require 3. Benefits of working in this company \
                Each part should have 5 bullet points, shorten the bullet points into keywords only, and make sure to include all the technologies. Make sure all the tools and tech mentioned are covered \
                Output to be in markdown format, with bold part tile, bullet point name \n\n \
                "
)

    name_chain = LLMChain(llm=llm, prompt=prompt_template_JD_summary)

    response = name_chain.run(prompt_template_JD_summary)

    return response


def resume_jd_skill_match(resume, job_skills):

    prompt_template_JD_summary = PromptTemplate(
    input_variables = ['resume','job_skills'],
    template = "Compare {job_skills} with the {resume}\
                Show what skills are 1. Fully matched \
                                    2. Partial matched \
                                    3. Not matched"
)

    chain = LLMChain(llm=llm, prompt=prompt_template_JD_summary)

    response = chain.run({"resume": resume, 
                          "job_skills": job_skills})

    return response


