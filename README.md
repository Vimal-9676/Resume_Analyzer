# 📊 AI Resume Analyzer (ATS Scoring System)

An AI-powered Resume Analyzer that evaluates resumes against job descriptions and provides an **ATS score, missing skills, and AI feedback** using Google Gemini.

---

## 🚀 Live Demo
👉[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=for-the-badge)](https://resume-analyzer-3l6y.onrender.com)
 

---

## 📌 Features

- 📄 Upload and analyze resume (PDF/Text)
- 🧠 AI feedback using Google Gemini API
- 📊 ATS Score calculation
- 🎯 Skill matching with job description
- 💡 Improvement suggestions
- ⚡ Flask-based web app

---

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌐
- Google Gemini API 🤖
- HTML, CSS, JavaScript
- Gunicorn (Production server)
- Render (Deployment)

---

## ⚙️ How It Works

1. User uploads resume
2. Enters job description
3. Resume text is extracted
4. AI compares resume with job requirements
5. System returns:
   - ATS Score
   - Missing Skills
   - Suggestions for improvement

---

## 📂 Project Structure
Resume-Analyzer/
│
├── app.py
├── ai.py
├── utils.py
├── requirements.txt
├── .gitignore
├── Procfile (optional for Render)
├── templates/
│ └── index.html
├── static/
└── README.md

# Clone repository
git clone https://github.com/your-username/resume-analyzer.git

cd resume-analyzer

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py

#Open Browser
http://127.0.0.1:5000
