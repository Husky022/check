from .configuration import VERSION, AUTHOR


info = """

<b>Добро пожаловать в приложение CheckMyVin !</b>

Данное приложение разработано для получения информации актуальных отчетов об автомобиле, штрафах, приблизительной оценке ТС

-<b>Версия программы: - </b><i>{}</i>
-<b>Разработчик: - </b><i>{}</i>

""".format(VERSION, AUTHOR)

settings = """

"""

MESSAGES = {
    'info': info,
    'settings': settings
}
