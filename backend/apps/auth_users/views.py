from django.shortcuts import render
from apps.nlp_engine.cv_reader import read_cv_file
from apps.nlp_engine.cleaner import clean_cv_text

def match_cv_view(request):
    file = request.FILES['cv']
    
    with open("temp_cv.docx", "wb+") as f:
        for chunk in file.chunks():
            f.write(chunk)

    cv_text = read_cv_file("temp_cv.docx")
    cleaned = clean_cv_text(cv_text)

    results = compute_matching(cleaned)

    return JsonResponse({"results": results})