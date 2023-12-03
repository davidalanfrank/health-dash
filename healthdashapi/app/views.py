from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def aggregate_data(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET request received"})
    elif request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({"message": "POST request received", "data": data})