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
    set_working_dir()
    file_type = get_file_type("dexa_1.pdf")
    print("file_type",file_type)
    extracted_data = extractFileData("dexa_1.pdf", file_type)
    data = aggregateData(extracted_data, result_type='DEXA')
    return JsonResponse(data)
