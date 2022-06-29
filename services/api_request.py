import requests
from settings.configuration import API, REQUEST_GIBDD, REQUEST_PHOTO, REQUEST_FINES, REQUEST_PRICE, REQUEST_FSSP, \
    REQUEST_TAXI, REQUEST_API
from settings.messages import car_report_message, fines_message, fssp_message


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
    'fssp': REQUEST_FSSP,
    'api': REQUEST_API
}


def get_response(type, params):
    return requests.get(urls[type], params=params)


def request_cash():
    request_params = params
    request_params.update({'type': 'balance'})
    report = get_response('api', request_params)
    report_dict = report.json()
    return report_dict


def request_operations():
    request_params = params
    request_params.update({'type': 'operations'})
    report = get_response('api', request_params)
    report_dict = report.json()
    return report_dict


def request_gibdd(vin):
    request_params = params
    types = ['gibdd', 'restrict', 'wanted', 'dtp', 'eaisto']
    report_dict = {}
    for item in types:
        request_params.update({'type': item, 'vin': vin})
        report = get_response(item, request_params)
        report_dict[item] = report.json()
    return report_dict


def request_photo(regnumber):
    request_params = params
    request_params.update({'type': 'regnum', 'regNum': regnumber})
    report = get_response('photo', request_params)
    report_dict = report.json()
    return report_dict


def request_fines(regnum, sts):
    request_params = params
    request_params.update({'type': 'fines', 'regNumber': regnum, 'stsNumber': sts})
    report = get_response('fines', request_params)
    report_dict = report.json()
    return report_dict




def request_models(marka):
    request_params = params
    request_params.update({'type': 'chekmodel', 'marka': marka})
    report = get_response('chekmodel', request_params)
    report_dict = report.json()
    return report_dict


def request_year(marka, model):
    request_params = params
    request_params.update({'type': 'chekyear', 'marka': marka, 'model': model})
    report = get_response('chekyear', request_params)
    report_dict = report.json()
    return report_dict


def request_price(cache, probeg):
    request_params = params
    request_params.update({'type': 'price',
                           'marka': cache['marka'],
                           'model': cache['model'],
                           'year': cache['year'],
                           'probeg': probeg
                           })
    report = get_response('price', request_params)
    report_dict = report.json()
    return report_dict


def request_regions():
    request_params = params
    request_params.update({'type': 'regionsList'})
    report = get_response('fssp', request_params)
    report_dict = report.json()
    return report_dict



def request_fssp(data):
    request_params = params
    request_params.update(
        {
            'type': 'physical',
            'firstname': data['firstname'],
            'lastname': data['lastname'],
            'secondname': data['secondname'],
            'region': data['region']
        }
    )
    report = get_response('fssp', request_params)
    print(report.json())
    report_dict = report.json()
    return report_dict
