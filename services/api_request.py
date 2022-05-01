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
    recors_list = response.json()['records']
    images_list = []
    for el in recors_list:
        images_list.append(el['bigPhoto'])
    return images_list


def request_gibdd():
    pass


def request_photo(regnumber):
    request_params = params
    request_params.update({'type': 'regnum', 'regNum': regnumber})
    images_list = get_response('photo', request_params)
    return images_list


def request_fines():
    pass


def request_price():
    pass
