import requests
from settings.configuration import API, REQUEST_GIBDD, REQUEST_PHOTO, REQUEST_FINES, REQUEST_PRICE, REQUEST_FSSP, REQUEST_TAXI
from settings.messages import car_report_message


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
    'taxi': REQUEST_TAXI,
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
    report_dict = {}
    for item in types:
        request_params.update({'type': item, 'vin': vin})
        report = get_response(item, request_params)
        report_dict[item] = report.json()
    print(report_dict)
    return car_report_message(model=report_dict['gibdd']['vehicle']['model'],
                              vin=report_dict['gibdd']['vehicle']['vin'],
                              date='06/05/22',
                              body_number=report_dict['gibdd']['vehicle']['bodyNumber'],
                              color=report_dict['gibdd']['vehicle']['color'],
                              year=report_dict['gibdd']['vehicle']['year'],
                              engine_volume=report_dict['gibdd']['vehicle']['engineVolume'],
                              hp=report_dict['gibdd']['vehicle']['powerHp'],
                              kWt=report_dict['gibdd']['vehicle']['powerKwt'],
                              car_type=report_dict['gibdd']['vehicle']['typeinfo'],
                              passport=report_dict['gibdd']['vehiclePassport']['number'],
                              owners_list=report_dict['gibdd']['ownershipPeriod'],
                              restrict_dict=report_dict['restrict'],
                              dtp_dict=report_dict['dtp'],
                              wanted_dict=report_dict['wanted'],
                              eaisto_dict=report_dict['eaisto']
                              )


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


def request_regions():
    request_params = params
    request_params.update({'type': 'regionsList'})
    report = get_response('fssp', request_params)
    return report.json()['rez']


def request_fssp_fiz(data):
    request_params = params
    request_params.update(
        {
            'type': 'physical',
            'firstname': data['firstname'],
            'lastname': data['lastname'],
            'region': data['region']
        }
    )
    report = get_response('fssp', request_params)
    return report.json()


def request_fssp_yur(data):
    request_params = params
    request_params.update(
        {
            'type': 'legal',
            'nameLegal': data['yurname'],
            'region': data['region']
        }
    )
    report = get_response('fssp', request_params)
    return report.json()


def request_fssp_id(data):
    request_params = params
    request_params.update(
        {
            'type': 'ip',
            'number': data['number_ip']
        }
    )
    report = get_response('fssp', request_params)
    return report.json()
