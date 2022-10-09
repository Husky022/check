# from transliterate import translit
#
# text = 'УS3ЕD49Е863501038'
#
# ru_text = translit(text, 'ru', reversed=True)
#
# print(ru_text)

# model = 'MERCEDES BENZ А45 АМG 4МАТIС'
#
# model = model.replace('БЕЗ МОДЕЛИ ', '')
#
# print(model)
#
# text = 'Wdd1760521j279894'
#
# text = text.upper()
#
# print(text)

from base64 import b64encode
from hashlib import md5
from time import time
import requests
from pprint import pprint
import datetime


url_spectrum = 'https://b2b-api.spectrumdata.ru/b2b/api/v1/'


def generate_token(user: str, password: str, age: int = 60 * 60 * 24) -> str:
    timestamp = int(time())

    print(timestamp)

    password_hash = b64encode(md5(password.encode()).digest()).decode()

    hash_with_salt = f"{timestamp}:{age}:{password_hash}"
    salted_hash_b64 = b64encode(md5(hash_with_salt.encode()).digest()).decode()

    print(salted_hash_b64)

    token = f"{user}:{timestamp}:{age}:{salted_hash_b64}"
    token_b64 = b64encode(token.encode()).decode()

    return token_b64


def request_balance(token, report_type):
    url_current = url_spectrum + 'user/balance/' + report_type + '@iqworks'
    resp = requests.get(url_current,
                        headers={'Accept': 'application/json',
                                 'Authorization': 'AR-REST ' + token})
    return resp.json()


def request_validation_token(token):
    url_current = url_spectrum + 'user'
    resp = requests.get(url_current,
                        headers={'Accept': 'application/json',
                                 'Authorization': 'AR-REST ' + token})
    return resp.json()


def request_insurance_payments(token, report_type):
    url_current = url_spectrum + 'user/reports/' + report_type + '@iqworks/_make'
    params = {
        "queryType": "VIN",
        "query": "Z94CB41BAFR231870"
    }
    resp = requests.get(url_current,
                        headers={'Accept': 'application/json',
                                 'Authorization': 'AR-REST ' + token},
                        params=params)
    return resp.json()


def request_make_report(token, report_type):
    url_current = url_spectrum + 'user/reports/' + report_type + '@iqworks/_make'
    params = {
        "queryType": "GRZ",
        "query": "С106МТ797"
    }
    resp = requests.get(url_current,
                        headers={'Accept': 'application/json',
                                 'Authorization': 'AR-REST ' + token},
                        params=params)
    return resp.json()


def request_get_report(token, report_uid):
    url_current = url_spectrum + 'user/reports/report_check_vehicle_eyJ0eXBlIjoiR1JaIiwiYm9keSI6ItChMTA20JzQojc5NyIsInNjaGVtYV92ZXJzaW9uIjoiMS4wIiwic3RvcmFnZXMiOnt9fQ==@iqworks'
    params = {
        "_content": "true"
    }
    resp = requests.get(url_current,
                        headers={'Accept': 'application/json',
                                 'Authorization': 'AR-REST ' + token},
                        params=params)
    return resp.json()


if __name__ == '__main__':

    api_token = generate_token(
        user='admin_integration@iqworks',
        password='L5EiMP84'
    )
    print(api_token)

    # pprint(request_validation_token(api_token))
    # pprint(request_make_report(api_token, 'report_check_vehicle'))
    pprint(request_get_report(api_token, 'report_check_vehicle'))
    # pprint(request_balance(api_token, 'report_check_vehicle'))



