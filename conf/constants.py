import os
from dotenv import load_dotenv

load_dotenv()

MAGENTO_URL = os.environ.get("MAGENTO_URL", None)
AUTH = os.environ.get("AUTH", None)
ACTION = os.environ.get("ACTION", None)
COL = ""
API_URL = ""

if ACTION == 'product':
    COL = 'sku'
    API_URL = 'rest/V1/products'

elif ACTION == 'address':
    COL = 'entity_id'
    API_URL = 'rest/V1/addresses'

