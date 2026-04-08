from google import genai
import time

client = genai.Client(api_key="AIzaSyC2eTBTwODgsGMxGDvIUFKyWaESTAcit-4")

def get_ai_feedback(resume_text, job_desc, score):

    prompt = f"""
You are an ATS resume expert.

Resume:
{resume_text}

Job Description:
{job_desc}

Score: {score}

Give:
- Feedback
- Missing skills
- Improvements
"""

    for attempt in range(3):  # retry 3 times
        try:
            response = client.models.generate_content(
                model="models/gemini-2.0-flash",  # use your working model
                contents=prompt
            )
            return response.text

        except Exception as e:
            print(f"Retry {attempt+1} due to error:", e)
            time.sleep(2)

    return "⚠️ AI is busy right now. Please try again later."

