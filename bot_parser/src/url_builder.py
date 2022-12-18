import os

from bot_parser.src.data_work import get_category, get_brand, get_model


MAIN_URL = 'https://www.mvideo.ru'
TV_URL = 'televizory-i-cifrovoe-tv-1/televizory-65'
LAPTOPS_URL = 'noutbuki-planshety-komputery-8/noutbuki-118'
SMARTPHONES_URL = 'smartfony-i-svyaz-10/smartfony-205'


def url_builder_mvideo(user_request: dict):
    result_url = MAIN_URL
    if get_category(user_request) is 'TV':
        result_url = os.path.join(result_url, TV_URL)
    elif get_category(user_request) is 'Laptops':
        result_url = os.path.join(result_url, LAPTOPS_URL)
    elif get_category(user_request) is 'S':
        result_url = os.path.join(result_url, SMARTPHONES_URL)
