# views.py
import requests
from decouple import config
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_jobs(request):
    # Get user input (with safe defaults)
    keyword = request.GET.get('q', 'developer').strip()
    location = request.GET.get('l', '').strip()

    # Build params — only add 'where' if location is valid and not "remote"
    params = {
        'app_id': config('ADZUNA_APP_ID'),
        'app_key': config('ADZUNA_APP_KEY'),
        'what': keyword,
        'results_per_page': 20,
    }

    # Optional: skip location if it's "remote" or empty → search globally
    if location and location.lower() not in ['remote', 'anywhere', '']:
        params['where'] = location

    try:
        # Make request to Adzuna
        response = requests.get(
            "https://api.adzuna.com/v1/api/jobs/us/search/1",
            params=params,
            # Bypass system proxy (fixes corporate proxy issues)
            proxies={"http": None, "https": None},
            # Optional: set timeout to avoid hanging
            timeout=10
        )
        response.raise_for_status()  # raises HTTPError for 4xx/5xx

        data = response.json()
        return Response({
            "count": data.get("count", 0),
            "results": data.get("results", [])
        })

    except requests.exceptions.Timeout:
        return Response({"error": "Request timed out"}, status=504)
    except requests.exceptions.RequestException as e:
        # Log internally if needed (avoid exposing keys in logs!)
        return Response({"error": "Failed to fetch jobs from Adzuna"}, status=502)