def gibdd(data):
    for item in data.keys():
        if data[item].get('status') != 200:
            message = data[item].get('message') + '.\n'
            if data[item].get('errormsg'):
                message += data.get('errormsg') + '.\n'
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
    elif data.get('status') != 200:
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
    elif data.get('status') != 200:
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def regions(data):
    if data.get('status') == 200:
        return None, data.get('rez')
    elif data.get('status') != 200:
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'


def car_price(data):
    if data.get('status') == 200:
        if data.get('count') and data.get('count'):
            return None, data
        else:
            return True, data.get('message')
    elif data.get('status') != 200:
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'
