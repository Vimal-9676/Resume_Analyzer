import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_ai_feedback(resume_text, job_desc, score):
    try:
        model = model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
You are an ATS resume expert.

Resume:
{resume_text[:2000]}

Job Description:
{job_desc}

Score: {score}

Give:
- Feedback
- Missing skills
- Improvements
"""

        response = model.generate_content(prompt)

        return response.text if response.text else "No response from AI"

    except Exception as e:
        print("AI ERROR:", e)
        return "⚠️ AI failed. Try again."