from flask import Flask, request, render_template

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
            file = request.files.get('resume')
            job_desc = request.form.get('job_desc')

            if not file or file.filename == "":
                error = "Please upload a resume"
                return render_template('index.html', error=error)

            resume_text = extract_text_from_pdf(file)

            score, missing_skills = calculate_match(resume_text, job_desc)

            # Safe AI call
            try:
                feedback = get_ai_feedback(resume_text, job_desc, score)
            except Exception as e:
                feedback = "⚠️ AI is busy. Please try again."

            skill_data = extract_skill_scores(resume_text)

        except Exception as e:
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
    app.run(debug=True, host='0.0.0.0', port=10000)