import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def calculate_match(resume, job_desc):
    text = [resume, job_desc]

    cv = CountVectorizer().fit_transform(text)
    similarity = cosine_similarity(cv)[0][1]

    score = round(similarity * 100, 2)

    # simple skill gap logic
    jd_words = set(job_desc.lower().split())
    resume_words = set(resume.lower().split())

    missing = list(jd_words - resume_words)[:10]

    return score, missing
def extract_skill_scores(resume_text):
    skills = {
        "Python": 0,
        "SQL": 0,
        "Flask": 0,
        "Machine Learning": 0,
        "Communication": 0,
        "Problem Solving": 0
    }

    text = resume_text.lower()

    if "python" in text:
        skills["Python"] = 90
    if "sql" in text:
        skills["SQL"] = 80
    if "flask" in text:
        skills["Flask"] = 85
    if "machine learning" in text:
        skills["Machine Learning"] = 75
    if "communication" in text:
        skills["Communication"] = 70
    if "project" in text or "problem" in text:
        skills["Problem Solving"] = 80

    return skills