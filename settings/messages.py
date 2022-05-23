

def info_message(version, author):

    message = f"""
    
    <b>Добро пожаловать в приложение CheckMyVin !</b>
    
    Данное приложение разработано для получения информации актуальных отчетов об автомобиле, штрафах, приблизительной 
    оценке ТС
    
    -<b>Версия программы: - </b><i>{version}</i>
    -<b>Разработчик: - </b><i>{author}</i>
    
    """
    return message


# Рендер отчета по авто

def car_report_message(data):
    print(data)
    vehicle = data['gibdd']['vehicle']
    message_car = f"Отчет об авто {vehicle['model']} {vehicle['vin']} Модель: - {vehicle['model']} " \
                  f"VIN: {vehicle['vin']} Номер кузова: - {vehicle['bodyNumber']} Цвет: - <b><i>" \
                  f"{vehicle['color']}</i></b>" \
                  f"Год выпуска: - <b><i>{vehicle['year']}</i>-</b>Объем двигателя, см3: - <b>" \
                  f"<i>{vehicle['engineVolume']}</i>-</b>Мощность л.с./кВт: - <b><i>{vehicle['powerHp']}/" \
                  f"{vehicle['powerKwt']}</i></b>" \
                  f"-Тип: - <b><i>{vehicle['typeinfo']}</i></b>"
    
    owners_list = data['gibdd']['ownershipPeriod']
    message_owners_general = f"Сведения о собственниках: Количество собственников: - </b><i>{len(owners_list)}</i>"

    i_owner = 1
    message_owners_detail = " "

    while i_owner <= len(owners_list):
        cur_owner = owners_list[i_owner - 1]
        cur_owner_info = f"<i>{i_owner}й собственник - {cur_owner['simplePersonTypeInfo']}</i>" \
                         f"<b>Предшествующая операция: - </b><i>{cur_owner['lastOperationInfo']}</i>" \
                         f"<b>Период владения: - {cur_owner['period']}</b>"

        if cur_owner['to'] == 'null':
            cur_ownership = f"<i>c {cur_owner['from']} по настоящее время</i>"
        else:
            cur_ownership = f"<i>c {cur_owner['from']} по {cur_owner['to']}</i>"

        message_owners_detail = message_owners_detail + cur_owner_info + cur_ownership

        i_owner += 1

    restricts = data['gibdd']['restrict']
    message_restricks = f"<b>Сведения об ограничениях: </b>"

    if restricts['count'] == 0:
        message_restricks += "<i>Ограничения отсутсвуют </i>"
    else:
        i_restrict = 1
        restricts_list = restricts['records']
        while i_restrict <= len(restricts_list):
            cur_restrict = restricts_list[i_restrict - 1]
            cur_restrict_info = f"<i>Номер ограничения - {cur_restrict['num']}</i><b>Вид ограничения: " \
                                f"- {cur_restrict['ogrkodinfo']}</b><b>Основание: - {cur_restrict['osnOgr']}</b>" \
                                f"<b>Дата наложения ограничения: - {cur_restrict['dateogr']}</b>" \
                                f"<b>Дата окончания ограничения: - {cur_restrict['dateadd']}</b>"

            message_restricks += cur_restrict_info

            i_restrict += 1

    dtp_message = "<b>Сведения о ДТП: </b>"
    dtp = data['gibdd']['dtp']

    if dtp['count'] == 0:
        dtp_message += "<i>Сведения о ДТП отсутствуют </i>"
    else:
        i_dtp = 1
        dtp_list = dtp['records']
        while i_dtp <= len(dtp_list):
            cur_dtp = dtp_list[i_dtp - 1]
            cur_dtp_info = f"<i>Номер ДТП - {cur_dtp['num']}</i><b>Дата и время ДТП: - {cur_dtp['AccidentDateTime']}</b>" \
                           f"<b>Описание ДТП: - {cur_dtp['DamageDestription']}</b><b>Место ДТП: -" \
                           f" {cur_dtp['AccidentPlace']}</b>"
            dtp_message += cur_dtp_info

            i_dtp += 1


    wanted_message = "<b>Сведения о розыске </b>"
    wanted = data['wanted']

    if wanted['count'] == 0:
        wanted_message += "<i>В розыске не найдено </i>"
    else:
        i_wanted = 1
        wanted_list = wanted['records']
        while i_wanted <= len(wanted_list):
            cur_wanted = wanted_list[i_wanted - 1]
            cur_wanted_info = f"<i>Номер розыска - {cur_wanted['num']}</i><b>Регион инициатора розыска: -" \
                              f" {cur_wanted['w_reg_inic']}</b><b>Дата постановки в розыск: -" \
                              f" {cur_wanted['w_data_pu']}</b>"
            wanted_message += cur_wanted_info

            i_wanted += 1

    eaisto_message = "<b>Сведения о диагностических картах </b>"
    eaisto = data['eaisto']

    if eaisto['count'] == 0:
        eaisto_message += "<i>Сведения отсутствуют </i>"
    else:
        i_eaisto = 1
        eaisto_list = eaisto['records']
        while i_eaisto <= len(eaisto_list):
            cur_eaisto = eaisto_list[i_eaisto - 1]
            eaisto_message += f"<i>Номер записи - {cur_eaisto['num']}</i><b>Дата окончания диагностической карты: -" \
                              f" </b><i>{cur_eaisto['dcExpirationDate']}</i><b>Пункт выдачи диагностической карты: -" \
                              f" </b><i>{cur_eaisto['pointAddress']}</i><b>Номер диагностической карты: -" \
                              f" </b><i>{cur_eaisto['dcNumber']}</i><b>Показания одометра: -" \
                              f" </b><i>{cur_eaisto['odometerValue']}</i>"

            for item in cur_eaisto['previousDcs']:
                eaisto_message += f"<b>Предыдущее значение одометра: - </b><i>{item['dcNumber']}</i><b>Номер " \
                                  f"диагностической карты: - </b><i>{item['dcNumber']}</i>"

            i_eaisto += 1


    message = message_car + message_owners_general + message_owners_detail \
              + message_restricks + dtp_message + wanted_message + eaisto_message

    print('отчет по авто готов')

    return message


# Рендер отчета по штрафам

def fines_message(data):
    message = f"<b>Найдено штрафов - {data['num']}</b>Подробнее:"

    i_fine = 1
    fines_list = data['rez']
    while i_fine <= len(fines_list):
        cur_fine = fines_list[i_fine - 1]
        message += f"<i>Номер штрафа - {cur_fine['numfines']}</i>" \
                   f"<b>Описание:  </b><i>{cur_fine['KoAPtext']}</i>" \
                   f"<b>Статья:  </b><i>{cur_fine['KoAPcode']}</i>" \
                   f"<b>Сумма:  </b><i>{cur_fine['Summa']}</i>" \
                   f"<b>Постановление:  </b><i>{cur_fine['NumPost']}</i>" \
                   f"<b>Дата постановления:  </b><i>{cur_fine['DatePost']}</i>"

        i_fine += 1

    return message


# Рендер отчета по фссп

def fssp_message(data):
    if data['count'] == 0:
        message = "<b>Совпадений не найдено</b>"
        return message
    else:
        message = f"<b>Найдено записей - {data['countAll']}</b>Подробнее:"

        i_deb = 1
        debtors_list = data['records']
        message_list = []
        message_list.append(message)
        while i_deb <= len(debtors_list):
            cur_deb = debtors_list[i_deb - 1]
            message = f"<i>Номер записи - {i_deb}</i>" \
                      f"<b>Должник:  </b><i>{cur_deb['debtor_name']}</i>" \
                      f"<b>Н.П.:  </b><i>{cur_deb['debtor_address']}</i>" \
                      f"<b>Дата рождения:  </b><i>{cur_deb['debtor_dob']}</i>" \
                      f"<b>Номер производства:  </b><i>{cur_deb['process_title']}</i>" \
                      f"<b>Исполнительный документ:  </b><i>{cur_deb['recIspDoc']}</i>" \
                      f"<b>Тип:  </b><i>{cur_deb['subject']}</i>" \
                      f"<b>Орган:  </b><i>{cur_deb['document_organization']}</i>" \
                      f"<b>Офицер:  </b><i>{cur_deb['officer_name']}</i>" \
                      f"<b>Номера телефонов:  </b><i>{cur_deb['officer_phones']}</i>"
            message_list.append(message)
            i_deb += 1


        return message_list



