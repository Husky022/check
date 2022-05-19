def gibdd(data):
    print('3')
    if data['gibdd'].get('status') == 200 and data['restrict'].get('status') == 200 and data['wanted'].get(
            'status') == 200 and data['dtp'].get('status') == 200 and data['eaisto'].get('status') == 200:
        if data['gibdd'].get('found') and data['gibdd'].get('vehicle') and data['restrict'].get('count') and data[
            'wanted'].get('count') and data['dtp'].get('count') and data['eaisto'].get('count'):
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
