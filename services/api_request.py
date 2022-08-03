from datetime import date, timedelta
from pprint import pprint
from transliterate import translit

import requests
from settings.configuration import API, TAXI_API, REQUEST_GIBDD, REQUEST_PHOTO, REQUEST_FINES, REQUEST_PRICE, \
                                              REQUEST_FSSP, \
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
    # types = ['gibdd', 'restrict', 'wanted', 'dtp', 'eaisto', 'notary', 'fedresurs', 'decoder', 'company']
    types = ['gibdd']
    report_dict = {}
    for item in types:
        if item == 'gibdd':
            print('1')
            request_params.update({'type': item, 'vin': vin})
            report = get_response(item, request_params)
            print('2')
            report_json = report.json()
            print('3')
            report_dict[item] = report_json
            print('4')
            if report_json.get('message', None):
                print('5')
                return True, report_dict
            print('6')
            continue
        # if item == 'decoder' or item == 'company':
        #     request_params.update({'type': 'vin', 'vin': vin})
        # else:
        #     request_params.update({'type': item, 'vin': vin})
        # report = get_response(item, request_params)
        # report_dict[item] = report.json()

    # price_params = {'type': 'price',
    #                 'marka': report_dict['decoder']['Make']['value'],
    #                 'model': report_dict['decoder']['Model']['value'],
    #                 'year': report_dict['gibdd']['vehicle']['year'],
    #                 'probeg': (2022 - int(report_dict['gibdd']['vehicle']['year'])) * 10000
    #                 }
    # probeg = (2022 - int(report_dict['gibdd']['vehicle']['year'])) * 7000
    # report = request_price(price_params, probeg)
    # report_dict['price'] = report
    # taxi_dict = {'records': []}
    # periods = report_dict['gibdd']['ownershipPeriod']
    # for owner_period in periods:
    #     av_period = average_period_time(owner_period['from'], owner_period['to'])
    #     osago_params = params
    #     osago_params.update({
    #                         'type': 'osago',
    #                         'vin': report_dict['gibdd']['vehicle']['vin'],
    #                         'date': av_period
    #                         })
    #     osago_report = get_response('osago', osago_params).json()
    #     # pprint(osago_params)
    #     pprint(osago_report)
    #     if report_dict['gibdd']['ownershipPeriod'].index(owner_period) == len(periods) - 1:
    #         report_dict['osago'] = osago_report
    #     if osago_report.get('rez', None):
    #         grz = osago_report['rez'][0]['regnum']
    #         if grz.endswith('RUS'):
    #             grz = grz[:-3]
    #         grz = translit(grz, 'ru')
    #         report_taxi = request_taxi(grz)
    #         pprint(report_taxi)
    #         if report_taxi.get('records'):
    #             if len(report_taxi.get('records')) > 0:
    #                 for item in report_taxi.get('records'):
    #                     taxi_dict['records'].append(item)
    # report_dict['taxi'] = taxi_dict
    pprint(report_dict)
    return None, report_dict


def request_taxi(regnumber):
    taxi_params = {'key': TAXI_API,
                   'regNumber': regnumber
                  }
    report = get_response('taxi', taxi_params)
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


def average_period_time(date_from, date_to):
    if date_to == 'null':
        date_to = str(date.today())
        date_to_list = date_to.split('-')
        d2 = date(int(date_to_list[0]), int(date_to_list[1]), int(date_to_list[2]))
    else:
        date_to_list = date_to.split('.')
        d2 = date(int(date_to_list[2]), int(date_to_list[1]), int(date_to_list[0]))
    date_from_list = date_from.split('.')
    d1 = date(int(date_from_list[2]), int(date_from_list[1]), int(date_from_list[0]))
    current = (str((d2 - d1) / 2 + d1)).split('-')
    current_str = f'{current[2]}.{current[1]}.{current[0]}'
    return current_str
