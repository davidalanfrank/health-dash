import utils
from extract import extractFileData
from master_config import MASTER_PARAMS
from utils import get_file_type
from aggregate import aggregateData

file_type = get_file_type(MASTER_PARAMS['dex_test_file'])

extracted_data = extractFileData(MASTER_PARAMS['dex_test_file'], file_type)

data = aggregateData(extracted_data, result_type='DEXA')
print(data['choices']['message']['content'])



