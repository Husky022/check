def gibdd(data):

    if data['gibdd'].get('status') == 200 and data['restrict'].get('status') == 200 and data['wanted'].get(
            'status') == 200 and data['dtp'].get('status') == 200 and data['eaisto'].get('status') == 200:
        if data['gibdd'].get('found') and data['gibdd'].get('vehicle'):
            return None, data
        if not data['gibdd'].get('vehicle'):
            message = data['gibdd'].get('message')
            return True, message
    elif data['gibdd'].get('status') != 200:
        message = data['gibdd'].get('message')
        return True, message
    elif data['restrict'].get('status') != 200:
        message = data['restrict'].get('message')
        return True, message
    elif data['wanted'].get('status') != 200:
        message = data['wanted'].get('message')
        return True, message
    elif data['dtp'].get('status') != 200:
        message = data['wanted'].get('message')
        return True, message
    elif data['eaisto'].get('status') != 200:
        message = data['eaisto'].get('message')
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
        if data.get('num') == 0:
            return True, data.get('message')
        elif data.get('num') > 0:
            return None, data
    elif data.get('status') != 200:
        message = data.get('message') + '.\n'
        if data.get('errormsg'):
            message += data.get('errormsg') + '.\n'
        return True, message + 'Попробуйте заново или повторите ввод позже.'