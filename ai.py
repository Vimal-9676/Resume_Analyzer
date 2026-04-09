from google import genai
import os
from dotenv import load_dotenv
import time

load_dotenv()

# Create client (NEW WAY)
client = genai.Client(api_key=os.getenv("Gemini_API_Key"))

def get_ai_feedback(resume_text, job_desc, score):
    try:
        prompt = f"""
You are an ATS resume expert.

Analyze the resume against the job description.

Return structured feedback:

- Feedback
- Missing skills
- Improvements

Resume:
{resume_text[:2000]}

Job Description:
{job_desc}

ATS Score:
{score}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text if response.text else "No response from AI"

    except Exception as e:
        print("AI ERROR:", e)
        return "⚠️ AI failed. Try again."