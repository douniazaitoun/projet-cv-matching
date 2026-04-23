from django.http import JsonResponse
from apps.matching.matching_engine import compute_matching

def match_view(request):
    query = request.GET.get("q", "")

    if not query:
        return JsonResponse({"error": "No query provided"})

    results = compute_matching(query)

    return JsonResponse({"results": results})