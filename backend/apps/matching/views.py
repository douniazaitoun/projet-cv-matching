from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.matching.matching_engine import compute_matching
from apps.nlp_engine.cv_reader import read_cv_file
from apps.nlp_engine.cleaner import clean_cv_text
from apps.auth_users.models import UploadedCV

@csrf_exempt
def match_uploaded_cv_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST method"}, status=405)

    if "cv" not in request.FILES:
        return JsonResponse({"error": "No CV file uploaded"}, status=400)

    cv_file = request.FILES["cv"]

    if not (cv_file.name.endswith(".pdf") or cv_file.name.endswith(".docx")):
        return JsonResponse({"error": "Only PDF and DOCX files are allowed"}, status=400)

    uploaded_cv = UploadedCV.objects.create(file=cv_file)
    file_path = uploaded_cv.file.path

    try:
        cv_text = read_cv_file(file_path)
        cleaned_cv = clean_cv_text(cv_text)
        results = compute_matching(cleaned_cv)

        return JsonResponse({
            "filename": cv_file.name,
            "total_results": len(results),
            "results": results[:10]
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
