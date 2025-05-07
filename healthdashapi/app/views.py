import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from app.extract import extractFileData
from app.master_config import MASTER_PARAMS
from app.utils import get_file_type, set_working_dir
from app.aggregate import aggregateData
import boto3
import os
from django.utils import timezone

from .models.core_document import CoreDocument
from botocore.exceptions import ClientError


@csrf_exempt
@require_http_methods(["POST"])
def aggregate_data(request):
    # Parse the request body as JSON
    data = json.loads(request.body)

    # Get the file_path and type from the parsed JSON
    file_path = data.get('file_path')
    medical_type = data.get('type')
 
    set_working_dir()
    file_type = get_file_type(file_path)

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



@csrf_exempt
@require_http_methods(["POST"])
def extract_data(request):
    data = json.loads(request.body)
    file_name = data.get('file_name')
    # print(file_name)
    # s3_client = boto3.client('s3')
    # properties = [attr for attr in dir(s3_client) if not callable(getattr(s3_client, attr))]
    # print(properties)
    # print(os.getcwd())
    bucket_name = "healthdash"
    # s3_client = boto3.client('s3')

    # try:                                       
    #     response = s3_client.download_file(bucket_name, file_name, "data/blood/dexa_1.pdf")
    # except ClientError as e:
    #     print(e)
    #     return None
    # file_exists = False
    # file_path = "data/blood/" + file_name
    # if os.path.isfile(file_path):
    #     print(f"The file '{file_name}' exists.")
    #     file_exists = True
    # else:
    #     print(f"The file '{file_name}' does not exist.")
        
    # if file_exists:
    #     # set_working_dir()
    #     file_type = get_file_type(file_path)

    #     extracted_data = extractFileData(file_path, file_type)
    #     data = aggregateData(extracted_data, result_type='DEXA')

    #     # Parse the data string into actual JSON
    #     data_json = json.loads(data)
    
    json_string = '{"scan_information": {"scan_date": "18 November 2023", "scan_type": "a Whole Body", "operator": "AMC", "model": "Image not for diagnostic use 327 x 150"}, "patient_information": {"name": "WEBSTER, DAVID AF", "patient_id": "DAFW3107", "dob": "31 July 1993"}, "results": {"area_cm2": [253.31, 242.77, 169.41, 153.61, 145.5, 55.93, 262.23, 417.46, 420.29, 2120.52, 247.64, 2368.16], "bmc_g": [222.28, 232.32, 128.2, 114.62, 137.27, 71.29, 373.19, 586.0, 590.53, 2455.68, 571.69, 3027.38], "bmd_g_cm2": [0.878, 0.957, 0.757, 0.746, 0.943, 1.275, 1.423, 1.404, 1.405, 1.158, 2.309, 1.278], "t_score": [-1.3, -0.6, -1.0, -0.2, -1.3, 0.1, 0.0, -0.0], "z_score": [-1.4, -0.5, -0.9, -0.3, -1.4, -0.1, 0.0, 0.0], "percentiles": {"am": [16, 22, 17, 29, 26, 20], "yn": [20, 27, 23, 32, 29, 25]}, "total_body_fat_percent": {"am": 16.5, "yn": 19.0}, "fat_mass_height_ratio": 3.78, "android_gynoid_ratio": 1.02, "trunk_legs_fat_mass_ratio": 0.79, "trunk_limb_fat_mass_ratio": 0.86, "est_vat_mass_g": 313, "est_vat_volume_cm3": 339, "est_vat_area_cm2": 65.0, "lean_height_ratio": {"am": 18.3, "yn": 26}, "appendicular_lean_height_ratio": {"am": 8.29, "yn": 30}, "bmc_lean_mass_g": [3703.1, 3814.9, 29915.8, 10640.8, 10523.6, 58598.2, 4068.8, 62667.0], "fat_mass_g": [548.1, 642.3, 5266.6, 2497.8, 2428.4, 11383.2, 958.1, 12341.3], "lean_mass_g": [3480.9, 3582.6, 29091.2, 10054.8, 9933.1, 56142.6, 3497.1, 59639.7], "total_mass_g": [4251.3, 4457.3, 35182.3, 13138.6, 12952.0, 69981.4, 5026.9, 75008.4]}}'
    data = json.loads(json_string)
    
    

    print(data)
    # Create a new dictionary with 'success' and 'data' parameters
    response_data = {
        'success': True,
        'data': data
    }
        

    return JsonResponse(response_data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def presigned_url(request):
    data = json.loads(request.body)
    file_name = data.get('file_name')
    bucket_name = MASTER_PARAMS['bucket_name']
    expiration = MASTER_PARAMS['expiration']
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')

    try:                                       
        response = s3_client.generate_presigned_post(
        Bucket = bucket_name,
        Key = file_name,
        ExpiresIn = expiration
        )
    except ClientError as e:
        print(e)
        return None

    response_data = {
        'success': True,
        'data': response
    }

    return  JsonResponse(response_data, safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def test(request):
    # file_type = get_file_type(MASTER_PARAMS['dex_test_file'])

    # extracted_data = extractFileData(MASTER_PARAMS['dex_test_file'], file_type)

    # data = aggregateData(extracted_data, result_type='DEXA')
    
    document = CoreDocument(
    user_id=123,  # replace with actual user_id
    document_type='test',  # replace with actual document_type
    location='test_location',  # replace with actual location
    doc_label_exception_id=False,  # replace with actual doc_label_exception_id
    name='test_name',  # replace with actual name
    file_type='test_file_type',  # replace with actual file_type
    status='test_status',  # replace with actual status
    created_at=timezone.now(),
    updated_at=timezone.now()
    )

    # Save the instance to the database
    document.save()
    print(document.document_id)
    data = {
        'success': True,
        'data': 'test'
    }
    return JsonResponse(data, safe=False)

