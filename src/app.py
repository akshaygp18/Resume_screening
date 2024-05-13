import streamlit as st
# import google.generativeai as genai
from openai import OpenAI
import os, sys
import PyPDF2 as pdf
from src.constants import *
from dotenv import load_dotenv
from src.exception import CustomException
from src.logger import logging


load_dotenv() ## load all our environment variables

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

class Score:

    def __init__(self, model):
        self.model = model
        self.max_tokens = 250

    
    def get_openai(self, input):
        try:
            response = client.chat.completions.create(
                model= model,
                messages=[
            {"role": "user", "content": input}],
                max_tokens=self.max_tokens  # Adjust max_tokens as needed
            )
            logging.info(f"Chat completion: {response.choices[0].message.content}")
            return response.choices[0].message.content
        
        except Exception as e:
            logging.error(f"An error occurred: {CustomException(e,sys)}")
    

    def input_pdf_text(uploaded_file):
        try:
            reader=pdf.PdfReader(uploaded_file)
            text=""
            for page in range(len(reader.pages)):
                page=reader.pages[page]
                text+=str(page.extract_text())
            return text
        except Exception as e:
            logging.error(f"An error occurred: {CustomException(e,sys)}")



#Prompt Template

input="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the score out of 10 Matching based on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        score_generator = Score(model = model)
        response=score_generator.get_openai(input)
        st.subheader(response)