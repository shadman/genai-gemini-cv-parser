import requests
import os
import textwrap
import google.generativeai as genai

from PyPDF2 import PdfReader
from IPython.display import display
from IPython.display import Markdown

# Used to securely store your API key
from google.colab import userdata

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = "Aasdnmadadsna123123msadasd"
genai.configure(api_key=GOOGLE_API_KEY)

dir_path = os.getcwd()
print(f"path: {dir_path}")

# Function to pre-process CV (replace with your logic)
def preprocess_cv(cv_file):
  print(f"cv file: {cv_file}")

  with open(cv_file, 'rb') as file:
    pdf_reader = PdfReader(file)

    # Extract text from all pages (replace with page range if needed)
    cv_text = ""
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      cv_text += page.extract_text()

  return cv_text


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def parse_cv_with_gemini(uploaded_file):
  model = genai.GenerativeModel('gemini-1.5-flash')  
  cv_text = preprocess_cv(uploaded_file)

  purpose_of_text = "Analyze the candidate by their CV in the text format, return their main information, skills, and what are the main expertise of the candidate. CV is here:" 
  # response = model.generate_content(purpose_of_text + cv_text)
  response = model.generate_content([purpose_of_text, cv_text])
  return to_markdown(response.text)


uploaded_file = "./sample_data/Shadman_Jamil_CV_2024_v2.1.pdf"
parse_cv_with_gemini(uploaded_file)

#other help 
#response.prompt_feedback
#response.candidates
#https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb#scrollTo=5b4Hkfj-pm3p
