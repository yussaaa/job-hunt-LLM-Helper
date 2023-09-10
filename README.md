# job-hunt-LLM-Helper

LLM web application to help candidate with the following tasks:

1. Summarize resume
2. Summarize LinkedIn job posting description from URL
3. Skill match between the JD requirement and the skills listed in the resume

## Usage:

#### a. Environment setup

1. Clone the repo to local
1. Create a virtual environment by `python -m venv venv/` and activate the virtual environment by `source /venv/bin/activate`
1. pip install the the packages listed in requirement.txt by `pip install -r requirements.txt`
1. Save the OpenAI API key to .env file in the ditectory in the following format `OPENAI_API_KEY = ''
openai_organization=''
SERPAPI_API_KEY = '`

#### b. Using the app

1. Starting the streamlit app by `streamlit run main.py`
1. Input the path and hit button below to read and extract the keywords from the PDF resume file
1. Input the URL to the LinkedIn job posting page to summarize the job descripton
1. Hit the `Skill Match` button to start comparision between the skills mentioned in the job description with the skills mentioned in the resume

## Future improvement:

1. Input box in UI allowing user input API keys for easier user experience
1. Deploy the app on a server for easier user experience
1. Include more job hunting functionalities
