from emoji import emojize


def variants_message():

    message = f"<b>Доступны следующие варианты отчетов</b>\n\n" \
              f"<b>📋 Отчет Лайт:</b>\n\n" \
              f"⚙ Общие сведения об авто\n" \
              f"🕺 История владения\n" \
              f"🏦 Сведения о залогах\n" \
              f"⛔ Сведения об ограничениях\n" \
              f"👮‍♂ Сведения о розыске\n" \
              f"🚧 Сведения о ДТП\n" \
              f"📰 Сведения о штрафах\n" \
              f"👔 Сведения о страховке\n" \
              f"🚕 Сведения о работе в такси\n" \
              f"📷 Фото авто \n" \
              f"🛣 Примерный пробег\n\n" \
              f"<b>📋 Отчет MAX:</b>\n\n" \
              f"Включает в себя <b>Отчет Лайт</b>, а также: \n\n" \
              f"💼 Страховые выплаты \n" \
              f"🛠 Расчеты ремонтных работ \n" \
              f"💻 История размещения объявлений \n"

    return message


def info_message(version, author, reports=None):
    message = f"<b>Добро пожаловать к боту Checkita!</b>\n\n" \
              f"Данный бот разработан для получения информации актуальных" \
              f"отчетов об автомобиле, штрафах, приблизительной оценке ТС\n\n" \
              f"<b>Услуги:</b>\n\n" \
              f"- Отчет по авто - доступно по подписке \n" \
              f"- Оценка авто, Штрафы, Фотография по номеру, ФССП - 3 запроса в день <b>БЕСПЛАТНО</b>," \
              f" далее - доступ по подписке \n\n" \
              f"<b>Тарифы подписки:</b>\n\n" \
              f"1 отчет - 70 руб. \n" \
              f"2 отчета - 120 руб. \n" \
              f"5 отчетов - 180 руб. \n\n" \
              f"Количество доступных отчетов - <b>{reports} шт.</b> \n\n" \
              f"-<b>Версия программы: - </b><i>{version}</i>\n" \
              f"-<b>Разработчик: - </b><i>{author}</i>"
    return message


# Рендер отчета по авто (старый вариант)

# def car_report_message_old(data):
#     try:
#         vehicle = data['gibdd']['vehicle']
#         message_car = f"<b>📋 {vehicle['model'].replace('БЕЗ МОДЕЛИ ', '')} {data['report_id']} </b>\n\n"
#         if 'count' in data["restrict"]:
#             print('restrict true')
#             if data["restrict"]["count"] == 0:
#                 message_car += f"✅ Ограничения не найдены\n"
#             else:
#                 message_car += f"❌ Найдены ограничения\n"
#         else:
#             print('restrict false')
#         message_car += f"🚶 Количество владельцев в ПТС: {len(data['gibdd']['ownershipPeriod'])}\n"
#         if 'count' in data["wanted"]:
#             print('wanted true')
#             if data["wanted"]["count"] == 0:
#                 message_car += f"✅ Нет сведений о розыске\n"
#             else:
#                 message_car += f"❌ Найдены сведения о розыске\n"
#         else:
#             print('wanted false')
#         if 'count' in data["osago"]:
#             if data["osago"]["count"] == 0:
#                 message_car += f"❌ Полис ОСАГО не найден\n"
#             else:
#                 message_car += f"✅ Найден полис ОСАГО\n"
#                 message_car += f"✅ Госномер: {data['osago']['rez'][0]['regnum']}\n"
#         if 'num' in data["notary"]:
#             print('notary true')
#             if data["notary"]["num"] == 0:
#                 message_car += f"✅ Не в залоге\n"
#             else:
#                 message_car += f"❌ Найдены сведения о залоге\n"
#         else:
#             print('notary false')
#         if 'count' in data["company"]:
#             print('company true')
#             if data["company"]["count"] == 0:
#                 message_car += f"✅ Отзывные компании не найдены\n"
#             else:
#                 message_car += f"❌ Найдены отзывные компании\n"
#         else:
#             print('company false')
#         if 'count' in data["dtp"]:
#             if data["dtp"]["count"] == 0:
#                 message_car += f"✅ ДТП не найдены\n"
#             else:
#                 message_car += f"❌ Авто был в ДТП\n"
#         if len(data["taxi"]["records"]) == 0:
#             message_car += f"✅ Нет сведений о работе в такси\n\n"
#         else:
#             message_car += f"🚕 Авто работал в такси\n\n"
#         message_car += f"⬇ Скачайте отчет в PDF ⬇\n\n"
#
#         message = message_car
#         return message
#     except KeyError:
#         return 'Проблема на стороне API. Обратитесь к разработчику'


# Рендер отчета по авто (спектрум)

def car_report_message_spcr(data_inc):
    # try:
        data = data_inc['data'][0]['content']
        vehicle = data['tech_data']
        message_car = f"<b>📋 {vehicle['brand']['name']['original'].upper().replace('БЕЗ МОДЕЛИ ', '')} " \
                      f"{data['identifiers']['vehicle']['vin']} </b>\n\n"
        if data.get("restrictions", None):
            if not data["restrictions"]["registration_actions"]["has_restrictions"]:
                print('restrict true')
                message_car += f"✅ Ограничения не найдены\n"
            else:
                print('restrict false')
                message_car += f"❌ Найдены ограничения\n"
        else:
            print('restrict info not available')
        message_car += f"🚶 Количество владельцев в ПТС: {data['ownership']['history']['count']}\n"
        message_car += f"✅ Госномер: {data['identifiers']['vehicle']['reg_num']}\n"
        if not data['additional_info']['vehicle']['passport']['has_dublicate']:
            message_car += f"✅ ПТС: Оригинал, {data['identifiers']['vehicle']['pts']}\n"
        else:
            message_car += f"✅ ПТС: Дубликат, {data['identifiers']['vehicle']['pts']}\n"
        message_car += f"✅ СТС: {data['identifiers']['vehicle']['sts']}\n"
        if data.get("stealings", None):
            if not data["stealings"]["is_wanted"]:
                print('wanted true')
                message_car += f"✅ Нет сведений о розыске\n"
            else:
                print('wanted false')
                message_car += f"❌ Найдены сведения о розыске\n"
        else:
            print('wanted info not available')
        if data.get("insurance", None):
            if data["insurance"]["osago"]["count"] == 0:
                message_car += f"❌ Полис ОСАГО не найден\n"
            else:
                message_car += f"✅ Найден полис ОСАГО\n"
        if data.get("pledges", None):
            if data["pledges"]["count"] == 0:
                print('pledges true')
                message_car += f"✅ Не в залоге\n"
            else:
                print('pledges false')
                message_car += f"❌ Найдены сведения о залоге\n"
        else:
            print('pledges info not available')
        # if data.get("accidents", None):
        #     if data["company"]["count"] == 0:
        #         message_car += f"✅ Отзывные компании не найдены\n"
        #     else:
        #         message_car += f"❌ Найдены отзывные компании\n"
        # else:
        #     print('company false')
        if data.get("accidents", None):
            if not data["accidents"]["has_accidents"]:
                message_car += f"✅ ДТП не найдены\n"
            else:
                message_car += f"❌ Авто был в ДТП\n"
        else:
            print('accidents info not available')
        if data.get("taxi", None):
            if not data["taxi"]["used_in_taxi"]:
                print('taxi true')
                message_car += f"✅ Нет сведений о работе в такси\n\n"
            else:
                print('taxi false')
                message_car += f"❌ Найдены сведения о работе в такси\n\n"
        else:
            print('taxi info not available')

        message_car += f"⬇ Скачайте отчет в PDF ⬇\n\n"


        return message_car
    # except KeyError:
    #     return 'Проблема на стороне API. Обратитесь к разработчику'


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
        return 'Ошибка в работе сервиса. Обратитесь к разработчику'


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
