def info_message(version, author):
    message = f" <b>Добро пожаловать в приложение CheckMyVin!</b>\n\n" \
              f" Данное приложение разработано для получения информации актуальных" \
              f" отчетов об автомобиле, штрафах, приблизительной оценке ТС\n\n" \
              f" -<b>Версия программы: - </b><i>{version}</i>\n" \
              f" -<b>Разработчик: - </b><i>{author}</i>"
    return message


# Рендер отчета по авто

def car_report_message(data):
    try:
        vehicle = data['gibdd']['vehicle']
        message_car = f"<b>Отчет об авто {vehicle['model']} {vehicle['vin']} </b>\n\n" \
                      f"<b>Модель:  </b><i>{vehicle['model']}</i>\n" \
                      f"<b>VIN: </b><i>{vehicle['vin']}</i>\n" \
                      f"<b>Номер кузова: </b><i>{vehicle['bodyNumber']}</i>\n" \
                      f"<b>Цвет: </b><i>{vehicle['color']}</i>\n" \
                      f"<b>Год выпуска: - </b><i>{vehicle['year']}</i>\n" \
                      f"<b>Объем двигателя, см3: </b><i>{vehicle['engineVolume']}</i>\n" \
                      f"<b>Мощность л.с./кВт: </b><i>{vehicle['powerHp']}/{vehicle['powerKwt']}</i>\n" \
                      f"<b>Тип: </b><i>{vehicle['typeinfo']}</i>\n\n"

        owners_list = data['gibdd']['ownershipPeriod']
        message_owners_general = f"<b>Сведения о собственниках:</b>\n\n" \
                                 f"<b>Количество собственников: </b><i>{len(owners_list)}</i>\n\n"

        i_owner = 1
        message_owners_detail = " "

        while i_owner <= len(owners_list):
            cur_owner = owners_list[i_owner - 1]
            cur_owner_info = f"<b>{i_owner}й собственник - </b><i>{cur_owner['simplePersonTypeInfo']}</i>\n" \
                             f"<b>Предшествующая операция: - </b><i>{cur_owner['lastOperationInfo']}</i>\n" \
                             f"<b>Период владения: - </b><i>{cur_owner['period']}</i>"

            if cur_owner['to'] == 'null':
                cur_ownership = f"<i>c {cur_owner['from']} по настоящее время</i>\n\n"
            else:
                cur_ownership = f"<i>c {cur_owner['from']} по {cur_owner['to']}</i>\n\n"

            message_owners_detail = message_owners_detail + cur_owner_info + cur_ownership

            i_owner += 1

        restricts = data['restrict']
        message_restricks = f"<b>Сведения об ограничениях: </b>\n\n"

        if restricts['count'] == 0:
            message_restricks += "<i>Ограничения отсутсвуют </i>\n\n"
        else:
            i_restrict = 1
            restricts_list = restricts['records']
            while i_restrict <= len(restricts_list):
                cur_restrict = restricts_list[i_restrict - 1]
                cur_restrict_info = f"<b>Номер ограничения - {cur_restrict['num']}</b>\n" \
                                    f"<b>Вид ограничения: </b><i>{cur_restrict['ogrkodinfo']}</i>\n" \
                                    f"<b>Основание: </b><i>{cur_restrict['osnOgr']}</i>\n" \
                                    f"<b>Дата наложения ограничения: </b><i>{cur_restrict['dateogr']}</i>\n" \
                                    f"<b>Дата окончания ограничения: </b><i>{cur_restrict['dateadd']}</i>\n\n"

                message_restricks += cur_restrict_info

                i_restrict += 1

        dtp_message = "<b>Сведения о ДТП: </b>\n\n"
        dtp = data['dtp']

        if dtp['count'] == 0:
            dtp_message += "<i>Сведения о ДТП отсутствуют </i>\n\n"
        else:
            i_dtp = 1
            dtp_list = dtp['records']
            while i_dtp <= len(dtp_list):
                cur_dtp = dtp_list[i_dtp - 1]
                cur_dtp_info = f"<b>Номер ДТП - </b>{cur_dtp['num']}\n" \
                               f"<b>Дата и время ДТП: - </b><i>{cur_dtp['AccidentDateTime']}</i>\n" \
                               f"<b>Описание ДТП: - </b><i>{cur_dtp['DamageDestription']}</i>\n" \
                               f"<b>Место ДТП: - </b><i>{cur_dtp['AccidentPlace']}</i>\n\n"
                dtp_message += cur_dtp_info

                i_dtp += 1

        wanted_message = "<b>Сведения о розыске </b>\n\n"
        wanted = data['wanted']

        if wanted['count'] == 0:
            wanted_message += "<i>В розыске не найдено </i>\n\n"
        else:
            i_wanted = 1
            wanted_list = wanted['records']
            while i_wanted <= len(wanted_list):
                cur_wanted = wanted_list[i_wanted - 1]
                cur_wanted_info = f"<b>Номер розыска - </b><i>{cur_wanted['num']}</i>\n" \
                                  f"<b>Регион инициатора розыска: - </b><i>{cur_wanted['w_reg_inic']}</i>\n" \
                                  f"<b>Дата постановки в розыск: - </b><i>{cur_wanted['w_data_pu']}</i>\n\n"
                wanted_message += cur_wanted_info

                i_wanted += 1

        eaisto_message = "<b>Сведения о диагностических картах </b>\n\n"
        eaisto = data['eaisto']

        if eaisto['count'] == 0:
            eaisto_message += "<i>Сведения отсутствуют </i>\n\n"
        else:
            i_eaisto = 1
            eaisto_list = eaisto['records']
            while i_eaisto <= len(eaisto_list):
                cur_eaisto = eaisto_list[i_eaisto - 1]
                eaisto_message += f"<b>Номер записи - </b><i>{cur_eaisto['num']}</i>\n" \
                                  f"<b>Дата окончания диагностической карты: - </b><i>{cur_eaisto['dcExpirationDate']}</i>\n" \
                                  f"<b>Пункт выдачи диагностической карты: - </b><i>{cur_eaisto['pointAddress']}</i>\n" \
                                  f"<b>Номер диагностической карты: - </b><i>{cur_eaisto['dcNumber']}</i>\n" \
                                  f"<b>Показания одометра: - </b><i>{cur_eaisto['odometerValue']}</i>\n\n"

                for item in cur_eaisto['previousDcs']:
                    eaisto_message += f"<b>Предыдущее значение одометра: - </b><i>{item['dcNumber']}</i>\n" \
                                      f"<b>Номер диагностической карты: - </b><i>{item['dcNumber']}</i>\n\n"

                i_eaisto += 1

        message = message_car + message_owners_general + message_owners_detail \
                  + message_restricks + dtp_message + wanted_message + eaisto_message

        print('отчет по авто готов')

        return message
    except KeyError:
        return 'Проблема на стороне API. Обратитесь к разработчику'


# Рендер отчета по штрафам

def fines_message(data):
    try:
        message = f"<b>Найдено штрафов - {data['num']}. Подробнее:</b>\n\n"

        i_fine = 1
        fines_list = data['rez']
        while i_fine <= len(fines_list):
            cur_fine = fines_list[i_fine - 1]
            message += f"<i>Номер штрафа - {cur_fine['numfines']}</i>\n" \
                       f"<b>Описание:  </b><i>{cur_fine['KoAPtext']}</i>\n" \
                       f"<b>Статья:  </b><i>{cur_fine['KoAPcode']}</i>\n" \
                       f"<b>Сумма:  </b><i>{cur_fine['Summa']}</i>\n" \
                       f"<b>Постановление:  </b><i>{cur_fine['NumPost']}</i>\n" \
                       f"<b>Дата постановления:  </b><i>{cur_fine['DatePost']}</i>\n\n"

            i_fine += 1

        return message
    except KeyError:
        return 'Проблема на стороне API. Обратитесь к разработчику'


# Рендер отчета по фссп

def fssp_message(data):
    try:
        message = f"<b>Найдено записей - {data['countAll']}</b>. Подробнее: \n\n"

        i_deb = 1
        debtors_list = data['records']
        while i_deb <= len(debtors_list):
            cur_deb = debtors_list[i_deb - 1]
            cur_message = f"<i>Номер записи - {i_deb}</i>\n" \
                          f"<b>Должник:  </b><i>{cur_deb['debtor_name']}</i>\n" \
                          f"<b>Дата рождения:  </b><i>{cur_deb['debtor_dob']}</i>\n" \
                          f"<b>Номер производства:  </b><i>{cur_deb['process_title']}</i>\n"
            # f"<b>Н.П.:  </b><i>{cur_deb['debtor_address']}</i>\n" \
            # f"<b>Исполнительный документ:  </b><i>{cur_deb['recIspDoc']}</i>\n" \
            # f"<b>Тип:  </b><i>{cur_deb['subject']}</i>\n" \
            # f"<b>Орган:  </b><i>{cur_deb['document_organization']}</i>\n" \
            # f"<b>Офицер:  </b><i>{cur_deb['officer_name']}</i>\n" \
            # f"<b>Номера телефонов:  </b><i>{cur_deb['officer_phones']}</i>\n"
            message += cur_message
            i_deb += 1

        return message
    except KeyError:
        return 'Проблема на стороне API. Обратитесь к разработчику'


def cash_message(data):
    try:
        message = f"<b>Текущий баланс - {data['balance']} руб.</b>."
        return message
    except KeyError:
        return 'Проблема на стороне API. Обратитесь к разработчику'


def operations_message(data):
    try:
        message = f"<b>Количество операций пополнения: </b><i>{data['countPay']}</i>.\n" \
                  f"<b>Успешных запросов: </b><i>{data['countPaytoApi']}</i>.\n" \
                  f"<b>Возвраты за неуспешные запросы: </b><i>{data['countBack']}</i>."
        return message
    except KeyError:
        return 'Проблема на стороне API. Обратитесь к разработчику'
