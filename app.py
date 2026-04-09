from flask import Flask, request, render_template
from utils import extract_text_from_pdf, calculate_match, extract_skill_scores
from ai import get_ai_feedback

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    missing_skills = []
    feedback = None
    skill_data = None
    error = None

    if request.method == 'POST':
        try:
            print("STEP 1: File received")

            file = request.files.get('resume')
            job_desc = request.form.get('job_desc')

            if job_desc:
                job_desc = job_desc.strip()

                print("JOB DESC:", job_desc)

            if not file or file.filename == "":
                error = "Please upload a resume"
                return render_template('index.html', error=error)

            print("STEP 2: Extracting text")
            resume_text = extract_text_from_pdf(file)

            if not resume_text:
                return "❌ Could not read PDF properly"

            print("STEP 3: Calculating match")
            score, missing_skills = calculate_match(resume_text, job_desc)

            print("STEP 4: Running AI")

            try:
                feedback = get_ai_feedback(resume_text, job_desc, score)
            except Exception as e:
                print("AI ERROR:", e)
    
                feedback = f"""
            Resume Score: {score}%

            🔍 Basic Feedback:
            - Add more keywords related to '{job_desc}'
            - Improve project descriptions
            - Highlight technical skills clearly
            - Use action verbs (developed, built, designed)

            ⚠️ AI unavailable (quota issue)
            """
            

            print("STEP 5: Skill scores")
            skill_data = extract_skill_scores(resume_text)

            print("DONE")

        except Exception as e:
            print("ERROR:", e)
            error = str(e)

    return render_template(
        'index.html',
        score=score,
        missing_skills=missing_skills,
        feedback=feedback,
        skill_data=skill_data,
        error=error
    )

if __name__ == '__main__':
    app.run(host="0.0.0.o", port=7860)