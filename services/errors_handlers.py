def gibdd(data):
    for item in data.keys():
        if data[item].get('status') != 200 or not data[item].get('status'):
            if data[item].get("VIN", None) and data[item].get("WMI", None):
                return None, data
            message = data[item].get('message') + '.\n'
            if data[item].get('errormsg'):
                message += data[item].get('errormsg') + '.\n'
                return True, message + 'Попробуйте заново или повторите ввод позже.'
    if data['gibdd'].get('found') and data['gibdd'].get('vehicle'):
        return None, data
    if not data['gibdd'].get('vehicle'):
        message = data['gibdd'].get('message')
        return True, message


def fines(data):
    if data.get('status') == 200:
        if data.get('num') == 0:
            return True, data.get('message')
        elif data.get('num') > 0:
            return None, data
    elif data.get('status') != 200 or not data[item].get('status'):
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def fssp(data):
    if data.get('status') == 200:
        if data.get('count') == 0:
            return True, data.get('message')
        elif data.get('count') > 0:
            return None, data
    elif data.get('status') != 200 or not data[item].get('status'):
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def regions(data):
    if data.get('status') == 200:
        return None, data.get('rez')
    elif data.get('status') != 200 or not data[item].get('status'):
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def car_price(data):
    if data.get('status') == 200:
        if data.get('cost') and data.get('cost_trade_in'):
            return None, data
        else:
            return True, data.get('message')
    elif data.get('status') != 200 or not data[item].get('status'):
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def photos(data):
    if data.get('status') == 200:
        if data.get('count') == 0 and data.get('message'):
            return True, data.get('message')
        else:
            records_list = data['records']
            images_list = []
            for el in records_list:
                images_list.append(el['bigPhoto'])
            return None, images_list
    elif data.get('status') != 200 or not data[item].get('status'):
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def models(data):
    if data.get('status') == 200:
        if data.get('message'):
            return True, data.get('message')
        else:
            return None, data.get('models')
    elif data.get('status') != 200 or not data[item].get('status'):
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def years(data):
    if data.get('status') == 200:
        if data.get('message'):
            return True, data.get('message')
        else:
            return None, data.get('years')
    elif data.get('status') != 200 or not data[item].get('status'):
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def cash(data):
    if data.get('status') == 200:
        if data.get('message'):
            return True, data.get('message')
        else:
            return None, data
    elif data.get('status') != 200 or not data[item].get('status'):
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def operations(data):
    if data.get('status') == 200:
        if data.get('message'):
            return True, data.get('message')
        else:
            return None, data
    elif data.get('status') != 200 or not data[item].get('status'):
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'