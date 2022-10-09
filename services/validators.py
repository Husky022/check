import re


def reg_numder(string):
    return True if re.fullmatch(r'[аАвВеЕкКмМнНоОрРсСтТуУхХ]\d{3}[аАвВеЕкКмМнНоОрРсСтТуУхХ]{2}[017]?\d{1,2}',
                                string) else False


def sts_number(string):
    return True if re.fullmatch(r'\d{2}[0-9а-яА-Я]{2}\d{6}', string) else False


def mileage(string):
    return True if re.fullmatch(r'\d*', string) else False


def vin(string):
    return True if re.fullmatch(r'[0-9a-hA-Hj-nJ-Np-zP-Z]{17}', string) else False


def fio(string):
    return True if re.fullmatch(r'[а-яА-ЯёЁ]{2,}[ ]([а-яА-ЯёЁ ]{3,})+', string) else False

