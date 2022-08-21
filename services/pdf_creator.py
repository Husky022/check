from fpdf import FPDF, HTMLMixin
from datetime import date


BORDER_LINE = 0


class CarReport(FPDF, HTMLMixin):

    def __init__(self, data):
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
        self.wanted()
        self.dtp_block()
        self.notary()
        self.companies()
        self.osago()
        self.eaisto()
        self.taxi()
        # self.decoder()
        output_document_name = f"./reports/{self.data['report_id']}.pdf"
        self.output(output_document_name)
        return output_document_name


    def header_block(self):
        self.add_page()
        self.image('./media/logo1.jpg', x=10, y=10, h=20)
        self.add_font('DejaVu', 'B', fname='./fonts/DejaVuSansCondensed-Bold.ttf', uni=True)
        self.add_font('DejaVu', '', fname='./fonts/DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 18)
        self.cell(40, 0)
        self.cell(125, 10, f'Отчет по {self.data["gibdd"]["vehicle"]["model"].replace("БЕЗ МОДЕЛИ ", "")}', ln=1,
                  align='C', border=BORDER_LINE)
        self.cell(0, 10, f'VIN {self.data["report_id"]}', ln=1, align='C', border=BORDER_LINE)
        self.cell(0, 10, f'от {date.today()}', border=BORDER_LINE, ln=0, align='C')
        self.set_font('DejaVu', 'B', 15)
        self.ln(25)

    def general_info(self):
        # Заголовок блока
        self.cell(40, 0, 'Общие данные по автомобилю:', border=BORDER_LINE, ln=1)
        self.ln(15)
        self.set_font('DejaVu', '', 12)
        # 1я строка
        self.cell(100, 0, f'Модель: {self.data["gibdd"]["vehicle"]["model"].replace("БЕЗ МОДЕЛИ ", "")}', border=BORDER_LINE)
        self.cell(40, 0, f'Год выпуска: {self.data["gibdd"]["vehicle"]["year"]}', border=BORDER_LINE)
        self.ln(10)
        # 2я строка
        self.cell(100, 0, f'VIN: {self.data["report_id"]}', border=BORDER_LINE)
        self.cell(40, 0, f'Цвет: {self.data["gibdd"]["vehicle"]["color"]}', border=BORDER_LINE)
        self.ln(10)
        # 3я строка
        self.cell(100, 0, f'Номер кузова: {self.data["gibdd"]["vehicle"]["color"]}', border=BORDER_LINE)
        self.cell(40, 0, f'Объем двигателя: {self.data["gibdd"]["vehicle"]["engineVolume"]} см3', border=BORDER_LINE)
        self.ln(10)
        # 4я строка
        if self.data["gibdd"]["vehicle"]["engineNumber"] is None:
            self.cell(100, 0, 'Номер двигателя: Отсутствует', border=BORDER_LINE)
        else:
            self.cell(100, 0, f'Номер двигателя: {self.data["gibdd"]["vehicle"]["engineNumber"]}', border=BORDER_LINE)
        self.cell(40, 0, f'Мощность: {self.data["gibdd"]["vehicle"]["powerHp"]} лс / {self.data["gibdd"]["vehicle"]["powerKwt"]} '
                         f'кВт', border=BORDER_LINE)
        self.ln(10)
        # 5я строка
        self.cell(100, 0, f'Номер ПТС: {self.data["gibdd"]["vehiclePassport"]["number"]}', border=BORDER_LINE)
        self.cell(40, 0, f'Тип ТС: {self.data["gibdd"]["vehicle"]["typeinfo"]}', border=BORDER_LINE, ln=1)
        self.ln(10)
        self.set_font('DejaVu', 'B', 15)
        self.ln(25)

    def summary_brief(self):
        # Заголовок блока
        self.cell(40, 0, 'Краткая сводка:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 12)
        self.ln(10)

        # 1я строка

        if "count" in self.data["restrict"]:
            if self.data["restrict"]["count"] == 0:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Ограничения не найдены', border=BORDER_LINE, ln=0)

            else:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Есть ограничения на регистрацию', border=BORDER_LINE, ln=0)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Нет информации об ограничениях', border=BORDER_LINE, ln=0)

        self.image('./media/logo-info.png', x=self.get_x(), y=self.get_y(), w=5)
        self.cell(7, 5, border=BORDER_LINE, ln=0)
        self.cell(85, 5, f'Количество владельцев в ПТС: {len(self.data["gibdd"]["ownershipPeriod"])}', border=BORDER_LINE, ln=1)
        self.ln(5)

        # 2я строка

        if "count" in self.data["wanted"]:
            if self.data["wanted"]["count"] == 0:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Нет сведений о розыске', border=BORDER_LINE, ln=0)
            else:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Найдены сведения о розыске', border=BORDER_LINE, ln=0)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Нет информации о розыске', border=BORDER_LINE, ln=0)
        if "count" in self.data["osago"]:
            if self.data["osago"]["count"] == 0:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Полис ОСАГО не найден', border=BORDER_LINE, ln=1)
                self.ln(5)
            else:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Найден полис ОСАГО', border=BORDER_LINE, ln=1)
                self.ln(5)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Нет информации о страховке', border=BORDER_LINE, ln=1)
            self.ln(5)

        # 3я строка


        if "num" in self.data["notary"]:
            if self.data["notary"]["num"] == 0:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Не в залоге', border=BORDER_LINE, ln=0)
            else:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Найдены сведения о залоге', border=BORDER_LINE, ln=0)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Нет информации о залоге', border=BORDER_LINE, ln=0)

        if 'count' in self.data["company"]:
            self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Отзывные компании не найдены', border=BORDER_LINE, ln=1)
            self.ln(5)
        elif 'error' in self.data["company"]:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Нет сведений об отзывных компаниях', border=BORDER_LINE, ln=1)
            self.ln(5)
        else:
            self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Найдены отзывные компании', border=BORDER_LINE, ln=1)
            self.ln(5)

        # 4я строка

        if 'count' in self.data["dtp"]:
            if self.data["dtp"]["count"] == 0:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'ДТП не найдены', border=BORDER_LINE, ln=0)
            else:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Есть сведения о ДТП', border=BORDER_LINE, ln=0)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Нет сведений о ДТП', border=BORDER_LINE, ln=0)
        if len(self.data["taxi"]['records']) == 0:
            self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Не найдены сведения о работе в такси', border=BORDER_LINE, ln=1)
            self.ln(5)
        else:
            self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Есть информация о работе в такси', border=BORDER_LINE, ln=1)
            self.ln(5)


    def price_block(self):
        # Заголовок блока
        if self.data["price"] is not None and self.data["price"].get("cost", None):
            self.set_font('DejaVu', 'B', 15)
            self.cell(150, 15, f'Средняя рыночная стоимость ~ {self.data["price"]["cost"]} руб.', border=BORDER_LINE, ln=1)
            self.set_font('DejaVu', '', 13)
        if self.data["price"] is not None and self.data["price"].get("cost_trade_in", None):
            self.cell(150, 15, f'В Traid-In предложат ~ {self.data["price"]["cost_trade_in"]} руб.', border=BORDER_LINE, ln=0)
            self.ln(10)


    def owners_block(self):
        self.add_page()
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация о собственниках:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        self.image('./media/logo-info.png', x=self.get_x(), y=self.get_y(), w=5)
        self.cell(7, 5, border=BORDER_LINE, ln=0)
        self.cell(85, 5, f'Количество собственников в ПТС: {len(self.data["gibdd"]["ownershipPeriod"])}',
                  border=BORDER_LINE, ln=0)
        self.ln(20)
        for i in range(len(self.data["gibdd"]["ownershipPeriod"])):
            owner_info = self.data["gibdd"]["ownershipPeriod"][i]
            self.set_font('DejaVu', 'B', 14)
            self.cell(85, 10, f'{i + 1}й собственник: {owner_info["simplePersonTypeInfo"]}',
                      border=BORDER_LINE, ln=1)
            self.set_font('DejaVu', '', 13)
            if owner_info["to"] == 'null':
                self.cell(85, 10, f'Период владения: с {owner_info["from"]} по настоящее время', border=BORDER_LINE,
                          ln=1)
            else:
                self.cell(85, 10, f'Период владения: с {owner_info["from"]} по {owner_info["to"]}', border=BORDER_LINE,
                          ln=1)
            self.cell(85, 10, f'Срок владения: {owner_info["period"]}', border=BORDER_LINE, ln=1)
            self.ln(10)

    def restrictions_block(self):
        self.add_page()
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 20, 'Информация об ограничениях:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 14)
        if "count" in self.data["restrict"]:
            if self.data['restrict']['count'] != 0:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, f'Записей об ограничениях найдено: {data["restrict"]["count"]}:', border=BORDER_LINE, ln=0)
                self.ln(10)
                for restrict in self.data["restrict"]["records"]:
                    self.cell(85, 10, f'{restrict["num"]}я запись:', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Вид ограничения: {restrict["ogrkodinfo"]}', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Дата наложения ограничения: {restrict["dateogr"]}', border=BORDER_LINE, ln=1)

                    self.multi_cell(0, 8, f'{restrict["osnOgr"]}', 0, 'J')
                    self.cell(85, 10, f'Кем наложено: {restrict["divtypeinfo"]}', border=BORDER_LINE, ln=1)
            else:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 10, f'Записи об ограничениях не найдено', border=BORDER_LINE, ln=0)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Информация не получена', border=BORDER_LINE, ln=0)
        self.ln(10)

    def dtp_block(self):
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация о ДТП:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        if 'count' in self.data["dtp"]:
            if self.data['dtp']['count'] != 0:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, f'Найдено ДТП: {self.data["dtp"]["count"]}', border=BORDER_LINE, ln=0)
                self.ln(10)
                for dtp in self.data["dtp"]["records"]:
                    self.cell(85, 10, f'{dtp["num"]}я запись:', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Дата происшествия: {dtp["AccidentDateTime"]}', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Тип происшествия: {dtp["AccidentType"]}', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Место происшествия: {dtp["AccidentPlace"]}', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Повреждения по ссылке: {dtp["DamagePointsSVGdesc"]}', border=BORDER_LINE, ln=1)
                    self.ln(10)
                    # self.image('../media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                    # img_url = str(dtp["DamagePointsSVGdesc"])
                    # self.image(name=img_url,x=self.get_x(), y=self.get_y(), w=0, h=0, type='', link='')
                    # self.multi_cell(0, 8, f'{restrict["osnOgr"]}', 0, 'J')
                    # self.cell(85, 10, f'Кем наложено: {restrict["divtypeinfo"]}', border=BORDER_LINE, ln=1)
            else:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'ДТП не найдены', border=BORDER_LINE, ln=0)
                self.ln(10)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Информация не получена', border=BORDER_LINE, ln=0)
            self.ln(10)


    def notary(self):
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация о залоге:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        if "num" in self.data["notary"]:
            if self.data['notary']['num'] != 0:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, f'Найдено записей о залогах ДТП: {self.data["notary"]["num"]}', border=BORDER_LINE, ln=0)
                self.ln(10)
                for notary in data["notary"]["rez"]:
                    self.cell(85, 10, f'{self.data["notary"]["rez"].index(notary)}я запись:', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Дата регистрации : {notary["regDate"]}', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Залогодатель: {notary["pledgors"][0]["name"]}, {notary["pledgors"][0]["nameDetal"]}', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Залогодержатель: {notary["pledgees"][0]["name"]}', border=BORDER_LINE, ln=1)
                    self.ln(10)
            else:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Данные о залоге не найдены', border=BORDER_LINE, ln=0)
                self.ln(10)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Информация не получена', border=BORDER_LINE, ln=0)
            self.ln(10)

    def companies(self):
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация об отзывных компаниях:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        if 'count' in self.data["company"]:
            self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Данные об отзывных компаниях не найдены', border=BORDER_LINE, ln=0)
            self.ln(10)
        elif 'error' in self.data["company"]:
            self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Информация не получена', border=BORDER_LINE, ln=1)
            self.ln(10)
        else:
            self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, f'Найдена отзывная компания:', border=BORDER_LINE, ln=0)
            self.ln(10)
            self.cell(85, 10, f'Дата компании: {self.data["company"]["date"]}', border=BORDER_LINE, ln=1)
            self.multi_cell(0, 8, f'Организатор: {self.data["company"]["organizator"]}', 0, 'L')
            self.ln(1)
            self.multi_cell(0, 8, f'Причина: {self.data["company"]["reasons"]}', 0, 'L')
            self.ln(1)
            self.multi_cell(0, 8, f'Рекомендация: {self.data["company"]["recommendation"]}', 0, 'L')
            self.ln(10)



    def wanted(self):
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация о розыске:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        if "count" in self.data["wanted"]:
            if self.data['wanted']['count'] != 0:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, f'Найдено записей о розыске: {data["wanted"]["count"]}', border=BORDER_LINE, ln=0)
                self.ln(10)
                for wanted in self.data['wanted']["records"]:
                    self.cell(85, 10, f'{self.data["wanted"]["records"].index(wanted)}я запись:', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Регион инициатора розыска: {wanted["w_reg_inic"]}', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Дата постановки в розыск: {wanted["w_data_pu"]}', border=BORDER_LINE, ln=1)
                    self.cell(85, 10, f'Объект розыска: {wanted["w_model"]}, VIN {wanted["w_vin"]}', border=BORDER_LINE, ln=1)
                    self.ln(10)
            else:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Данные о розыске не найдены', border=BORDER_LINE, ln=0)
                self.ln(10)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Информация не получена', border=BORDER_LINE, ln=0)
            self.ln(10)

    def osago(self):
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация об ОСАГО:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        if "count" in self.data["osago"]:
            if self.data['osago']['count'] != 0:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, f'Найден страховой полис:', border=BORDER_LINE, ln=0)
                self.ln(10)
                self.cell(85, 10, f'Страхователь: {self.data["osago"]["rez"][0]["insured"]}', border=BORDER_LINE, ln=1)
                self.cell(85, 10, f'Страховщик: {self.data["osago"]["rez"][0]["orgosago"]}', border=BORDER_LINE, ln=1)
                self.cell(85, 10, f'Регион: {self.data["osago"]["rez"][0]["region"]}', border=BORDER_LINE, ln=1)
                self.cell(85, 10, f'Госномер: {self.data["osago"]["rez"][0]["regnum"]}', border=BORDER_LINE, ln=1)
                self.cell(85, 10, f'Статус страхового полиса: {self.data["osago"]["rez"][0]["term"]}', border=BORDER_LINE, ln=1)
                self.ln(10)
            else:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Данные о страховке не найдены', border=BORDER_LINE, ln=0)
                self.ln(10)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Информация не получена', border=BORDER_LINE, ln=0)
            self.ln(10)

    def eaisto(self):
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация об диагностических картах:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        if "count" in self.data["eaisto"]:
            if self.data['eaisto']['count'] != 0:
                self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, f'Найдены сведения о диагностической карте:', border=BORDER_LINE, ln=0)
                self.ln(10)
                self.multi_cell(0, 8, f'Адрес выдачи карты: {self.data["eaisto"]["records"][0]["pointAddress"]}', 0, 'L')
                self.cell(85, 10, f'Срок действия: {self.data["eaisto"]["records"][0]["dcExpirationDate"]}', border=BORDER_LINE, ln=1)
                self.cell(85, 10, f'Пробег: {self.data["eaisto"]["records"][0]["odometerValue"]}', border=BORDER_LINE, ln=1)
                self.ln(10)
            else:
                self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
                self.cell(7, 5, border=BORDER_LINE, ln=0)
                self.cell(85, 5, 'Данные о диагностических картах не найдены', border=BORDER_LINE, ln=0)
                self.ln(10)
        else:
            self.image('./media/logo-question.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Информация не получена', border=BORDER_LINE, ln=0)
            self.ln(10)

    def taxi(self):
        # Заголовок блока
        self.set_font('DejaVu', 'B', 15)
        self.cell(150, 15, 'Информация о работе в такси:', border=BORDER_LINE, ln=1)
        self.set_font('DejaVu', '', 13)
        if len(self.data['taxi']['records']) > 0:
            self.image('./media/logo-stop.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, f'Найдены сведения о работе в такси:', border=BORDER_LINE, ln=0)
            self.ln(10)
            for item in self.data['taxi']['records']:
                self.cell(85, 10, f'Номер разрешения: {item["permitNumber"]}', border=BORDER_LINE, ln=1)
                self.cell(85, 10, f'Дата выдачи разрешения: {item["dateFrom"]}', border=BORDER_LINE, ln=1)
                self.cell(85, 10, f'Дата окончания разрешения: {item["dateTo"]}', border=BORDER_LINE, ln=1)
                self.cell(85, 10, f'Регион: {item["regionName"]}', border=BORDER_LINE, ln=1)
                self.cell(85, 10, f'Статус: {item["isActual"]}', border=BORDER_LINE, ln=1)
                self.ln(10)
        else:
            self.image('./media/logo-ok.png', x=self.get_x(), y=self.get_y(), w=5)
            self.cell(7, 5, border=BORDER_LINE, ln=0)
            self.cell(85, 5, 'Данные о работе в такси не найдены', border=BORDER_LINE, ln=0)
            self.ln(10)



# pdf = CarReport()
