from fpdf import FPDF, HTMLMixin
from datetime import date

data = {'company': {'count': 0,
             'inquiry': {'attempts': 1, 'price': 0.2, 'speed': 0},
             'message': 'Отзывные компании по указанному VIN отсутствуют',
             'status': 200},
 'decoder': {'ABS': {'title': 'ABS', 'value': 'ABS'},
             'Adress1': {'title': 'Адрес 1', 'value': '1 Mazda Dr'},
             'Adress2': {'title': 'Адрес 2',
                         'value': 'Flat Rock MI 48134-9498,'},
             'Body': {'title': 'Тип кузова', 'value': '2 Doors Coupe'},
             'Body_type': {'title': 'Отличие кузова', 'value': 'Купэ'},
             'Country': {'title': 'Страна', 'value': 'United States'},
             'Displacement': {'title': 'Рабочий объем двигателя',
                              'value': '3720'},
             'Displacement_nominal': {'title': 'Объем двигателя',
                                      'value': '3.7'},
             'Driveline': {'title': 'Трансмиссия', 'value': 'RWD'},
             'Emission_standard': {'title': 'Стандарт выбросов', 'value': None},
             'Engine': {'title': 'Тип двигателя', 'value': 'V6'},
             'Engine_valves': {'title': 'Количество клапанов', 'value': '24'},
             'Fuel': {'title': 'Тип топлива', 'value': 'Бензин'},
             'HorsePower': {'title': 'Мощность л.с.', 'value': '305'},
             'KiloWatts': {'title': 'Мощность двигателя кВт', 'value': '227'},
             'Make': {'title': 'Марка', 'value': 'Ford'},
             'Manufactured': {'title': 'Произведено в',
                              'value': 'Соединенные Штаты'},
             'Manufacturer': {'title': 'Производитель',
                              'value': 'Auto Alliance International Inc'},
             'Model': {'title': 'Модель', 'value': 'Mustang'},
             'Note': {'title': 'Примечание',
                      'value': 'Manufacturer builds more than 500 vehicles per '
                               'year'},
             'Number_doors': {'title': 'Количество дверей', 'value': '2'},
             'Number_seats': {'title': 'Количество мест', 'value': '4'},
             'Optional_equipment': {'title': 'Дополнительное оборудование',
                                    'value': ['Нет данных ']},
             'Region': {'title': 'Регион', 'value': 'North America'},
             'Serial_number': {'title': 'Серийный номер', 'value': '214451'},
             'Standard_equipment': {'title': 'Стандартное оборудование',
                                    'value': ['Engine immobilizer',
                                              'Tachometer',
                                              'AM/FM radio',
                                              'CD player',
                                              'MP3 player',
                                              'Power Steering',
                                              'Tilt steering wheel',
                                              'Daytime running lights',
                                              'Power windows',
                                              'Cloth seats',
                                              'Front air conditioning',
                                              'ABS brakes',
                                              'Alloy wheels']},
             'Transmission': {'title': 'Тип трансмиссии',
                              'value': '6-Speed Automatic or 6-Speed Manual'},
             'VDS': {'title': 'VDS', 'value': 'BP8AM4C5'},
             'VIN': {'title': 'VIN', 'value': '1ZVBP8AM4C5214451'},
             'VIN_type': {'title': 'Тип VIN', 'value': 'normal'},
             'VIS identifier': {'title': 'VIS идентификатор', 'value': 'N/A'},
             'WMI': {'title': 'WMI', 'value': '1ZV'},
             'Year': {'title': 'Год', 'value': '2012'},
             'Year_identifier': {'title': 'Идентификатор года', 'value': 'C'},
             'classCar': {'title': 'Класс авто', 'value': None},
             'cylinders': {'title': 'Количество цилиндров', 'value': '6'},
             'gearbox': {'title': 'Механическая коробка передач',
                         'value': '6MT'},
             'inquiry': {'attempts': 1, 'price': 0.4, 'speed': 2},
             'logo': {'title': 'Изображение логотипа в base64',
                      'value': 'data:image/png;base64,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'},
             'typeCar': {'title': 'Тип авто', 'value': None}},
 'dtp': {'cache': {'actual': '04.07.2022 23:44:44',
                   'start': {'date': '04.07.2022 19:21:22',
                             'timestamp': 1656951682},
                   'stop': {'date': '05.07.2022 07:21:22',
                            'timestamp': 1656994882}},
         'count': 0,
         'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 2},
         'records': [],
         'status': 200},
 'eaisto': {'cache': {'actual': '04.07.2022 23:44:53',
                      'start': {'date': '04.07.2022 19:21:22',
                                'timestamp': 1656951682},
                      'stop': {'date': '05.07.2022 07:21:22',
                               'timestamp': 1656994882}},
            'count': 1,
            'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 1},
            'records': [{'body': '1ZVBP8AM4C5214451',
                         'brand': 'FORD',
                         'chassis': 'ОТСУТСТВУЕТ',
                         'dcDate': '2021-05-22',
                         'dcExpirationDate': '2022-05-22',
                         'dcNumber': '100291012101169',
                         'model': 'Mustang',
                         'num': 1,
                         'odometerValue': '49520',
                         'operatorName': '10029',
                         'pointAddress': '105118, Москва Город, Москва г., '
                                         'Буракова ул., дом д. 14, стр, ',
                         'previousDcs': [{'dcDate': '2017-07-17',
                                          'dcExpirationDate': '2019-07-17',
                                          'dcNumber': '017730031700731',
                                          'odometerValue': '330000'},
                                         {'dcDate': '2018-01-01',
                                          'dcExpirationDate': '2018-07-01',
                                          'dcNumber': '055050031800027',
                                          'odometerValue': '330000'},
                                         {'dcDate': '2012-12-11',
                                          'dcExpirationDate': '2014-12-11',
                                          'dcNumber': '201212110830020404765',
                                          'odometerValue': '8000'}],
                         'vin': '1ZVBP8AM4C5214451'}],
            'status': 200},
 'fedresurs': {'cache': {'actual': '04.07.2022 23:47:24',
                         'start': {'date': '04.07.2022 19:21:23',
                                   'timestamp': 1656951683},
                         'stop': {'date': '05.07.2022 07:21:23',
                                  'timestamp': 1656994883}},
               'inquiry': {'attempts': 1, 'price': 0.6, 'speed': 13},
               'message': 'Авто в базе лизинга не найдено',
               'num': 0,
               'status': 200},
 'gibdd': {'cache': {'actual': '04.07.2022 23:44:12',
                     'start': {'date': '04.07.2022 19:21:21',
                               'timestamp': 1656951681},
                     'stop': {'date': '05.07.2022 07:21:21',
                              'timestamp': 1656994881}},
           'found': True,
           'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 8},
           'ownershipPeriod': [{'from': '19.02.2013',
                                'lastOperation': '15',
                                'lastOperationInfo': 'регистрация ТС, '
                                                     'ввезенных из-за пределов '
                                                     'Российской Федерации',
                                'period': '2 года 12 месяцев 2 дня',
                                'simplePersonType': 'Natural',
                                'simplePersonTypeInfo': 'Физическое лицо',
                                'to': '16.02.2016'},
                               {'from': '16.02.2016',
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
                                'period': '1 год 5 месяцев 4 дня',
                                'simplePersonType': 'Natural',
                                'simplePersonTypeInfo': 'Физическое лицо',
                                'to': '19.07.2017'},
                               {'from': '19.07.2017',
                                'lastOperation': '06',
                                'lastOperationInfo': 'выдача взамен утраченных '
                                                     'или пришедших в '
                                                     'негодность '
                                                     'государственных '
                                                     'регистрационных знаков, '
                                                     'регистрационных '
                                                     'документов, паспортов '
                                                     'транспортных средств.',
                                'period': '3 года 10 месяцев 6 дней',
                                'simplePersonType': 'Natural',
                                'simplePersonTypeInfo': 'Физическое лицо',
                                'to': '20.05.2021'},
                               {'from': '20.05.2021',
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
                                'period': '1 год 1 месяц 15 дней',
                                'simplePersonType': 'Natural',
                                'simplePersonTypeInfo': 'Физическое лицо',
                                'to': 'null'}],
           'status': 200,
           'utilicazia': 0,
           'utilicaziainfo': '',
           'vehicle': {'bodyNumber': '1ZVBP8AM4C5214451',
                       'category': 'В',
                       'color': 'Красный',
                       'engineNumber': None,
                       'engineVolume': '3721.0',
                       'model': 'ФОРД МУСТАНГ ',
                       'powerHp': '305.0',
                       'powerKwt': '224.3',
                       'type': '25',
                       'typeinfo': 'Легковые автомобили купе',
                       'vin': '1ZVBP8AM4C5214451',
                       'year': '2011'},
           'vehiclePassport': {'issue': 'ТАМОЖНЯ: 10505050',
                               'number': '86ТЕ729658'}},
 'notary': {'cache': {'actual': '04.07.2022 23:46:57',
                      'start': {'date': '04.07.2022 19:21:22',
                                'timestamp': 1656951682},
                      'stop': {'date': '05.07.2022 07:21:22',
                               'timestamp': 1656994882}},
            'inquiry': {'attempts': 1, 'price': 0.6, 'speed': 26},
            'message': 'В базе залогов не найдено',
            'num': 0,
            'status': 200},
 'osago': {'cache': {'actual': '04.07.2022 23:45:02',
                     'start': {'date': '04.07.2022 19:21:22',
                               'timestamp': 1656951682},
                     'stop': {'date': '05.07.2022 07:21:22',
                              'timestamp': 1656994882}},
           'count': 1,
           'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 14},
           'rez': [{'brandmodel': 'Ford MUSTANG (категория «B»)',
                    'cel': 'Личная',
                    'dateactual': '04.07.2022',
                    'insured': 'Б***** ИЛЬЯ АЛЕКСАНДРОВИЧ 03.11.1990',
                    'kbm': '0.57',
                    'kuzovNumber': None,
                    'maxMassa': None,
                    'nomer': '0241399511',
                    'numberID': '1',
                    'ogran': 'Ограничен список лиц, допущенных к управлению '
                             '(допущено: 1 чел.)',
                    'orgosago': 'СПАО "Ингосстрах"',
                    'owner': 'Б***** ИЛЬЯ АЛЕКСАНДРОВИЧ 03.11.1990',
                    'power': '305.00',
                    'region': 'г Москва',
                    'regnum': 'Е017ЕЕ197',
                    'seria': 'ХХХ',
                    'sledToRegorTo': 'Нет',
                    'status': 'Действует',
                    'strahsum': '8057.65 руб.',
                    'term': 'Период использования ТС активен на запрашиваемую '
                            'дату',
                    'trailer': 'Нет',
                    'vin': '1ZVBP8AM4C5214451'}],
           'status': 200},
 'restrict': {'cache': {'actual': '04.07.2022 23:44:27',
                        'start': {'date': '04.07.2022 19:21:21',
                                  'timestamp': 1656951681},
                        'stop': {'date': '05.07.2022 07:21:21',
                                 'timestamp': 1656994881}},
              'count': 1,
              'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 1},
              'records': [{'codDL': 0,
                           'codeTo': 47,
                           'dateadd': '30.06.2022',
                           'dateogr': '30.06.2022',
                           'divid': '2',
                           'divtype': '2',
                           'divtypeinfo': 'Судебный пристав',
                           'gid': '77#SP514606238',
                           'num': 1,
                           'ogrkod': '1',
                           'ogrkodinfo': 'Запрет на регистрационные действия',
                           'osnOgr': 'Документ: 619416075/7759 от 30.06.2022, '
                                     'Паршина Екатерина Владимировна, СПИ: '
                                     '45591086405813, ИП: 96234/22/77059-ИП от '
                                     '20.06.2022',
                           'phone': '8(499)583-04-20',
                           'regid': '1145',
                           'regname': 'город Москва',
                           'tsKuzov': '1ZVBP8AM4C5214451',
                           'tsVIN': '1ZVBP8AM4C5214451',
                           'tsmodel': 'Нет данных',
                           'tsyear': '2011'}],
              'status': 200},
 'taxi': {'count': 0, 'message': 'В базе такси не найдено', 'status': 200},
 'wanted': {'cache': {'actual': '04.07.2022 23:44:36',
                      'start': {'date': '04.07.2022 19:21:21',
                                'timestamp': 1656951681},
                      'stop': {'date': '05.07.2022 07:21:21',
                               'timestamp': 1656994881}},
            'count': 0,
            'inquiry': {'attempts': 1, 'price': 0.5, 'speed': 1},
            'message': 'В розыске не найдено',
            'status': 200}}

BORDER_LINE = 0

print(data['dtp'])


class CarReport(FPDF, HTMLMixin):

    def __init__(self, data=data):
        super().__init__()
        self.data = data
        self.create_report()

    def create_report(self):

        self.header_block()
        self.general_info()
        self.summary_brief()
        self.price_block()
        self.owners_block()
        self.restrictions_block()
        self.dtp_block()
        self.output("test_report.pdf")

    def header_block(self):
        self.add_page()
        self.image('../media/logo1.jpg', x=10, y=10, h=20)
        self.add_font('DejaVu', 'B', '../fonts/DejaVuSansCondensed-Bold.ttf', uni=True)
        self.add_font('DejaVu', '', '../fonts/DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', 'B', 18)
        self.cell(40, 0)
        self.cell(125, 15, f'Отчет по {data["gibdd"]["vehicle"]["model"]} VIN {data["gibdd"]["vehicle"]["vin"]}',
                  ln=1, align='C', border=BORDER_LINE)
        self.cell(0, 0, f'от {date.today()}', border=BORDER_LINE, ln=1, align='C')
        self.set_font('DejaVu', 'B', 15)
        self.ln(25)

    def general_info(self):
        # Заголовок блока
        self.cell(40, 0, 'Общие данные по автомобилю:', border=BORDER_LINE, ln=1)
        self.ln(15)
        self.set_font('DejaVu', '', 12)
        # 1я строка
        self.cell(100, 0, f'Модель: {data["gibdd"]["vehicle"]["model"]}', border=BORDER_LINE)
        self.cell(40, 0, f'Год выпуска: {data["gibdd"]["vehicle"]["year"]}', border=BORDER_LINE)
        self.ln(10)
        # 2я строка
        self.cell(100, 0, f'VIN: {data["gibdd"]["vehicle"]["vin"]}', border=BORDER_LINE)
        self.cell(40, 0, f'Цвет: {data["gibdd"]["vehicle"]["color"]}', border=BORDER_LINE)
        self.ln(10)
        # 3я строка
        self.cell(100, 0, f'Номер кузова: {data["gibdd"]["vehicle"]["color"]}', border=BORDER_LINE)
        self.cell(40, 0, f'Объем двигателя: {data["gibdd"]["vehicle"]["engineVolume"]} см3', border=BORDER_LINE)
        self.ln(10)
        # 4я строка
        if data["gibdd"]["vehicle"]["engineNumber"] is None:
            self.cell(100, 0, 'Номер двигателя: Отсутствует', border=BORDER_LINE)
        else:
            self.cell(100, 0, f'Номер двигателя: {data["gibdd"]["vehicle"]["engineNumber"]}', border=BORDER_LINE)
        self.cell(40, 0, f'Мощность: {data["gibdd"]["vehicle"]["powerHp"]} лс / {data["gibdd"]["vehicle"]["powerKwt"]} '
                         f'кВт', border=BORDER_LINE)
        self.ln(10)
        # 5я строка
        self.cell(100, 0, f'Номер ПТС: {data["gibdd"]["vehiclePassport"]["number"]}', border=BORDER_LINE)
        self.cell(40, 0, f'Тип ТС: {data["gibdd"]["vehicle"]["typeinfo"]}', border=BORDER_LINE, ln=1)
        self.ln(10)
        self.set_font('DejaVu', 'B', 15)
        self.ln(25)

    def summary_brief(self):
        # Заголовок блока
        self.cell(40, 0, 'Краткая сводка:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 12)
        self.ln(10)
        # 1я строка
        if data["restrict"]["count"] == 0:
            self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Есть ограничения на регистрацию', border=BORDER_LINE, ln=0)
            self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), h=5)
        else:
            self.image('../media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Ограничения не найдены', border=BORDER_LINE, ln=0)

        self.image('../media/logo-info.png', x=self.get_x(), y=self.get_y(), w=5)
        self.cell(7, 5, border=BORDER_LINE, ln=0)
        self.cell(85, 5, f'Количество владельцев в ПТС: {len(data["gibdd"]["ownershipPeriod"])}', border=BORDER_LINE, ln=1)
        self.ln(5)
        # 2я строка
        if data["wanted"]["count"] == 0:
            self.image('../media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Нет сведений о розыске', border=BORDER_LINE, ln=0)
        else:
            self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Найдены сведения о розыске', border=BORDER_LINE, ln=0)
        if data["osago"]["count"] == 0:
            self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Полис ОСАГО не найден', border=BORDER_LINE, ln=1)
            self.ln(5)
        else:
            self.image('../media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Найден полис ОСАГО', border=BORDER_LINE, ln=1)
            self.ln(5)
        # 3я строка
        if data["notary"]["num"] == 0:
            self.image('../media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Не в залоге', border=BORDER_LINE, ln=0)
        else:
            self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Найдены сведения о залоге', border=BORDER_LINE, ln=0)
        if data["company"]["count"] == 0:
            self.image('../media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Отзывные компании не найдены', border=BORDER_LINE, ln=1)
            self.ln(5)
        else:
            self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Найдены отзывные компании', border=BORDER_LINE, ln=0)
        # 4я строка
        if data["dtp"]["count"] == 0:
            self.image('../media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'ДТП не найдены', border=BORDER_LINE, ln=0)
        else:
            self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Найдено 1 ДТП', border=BORDER_LINE, ln=0)
        if data["taxi"]["count"] == 0:
            self.image('../media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Не найдены сведения о работе в такси', border=BORDER_LINE, ln=1)
            self.ln(5)
        else:
            self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Есть информация о работе в такси', border=BORDER_LINE, ln=1)
            self.ln(5)


    def price_block(self):
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Средняя рыночная стоимость ~ 2 231 380 руб.', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        self.cell(150, 15, 'В Traid-In предложат ~ 1 935 099 руб.', border=BORDER_LINE, ln=0)
        self.ln(10)

    def owners_block(self):
        self.add_page()
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация о собственниках:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        self.image('../media/logo-info.png', x=self.get_x(), y=self.get_y(), w=5)
        self.cell(7, 5, border=BORDER_LINE, ln=0)
        self.cell(85, 5, 'Количество собственников в ПТС: 4', border=BORDER_LINE, ln=0)
        self.ln(20)
        for i in range(4):
            self.set_font('DejaVu', 'B', 14)
            self.cell(85, 10, f'{i + 1}й собственник: Физическое лицо', border=BORDER_LINE, ln=1)
            self.set_font('DejaVu', '', 13)
            self.cell(85, 10, 'Период владения: с 19.07.2017 по 20.05.2021', border=BORDER_LINE, ln=1)
            self.cell(85, 10, 'Срок владения: 3 года 10 месяцев 6 дней', border=BORDER_LINE, ln=1)
            self.ln(10)

    def restrictions_block(self):
        self.add_page()
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация об ограничениях:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
        self.cell(7, 5, border=BORDER_LINE, ln=0)
        self.cell(85, 5, 'Найдено записей: 1', border=BORDER_LINE, ln=0)
        self.ln(10)

    def dtp_block(self):
        self.add_page()
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация о ДТП:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        self.image('../media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
        self.cell(7, 5, border=BORDER_LINE, ln=0)
        self.cell(85, 5, 'Найдено ДТП: 2', border=BORDER_LINE, ln=0)
        self.ln(10)


pdf = CarReport()
