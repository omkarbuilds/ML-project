from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS   # ✅ ADD
from parser import extract_text
from matcher import get_similarity
from analyzer import get_missing_skills, get_suggestions

app = Flask(__name__)
CORS(app)   # ✅ ADD

@app.route("/")
def home():
    return "Backend running 🚀"


@app.route("/")
def landing():
    return send_from_directory("../frontend", "landing.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")
    jd = request.form.get("jd")

    if not file or not jd:
        return jsonify({"error": "Missing file or JD"}), 400

    resume_text = extract_text(file)

    score = get_similarity(resume_text, jd)
    missing = get_missing_skills(resume_text, jd)
    suggestions = get_suggestions(resume_text)

    return jsonify({
        "score": score,
        "missing_skills": missing,
        "suggestions": suggestions
    })

if __name__ == "__main__":
    app.run(debug=True)