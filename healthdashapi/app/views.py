import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from app.extract import extractFileData
from app.master_config import MASTER_PARAMS
from app.utils import get_file_type, set_working_dir
from app.aggregate import aggregateData

@csrf_exempt
@require_http_methods(["POST"])
def aggregate_data(request):
    # Parse the request body as JSON
    data = json.loads(request.body)
    print("data",data)

    # Get the file_path and type from the parsed JSON
    file_path = data.get('file_path')
    medical_type = data.get('type')
    print("file_path",file_path)
    print("request",request)
    set_working_dir()
    file_type = get_file_type(file_path)
    print("file_type",file_type)
    extracted_data = extractFileData(file_path, file_type)
    data = aggregateData(extracted_data, result_type='DEXA')

    # Parse the data string into actual JSON
    data_json = json.loads(data)

    # Create a new dictionary with 'success' and 'data' parameters
    response_data = {
        'success': True,
        'data': data_json
    }

    return JsonResponse(response_data, safe=False)