from .configuration import VERSION, AUTHOR
import datetime


info = """

<b>Добро пожаловать в приложение CheckMyVin !</b>

Данное приложение разработано для получения информации актуальных отчетов об автомобиле, штрафах, приблизительной оценке ТС

-<b>Версия программы: - </b><i>{}</i>
-<b>Разработчик: - </b><i>{}</i>

""".format(VERSION, AUTHOR)

car_report = """

<b>Отчет об авто {} {} от {}</b>

-<b>VIN: - </b><i>{}</i>
-<b>VIN: - </b><i>{}</i>

"""

settings = """

"""

MESSAGES = {
    'info': info,
    'settings': settings,
    'car_report': car_report
}
