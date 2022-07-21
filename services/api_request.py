import requests
from settings.configuration import API, REQUEST_GIBDD, REQUEST_PHOTO, REQUEST_FINES, REQUEST_PRICE, REQUEST_FSSP, \
    REQUEST_TAXI, REQUEST_API, REQUEST_RSA, REQUEST_DECODE, REQUEST_NOTARY, REQUEST_COMPANY, REQUEST_TAXI
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
    'osago': REQUEST_RSA,
    'decoder': REQUEST_DECODE,
    'company': REQUEST_COMPANY,
    'notary': REQUEST_NOTARY,
    'fedresurs': REQUEST_NOTARY,
    'api': REQUEST_API,
    'taxi': REQUEST_TAXI
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
    types = ['gibdd', 'restrict', 'wanted', 'dtp', 'eaisto', 'osago', 'notary', 'fedresurs', 'decoder', 'company']
    report_dict = {}
    for item in types:
        if item == 'decoder' or item == 'company':
            request_params.update({'type': 'vin', 'vin': vin})
        else:
            request_params.update({'type': item, 'vin': vin})
        report = get_response(item, request_params)
        report_dict[item] = report.json()

    grz = report_dict['osago']['rez'][0]['regnum']
    report = request_taxi(grz)
    report_dict['taxi'] = report
    price_params = {'type': 'price',
                    'marka': report_dict['decoder']['Make']['value'],
                    'model': report_dict['decoder']['Model']['value'],
                    'year': report_dict['gibdd']['vehicle']['year'],
                    'probeg': (2022 - int(report_dict['gibdd']['vehicle']['year'])) * 10000
                    }
    probeg = (2022 - int(report_dict['gibdd']['vehicle']['year'])) * 7000
    report = request_price(price_params, probeg)
    report_dict['price'] = report
    return report_dict


def request_taxi(regnumber):
    request_params = params
    request_params.update({'type': 'regnum', 'regnum': regnumber})
    report = get_response('taxi', request_params)
    report_dict = report.json()
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
