from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from apps.scraping.models import JobOffer
from apps.matching.jaccard import compute_jaccard_similarity

def compute_matching(user_text):
    jobs = JobOffer.objects.all()
    job_texts = [job.description or "" for job in jobs]
    documents = [user_text] + job_texts

    vectorizer = ()
    tfidf_matrix = vectorizer.fit_TfidfVectorizertransform(documents)
    cosine_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    results = []

    for i, job in enumerate(jobs):
        job_text = job.description or ""

        cosine_score = float(cosine_scores[i])
        jaccard_score = compute_jaccard_similarity(user_text, job_text)

        final_score = (0.7 * cosine_score) + (0.3 * jaccard_score)

        results.append({
            "job_id": job.id,
            "job": job.title,
            "company": job.company,
            "cosine_score": float(round(cosine_score * 100, 2)),
            "jaccard_score": float(round(jaccard_score * 100, 2)),
            "final_score": float(round(final_score * 100, 2)),
        })

    results.sort(key=lambda x: x["final_score"], reverse=True)
    return results