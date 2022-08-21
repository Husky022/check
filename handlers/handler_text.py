from handlers.handler import Handler
from settings import configuration
from services import api_request, validators, errors_handlers, pdf_creator
from settings.messages import car_report_message, fines_message, fssp_message
from pprint import pprint


fake_data = {'company': {'date': '26.03.2018',
             'inquiry': {'attempts': 1, 'price': 0.2, 'speed': 0},
             'marka': 'Mercedes-Benz',
             'namets': 'A-Class (тип 176),B-Class (тип 246),C-Class (тип '
                       '205),CLA Coupe (тип 117),GLA (тип 156)',
             'organizator': 'АКЦИОНЕРНОЕ ОБЩЕСТВО "МЕРСЕДЕС-БЕНЦ РУС"',
             'reasons': 'Причина отзыва транспортных средств: при '
                        'недостаточном заземлении рулевой колонки и '
                        'одновременном повреждении токопроводящих дорожек '
                        'внутри кассеты витых пружин в блоке подрулевых '
                        'переключателей подушка безопасности водителя может '
                        'сработать из-за электростатического разряда. О '
                        'повреждении данных токопроводящих дорожек водителю '
                        'заранее сообщается путём предупреждающего сообщения о '
                        'подушке безопасности на комбинации приборов, а также '
                        'с помощью контрольной лампы подушки безопасности. '
                        'Необоснованное срабатывание подушки безопасности '
                        'водителя может привести к риску травмирования '
                        'водителя, а также повысить риск возникновения аварии',
             'recommendation': 'На всех транспортных средствах будет выполнена '
                               'проверка, и, при необходимости, доработка  '
                               'рулевой колонки',
             'status': 200},
 'decoder': {'ABS': {'title': 'ABS', 'value': None},
             'Adress1': {'title': 'Адрес 1', 'value': 'Mercedesstrasse 137'},
             'Adress2': {'title': 'Адрес 2', 'value': 'D-70546 Stuttgart'},
             'Body': {'title': 'Тип кузова',
                      'value': '5 Doors Combi - Vehicle'},
             'Body_type': {'title': 'Отличие кузова',
                           'value': 'Combi - Vehicle'},
             'Country': {'title': 'Страна', 'value': 'Germany'},
             'Displacement': {'title': 'Рабочий объем двигателя',
                              'value': '1991'},
             'Displacement_nominal': {'title': 'Объем двигателя',
                                      'value': '2.0'},
             'Driveline': {'title': 'Трансмиссия',
                           'value': 'Chassis With 4-Matic-/All-Wheel Drive'},
             'Emission_standard': {'title': 'Стандарт выбросов',
                                   'value': 'Euro 6'},
             'Engine': {'title': 'Тип двигателя', 'value': 'L4'},
             'Engine_valves': {'title': 'Количество клапанов', 'value': '16'},
             'Fuel': {'title': 'Тип топлива', 'value': 'Бензин'},
             'HorsePower': {'title': 'Мощность л.с.', 'value': '360-381'},
             'KiloWatts': {'title': 'Мощность двигателя кВт',
                           'value': '265-280'},
             'Make': {'title': 'Марка', 'value': 'Mercedes-Benz'},
             'Manufactured': {'title': 'Произведено в', 'value': 'Германия'},
             'Manufacturer': {'title': 'Производитель', 'value': 'Daimler AG'},
             'Model': {'title': 'Модель', 'value': 'A 45 AMG'},
             'Note': {'title': 'Примечание',
                      'value': 'Manufacturer builds more than 500 vehicles per '
                               'year'},
             'Number_doors': {'title': 'Количество дверей', 'value': '5'},
             'Number_seats': {'title': 'Количество мест', 'value': None},
             'Optional_equipment': {'title': 'Дополнительное оборудование',
                                    'value': ['Нет данных ']},
             'Region': {'title': 'Регион', 'value': 'Europe'},
             'Serial_number': {'title': 'Серийный номер', 'value': '279894'},
             'Standard_equipment': {'title': 'Стандартное оборудование',
                                    'value': ['Нет данных ']},
             'Transmission': {'title': 'Тип трансмиссии',
                              'value': '7-Speed Automatic'},
             'VDS': {'title': 'VDS', 'value': '1760521J'},
             'VIN': {'title': 'VIN', 'value': 'WDD1760521J279894'},
             'VIN_type': {'title': 'Тип VIN', 'value': 'normal'},
             'VIS identifier': {'title': 'VIS идентификатор', 'value': 'N/A'},
             'WMI': {'title': 'WMI', 'value': 'WDD'},
             'Year': {'title': 'Год', 'value': '2014'},
             'Year_identifier': {'title': 'Идентификатор года', 'value': '1'},
             'classCar': {'title': 'Класс авто', 'value': None},
             'cylinders': {'title': 'Количество цилиндров', 'value': '4'},
             'gearbox': {'title': 'Механическая коробка передач',
                         'value': None},
             'inquiry': {'attempts': 1, 'price': 0.4, 'speed': 2},
             'logo': {'title': 'Изображение логотипа в base64',
                      'value': 'data:image/png;base64,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'},
             'typeCar': {'title': 'Тип авто', 'value': None}},
 'dtp': {'cache': {'actual': '21.08.2022 12:13:39',
                   'start': {'date': '21.08.2022 06:27:19',
                             'timestamp': 1661052439},
                   'stop': {'date': '21.08.2022 18:27:19',
                            'timestamp': 1661095639}},
         'count': 0,
         'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 1},
         'records': [],
         'status': 200},
 'eaisto': {'cache': {'actual': '21.08.2022 12:13:46',
                      'start': {'date': '21.08.2022 06:27:20',
                                'timestamp': 1661052440},
                      'stop': {'date': '21.08.2022 18:27:20',
                               'timestamp': 1661095640}},
            'count': 1,
            'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 0},
            'records': [{'body': 'WDD1760521J279894',
                         'brand': 'Mercedes-Benz',
                         'chassis': 'ОТСУТСТВУЕТ',
                         'dcDate': '2022-04-29',
                         'dcExpirationDate': '2024-04-29',
                         'dcNumber': '067391032201606',
                         'model': 'A45',
                         'num': 1,
                         'odometerValue': '96106',
                         'operatorName': '06739',
                         'pointAddress': '192019, Санкт-Петербург Город, '
                                         'Санкт-Петербург г., Седова ул., дом '
                                         '5, ',
                         'previousDcs': [{'dcDate': '2017-06-15',
                                          'dcExpirationDate': '2019-06-15',
                                          'dcNumber': '081600011710710',
                                          'odometerValue': '34100'},
                                         {'dcDate': '2019-06-17',
                                          'dcExpirationDate': '2021-06-18',
                                          'dcNumber': '059880071903612',
                                          'odometerValue': '44950'}],
                         'vin': 'WDD1760521J279894'}],
            'status': 200},
 'fedresurs': {'inquiry': {'attempts': 1, 'price': 0.6, 'speed': 6},
               'message': 'Авто в базе лизинга не найдено',
               'num': 0,
               'status': 200},
 'gibdd': {'cache': {'actual': '21.08.2022 12:13:18',
                     'start': {'date': '21.08.2022 06:27:19',
                               'timestamp': 1661052439},
                     'stop': {'date': '21.08.2022 18:27:19',
                              'timestamp': 1661095639}},
           'found': True,
           'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 3},
           'ownershipPeriod': [{'from': '20.06.2014',
                                'lastOperation': '01',
                                'lastOperationInfo': 'регистрация новых, '
                                                     'произведенных в России '
                                                     'или ввезенных, а также '
                                                     'ввезенных в Россию '
                                                     'бывших в эксплуатации, в '
                                                     'том числе временно на '
                                                     'срок более 6 месяцев, '
                                                     'испытательной техники',
                                'period': '7 лет 10 месяцев 15 дней',
                                'simplePersonType': 'Natural',
                                'simplePersonTypeInfo': 'Физическое лицо',
                                'to': '29.04.2022'},
                               {'from': '29.04.2022',
                                'lastOperation': '03',
                                'lastOperationInfo': 'Изменение собственника '
                                                     '(владельца) в результате '
                                                     'совершения сделки, '
                                                     'вступления в наследство, '
                                                     'слияние и разделение '
                                                     'капитала у юридического '
                                                     'лица, переход права по '
                                                     'договору лизинга, '
                                                     'судебные решения и др.',
                                'period': '0 лет 3 месяца 24 дня',
                                'simplePersonType': 'Natural',
                                'simplePersonTypeInfo': 'Физическое лицо',
                                'to': 'null'}],
           'status': 200,
           'utilicazia': 0,
           'utilicaziainfo': '',
           'vehicle': {'bodyNumber': 'WDD1760521J279894',
                       'category': 'В',
                       'color': 'СИНИЙ ЯРКИЙ',
                       'engineNumber': '80012778',
                       'engineVolume': '1991.0',
                       'model': 'MERCEDES BENZ БЕЗ МОДЕЛИ А45 АМG 4МАТIС',
                       'powerHp': '360.0',
                       'powerKwt': '265',
                       'type': '29',
                       'typeinfo': 'Легковые автомобили прочие',
                       'vin': 'WDD1760521J279894',
                       'year': '2014'},
           'vehiclePassport': {'issue': 'ТАМОЖНЯ: 10009210',
                               'number': '77УО070949'}},
 'notary': {'inquiry': {'attempts': 1, 'price': 0.6, 'speed': 17},
            'message': 'В базе залогов не найдено',
            'num': 0,
            'status': 200},
 'osago': {'count': 1,
           'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 14},
           'rez': [{'brandmodel': 'MERCEDES-BENZ A45 AMG MERCEDES-BENZ A45 AMG '
                                  '(категория «B»)',
                    'cel': 'Личная',
                    'dateactual': '21.08.2022',
                    'insured': 'Х***** ШАМИЛЬ НИЯЗОВИЧ 01.07.1993',
                    'kbm': '0.83',
                    'kuzovNumber': None,
                    'maxMassa': None,
                    'nomer': '0237468752',
                    'numberID': '1',
                    'ogran': 'Ограничен список лиц, допущенных к управлению '
                             '(допущено: 1 чел.)',
                    'orgosago': 'АО "ГСК "Югория"',
                    'owner': 'Х***** ШАМИЛЬ НИЯЗОВИЧ 01.07.1993',
                    'power': '360.00',
                    'region': 'Татарстан Респ',
                    'regnum': 'Транспортное средство не зарегистрировано',
                    'seria': 'ХХХ',
                    'sledToRegorTo': 'Нет',
                    'status': 'Действует',
                    'strahsum': '13255.85 руб.',
                    'term': 'Период использования ТС активен на запрашиваемую '
                            'дату',
                    'trailer': 'Нет',
                    'vin': 'WDD1760521J279894'}],
           'status': 200},
 'price': {'inquiry': {'attempts': 1, 'price': 0.3, 'speed': 7},
           'message': 'Отсутствует расчетная стоимость автомобиля.',
           'status': 200},
 'report_id': 'Wdd1760521j279894',
 'restrict': {'cache': {'actual': '21.08.2022 12:13:26',
                        'start': {'date': '21.08.2022 06:27:19',
                                  'timestamp': 1661052439},
                        'stop': {'date': '21.08.2022 18:27:19',
                                 'timestamp': 1661095639}},
              'count': 0,
              'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 2},
              'message': 'Ограничения отсутствуют',
              'status': 200},
 'taxi': {'records': []},
 'wanted': {'cache': {'actual': '21.08.2022 12:13:33',
                      'start': {'date': '21.08.2022 06:27:19',
                                'timestamp': 1661052439},
                      'stop': {'date': '21.08.2022 18:27:19',
                               'timestamp': 1661095639}},
            'count': 0,
            'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 1},
            'message': 'В розыске не найдено',
            'status': 200}}




class HandlerText(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def incorrect_input_regnumber(self, message):
        self.bot.send_message(message.chat.id, 'Введите корректный номер авто формата Х777ХХ197. Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def incorrect_input_stsnumber(self, message):
        self.bot.send_message(message.chat.id, 'Введите корректный номер CTC. Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def incorrect_input_mileage(self, message):
        self.bot.send_message(message.chat.id, 'Введите корректное значение пробега. Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def incorrect_input_vin(self, message):
        self.bot.send_message(message.chat.id, 'Введите корректный VIN (17 знаков). Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def incorrect_input_fio(self, message):
        self.bot.send_message(message.chat.id, 'Введены некорректные данные. Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def incorrect_input_username(self, message):
        self.bot.send_message(message.chat.id, 'Пользователь не найден. Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def get_photos_report(self, message):
        alert, answer = errors_handlers.photos(api_request.request_photo(message.text))
        # alert, answer = api_request.request_photo(message.text)
        if not alert:
            for el in answer:
                self.bot.send_message(message.chat.id, el, parse_mode='HTML')
        else:
            self.bot.send_message(message.chat.id, answer,
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.reset_user_data(message)

    def get_gibdd_report(self, message):
        self.bot.send_message(message.chat.id, "Подождите минутку, готовим информацию",
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        alert, answer = api_request.request_gibdd(message.text)
        # alert, answer = False, fake_data  # заглушка
        if alert:
            msg_to_user = answer['gibdd'].get('message', 'Ошибка в работе сервисе, повторите попытку позже')
            self.bot.send_message(message.chat.id, msg_to_user,
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())
            self.DB.reset_user_data(message)
        if not alert:
            print('set cache')
            pprint(answer)
            self.DB.set_user_cache(message, answer)

            msg_to_user = car_report_message(answer)

            self.bot.send_message(message.chat.id, msg_to_user,
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.save_report_with_btn_back())
            self.DB.set_user_state(message, configuration.STATES['READY_TO_GET_PDF'])
            # self.DB.reset_user_data(message)
            # pdf = pdf_creator.CarReport(answer)

    def get_fines_report(self, message, regnum):
        alert, answer = errors_handlers.fines(api_request.request_fines(regnum, message.text))
        if not alert:
            msg_to_user = fines_message(answer)
        else:
            msg_to_user = answer
        self.bot.send_message(message.chat.id, msg_to_user,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.reset_user_data(message)

    def get_price(self, message, cache, probeg):
        alert, answer = errors_handlers.car_price(api_request.request_price(cache, probeg))
        if not alert:
            msg_to_user = f"Ориентировочная рыночная стоимость составляет {answer['cost']} руб.\n " \
                          f"Если рассматривать Traid In, то {answer['cost_trade_in']} руб."
        else:
            msg_to_user = answer
        self.bot.send_message(message.chat.id, msg_to_user,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.reset_user_data(message)

    # работа с фото

    def handle(self):

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['DEFAULT'])
        def default_message(message):
            user = self.DB.choose_user(message)

            self.bot.send_message(message.chat.id, 'Выберите в главном меню доступное действие',
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.start_menu(user))

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['PHOTO_SET_REGNUMBER'])
        def entering_number_photo(message):
            if validators.reg_numder(message.text):
                self.get_photos_report(message)
                self.DB.reset_user_data(message)
            else:
                self.incorrect_input_regnumber(message)

        # работа с отчетом по vin

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['GIBDD_SET_VIN'])
        def entering_vin_gibdd(message):
            if validators.vin(message.text):
                self.get_gibdd_report(message)
                # self.DB.reset_user_data(message)
            else:
                self.incorrect_input_vin(message)

        # работа со штрафами

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['FINES_SET_REGNUMBER'])
        def entering_regnum_fines(message):
            if validators.reg_numder(message.text):
                self.DB.set_user_state(message, configuration.STATES['FINES_SET_STSNUMBER'])
                self.DB.set_user_cache(message, {'regnum': message.text})
                self.bot.send_message(message.chat.id, 'Теперь введите номер свидетельства ТС',
                                      parse_mode='HTML',
                                      reply_markup=self.keyboards.menu_with_btn_back())
            else:
                self.incorrect_input_regnumber(message)

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['FINES_SET_STSNUMBER'])
        def entering_sts_fines(message):
            if validators.sts_number(message.text):
                current_user = self.DB.choose_user(message)
                self.get_fines_report(message, current_user.cache['regnum'])
                self.DB.reset_user_data(message)
            else:
                self.incorrect_input_stsnumber(message)

        # работа с оценкой

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['PRICE_SET_PROBEG'])
        def entering_probeg_checkprice(message):
            if validators.mileage(message.text):
                current_user = self.DB.choose_user(message)
                self.get_price(message, current_user.cache, message.text)
                self.DB.reset_user_data(message)
            else:
                self.incorrect_input_mileage(message)

        # работа с фссп

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['FSSP_FIO'])
        def entering_fio_fssp(message):
            alert, answer = errors_handlers.regions(api_request.request_regions())
            if not alert:
                if validators.fio(message.text):
                    self.DB.set_user_state(message, configuration.STATES['FSSP_REGION_NAME'])
                    user_data = message.text.split()
                    if len(user_data) == 3:
                        self.DB.set_user_cache(message,
                                               {
                                                   'lastname': message.text.split()[0],
                                                   'firstname': message.text.split()[1],
                                                   'secondname': message.text.split()[2]
                                               })
                    elif len(user_data) == 2:
                        self.DB.set_user_cache(message,
                                               {
                                                   'lastname': message.text.split()[0],
                                                   'firstname': message.text.split()[1],
                                                   'secondname': None
                                               })
                    self.bot.send_message(message.chat.id, 'Выберите регион поиска',
                                          parse_mode='HTML',
                                          reply_markup=self.keyboards.keybord_inline(list(answer)))
                else:
                    self.incorrect_input_fio(message)
            else:
                self.bot.send_message(message.chat.id, answer,
                                      parse_mode='HTML',
                                      reply_markup=self.keyboards.menu_with_btn_back())

        # добавка подписки пользователю

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['ADD_SUBSCRIBE'])
        def entering_username(message):
            current_user = self.DB.choose_user_for_add_subscribe(message.text)
            if current_user:
                self.DB.set_user_cache(message,
                                       {
                                           'subscribe_for_user': message.text
                                       })
                self.DB.set_user_state(message, configuration.STATES['QT_SUBSCRIBES'])
                self.bot.send_message(message.chat.id, 'Сколько запросов добавить?',
                                      parse_mode='HTML',
                                      reply_markup=self.keyboards.keybord_inline([x for x in range(1, 9)]))

            else:
                self.incorrect_input_username(message)
