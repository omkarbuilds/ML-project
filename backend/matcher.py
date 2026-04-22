from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(resume, jd):
    tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    vectors = tfidf.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    # 🔥 make score realistic
    return round(score * 100 + 20, 2) if score < 0.5 else round(score * 100, 2)