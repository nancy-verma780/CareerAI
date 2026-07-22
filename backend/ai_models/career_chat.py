import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def ask_career_ai(question, profile):

    prompt = f"""
You are CareerAI, an expert AI career mentor.

Student Profile:
{profile}

Student Question:
{question}

Give:
1. Profile analysis
2. Missing skills
3. Learning roadmap
4. Project suggestions
"""


    response = model.generate_content(prompt)

    return response.text