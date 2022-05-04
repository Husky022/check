import requests
from settings.configuration import API, REQUEST_GIBDD, REQUEST_PHOTO, REQUEST_FINES, REQUEST_PRICE

api_token = API

params = {
    'token': API
}

urls = {
    'gibdd': REQUEST_GIBDD,
    'restrict': REQUEST_GIBDD,
    'wanted': REQUEST_GIBDD,
    'dtp': REQUEST_GIBDD,
    'eaisto': REQUEST_GIBDD,
    'photo': REQUEST_PHOTO,
    'fines': REQUEST_FINES,
    'price': REQUEST_PRICE,
    'chekmodel': REQUEST_PRICE,
    'chekyear': REQUEST_PRICE,
}


def get_response(type, params):
    if type == 'photo':
        response = requests.get(urls[type], params=params)
        records_list = response.json()['records']
        images_list = []
        for el in records_list:
            images_list.append(el['bigPhoto'])
        return images_list
    else:
        response = requests.get(urls[type], params=params)
        return response


def request_gibdd(vin):
    request_params = params
    types = ['gibdd', 'restrict', 'wanted', 'dtp', 'eaisto']
    report_list = []
    for item in types:
        request_params.update({'type': item, 'vin': vin})
        report = get_response(item, request_params)
        report_list.append(report.json())
    print(report_list)


def request_photo(regnumber):
    request_params = params
    request_params.update({'type': 'regnum', 'regNum': regnumber})
    images_list = get_response('photo', request_params)
    return images_list


def request_fines(regnum, sts):
    request_params = params
    request_params.update({'type': 'fines', 'regNumber': regnum, 'stsNumber': sts})
    report = get_response('fines', request_params)
    print(report.json())
    pass


def request_models(marka):
    request_params = params
    request_params.update({'type': 'chekmodel', 'marka': marka})
    report = get_response('chekmodel', request_params)
    return report.json()['models']


def request_year(marka, model):
    request_params = params
    request_params.update({'type': 'chekyear', 'marka': marka, 'model': model})
    report = get_response('chekyear', request_params)
    return report.json()['years']


def request_price(cache, probeg):
    request_params = params
    request_params.update({'type': 'price',
                           'marka': cache['marka'],
                           'model': cache['model'],
                           'year': cache['year'],
                           'probeg': probeg
                           })
    report = get_response('price', request_params)
    return report.json()


def fssp():
    pass
