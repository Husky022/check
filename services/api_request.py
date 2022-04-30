import requests
from settings.configuration import API, REQUEST_GIBDD, REQUEST_PHOTO, REQUEST_FINES, REQUEST_PRICE

api_token = API

params = {
    'token': API
}

urls = {
    'gibdd': REQUEST_GIBDD,
    'photo': REQUEST_PHOTO,
    'fines': REQUEST_FINES,
    'price': REQUEST_PRICE
}


def get_response(type, params):
    response = requests.get(urls[type], params=params)
    print(response.text)
    return response.text


def request_gibdd():
    pass


def request_photo(regnumber):
    request_params = params
    request_params.update({'type': 'regnum', 'regNum': regnumber})
    get_response('photo', request_params)

def request_fines():
    pass


def request_price():
    pass
