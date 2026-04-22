import re

COMMON_SKILLS = [
    "python","java","sql","machine learning","deep learning",
    "nlp","data analysis","pandas","numpy","tensorflow",
    "pytorch","aws","docker","power bi","excel"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found.append(skill)

    return found


def get_missing_skills(resume, jd):
    resume_skills = extract_skills(resume)
    jd_skills = extract_skills(jd)

    missing = list(set(jd_skills) - set(resume_skills))

    return missing


def get_suggestions(resume, jd):
    suggestions = []

    resume = resume.lower()
    jd = jd.lower()

    jd_skills = extract_skills(jd)

    # 🔥 Skill-based suggestion
    for skill in jd_skills:
        if skill not in resume:
            suggestions.append(f"Add skill: {skill}")

    # 🔥 Resume improvement
    if "project" not in resume:
        suggestions.append("Add strong projects related to job role")

    if "experience" not in resume:
        suggestions.append("Add relevant work experience")

    if "github" not in resume:
        suggestions.append("Add GitHub profile with projects")

    if len(resume.split()) < 300:
        suggestions.append("Increase resume content with impact points")

    return suggestions