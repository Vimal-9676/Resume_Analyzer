from flask import Flask, render_template, request
from utils import extract_text_from_pdf, calculate_match, extract_skill_scores
from ai import get_ai_feedback

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    missing_skills = []
    feedback = None
    skill_data = None

    if request.method == 'POST':
        try:
            file = request.files['resume']
            job_desc = request.form['job_desc']

            if file.filename == "":
                return render_template('index.html', error="Please upload a file")

            resume_text = extract_text_from_pdf(file)

            score, missing_skills = calculate_match(resume_text, job_desc)

            # AI call (safe)
            try:
                feedback = get_ai_feedback(resume_text, job_desc, score)
            except:
                feedback = "⚠️ AI is busy. Try again later."

            skill_data = extract_skill_scores(resume_text)

        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template(
        'index.html',
        score=score,
        missing_skills=missing_skills,
        feedback=feedback,
        skill_data=skill_data
    )
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)