import streamlit as st
import sys
import PyPDF2 as pdf
from src.constants import *
import json
import openai
from src.exception import CustomException
from src.logger import logging




class Jobdescription:
   
        def __init__(self, model):
            self.model = model
            self.max_tokens = 250

        def get_openai_response(self,input_prompt):
            try:
                response = client.chat.completions.create(
                    model= self.model,
                    messages=[
                {"role": "user", "content": input_prompt}],
                    max_tokens=self.max_tokens  # Adjust max_tokens as needed
                )
                logging.info(f"Chat completion: {response.choices[0].message.content}")
                return response.choices[0].message.content
    
            except Exception as e:
                logging.error(f"An error occurred: {CustomException(e,sys)}")




# Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience recuiter
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to provide the detailed job description for a {position}.
Include key skills such as programming languages, frameworks, and technologies required for 
the role. Additionally, specify any preferred qualifications or experience levels.
Job role:{JAVA_DEVELOPER}


I want the response in string having the structure
{{"position":" ","Job Description":" ","preferred qualifications":" ", "Experience level":" " }}
"""

## streamlit app
# st.title("Job Description Generator")
# skills=st.text_area("Paste the skills")
# position = st.text_input("Enter the job position:")


# submit = st.button("Submit")

# if submit:
#     if skills is not None and position:
#         job_description_generator = Jobdescription(model= model)
#         response = job_description_generator.get_openai(input_prompt)
#         st.subheader(response)

if __name__ == "__main__":
    job_description_generator = Jobdescription(model= model)
    response = job_description_generator.get_openai_response(input_prompt)
    print(response)