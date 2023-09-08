import streamlit as st

from src.linkedin_jd_parser import linkedin_jd_parser
from src.pdf_reader import extract_text_from_PDF
from src.langchain_helper import summarize_resume_skills
from src.langchain_helper_chatapi import (
    summarize_job_description,
    resume_jd_skill_match,
)

import os
from dotenv import load_dotenv

load_dotenv()

st.title("Job Hunting LLM ⛓ Helper")
st.text(
    "A LLM tool to \n\
    1. summarize the resume and linkedIn job descriptions, and \n\
    2. match between the skill shown in the job description"
)

# with st.sidebar:
#     resume_skill_extract = st.checkbox("Resume Skills Extraction")
#     linkedin_parsing = st.checkbox("Linkedin Parsing")
#     skill_match = st.checkbox("Skill Match")


with st.form("Resume uploading and skills summarization"):
    resume_path = st.text_input("Path to your resume")

    if resume_path:
        pdf = extract_text_from_PDF(resume_path)
        with st.expander("Reveal the resume"):
            st.write(pdf)

    summarize_resume = st.form_submit_button("Summarize the resume skills")

    if summarize_resume:
        st.write("Sending summarization request to ChatOpenAI ...")
        resume_skill_summary = summarize_resume_skills(pdf)

        st.write("**Resume skills summarized:**")
        st.markdown(resume_skill_summary)

st.divider()

with st.form("LinkedIn job Posting parsing"):
    linkedin_posting_url = st.text_input("LinkedIn Posting URL (Hit Enter to parse)")

    linkedin_posting_parse = st.form_submit_button("Summarize the resume skills")

    if linkedin_posting_parse:
        st.write("Parsing linkedIn job posting ...")
        job_info = linkedin_jd_parser(linkedin_posting_url)
        st.write("Sending request to ChatOpenAI ...")
        jd_summary = summarize_job_description(job_info["Job Description"])
        if jd_summary not in st.session_state:
            st.session_state["jd_summary"] = jd_summary

        st.write("**LinkedIn Job Posting summary:**")
        st.markdown(jd_summary)


st.divider()

skill_match = st.button("Run skill match between job description and resume")

if skill_match:
    if not linkedin_posting_url or not linkedin_posting_parse:
        st.write("**Please input the Job Posting URL and run the parser**")
    if not resume_path:
        st.write("**Please input the path the job posting**")

    st.write("Sending skills matching request to ChatOpenAI ...")
    skill_match_response = resume_jd_skill_match(
        pdf, st.session_state["jd_summary"].split("\n\n")[1]
    )

    st.write("**Skills matching result**")
    st.markdown(skill_match_response)
