def gibdd(data):
    print('3')
    print(data['gibdd'].get('found'))
    print(data['gibdd'].get('vehicle'))
    print(True if data['restrict'].get('count') else False)
    print(data['wanted'].get('count'))
    print(data['dtp'].get('count'))
    print(data['eaisto'].get('count'))


    if data['gibdd'].get('status') == 200 and data['restrict'].get('status') == 200 and data['wanted'].get(
            'status') == 200 and data['dtp'].get('status') == 200 and data['eaisto'].get('status') == 200:
        print('smt1')
        if data['gibdd'].get('found') and data['gibdd'].get('vehicle'):
            print('1None, data')
            return None, data
        if not data['gibdd'].get('vehicle'):
            print('smt2')
            message = data['gibdd'].get('message')
            print('2True')
            return True, message
    elif data['gibdd'].get('status') != 200:
        message = data['gibdd'].get('message')
        print('3True')
        return True, message
    elif data['restrict'].get('status') != 200:
        message = data['restrict'].get('message')
        print('4True')
        return True, message
    elif data['wanted'].get('status') != 200:
        message = data['wanted'].get('message')
        print('5True')
        return True, message
    elif data['dtp'].get('status') != 200:
        message = data['wanted'].get('message')
        print('6True')
        return True, message
    elif data['eaisto'].get('status') != 200:
        message = data['eaisto'].get('message')
        print('7True')
        return True, message



def fines(data):
    pass