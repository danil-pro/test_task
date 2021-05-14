import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
BASE_CUR = 'EUR'
SERVICE_URL = f'http://api.exchangeratesapi.io/v1/latest?base={BASE_CUR}&access_key={ACCESS_KEY}'

DB_PATH = 'db/db.txt'
DB_CACHE_TIME = 10 * 60

MESSAGES = {
    'service_error': 'No exchange rate data is available for the selected currency.',
    'error': 'Something is wrong, please try again later.',
    'exchange_format_error': 'Not the right format. Ex: 10 EUR TO UAH'
}