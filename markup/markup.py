from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from settings import configuration
from database.dbalchemy import DBManager


class Keyboards:
    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    def set_button(self, name):
        return KeyboardButton(configuration.KEYBOARD[name])

    def start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_button('CAR_REPORT')
        itm_btn_2 = self.set_button('CAR_PHOTO')
        itm_btn_3 = self.set_button('PRICE')
        itm_btn_4 = self.set_button('FINES')
        itm_btn_5 = self.set_button('SETTINGS')
        itm_btn_6 = self.set_button('INFO')
        self.markup.row(itm_btn_1, itm_btn_2)
        self.markup.row(itm_btn_3, itm_btn_4)
        self.markup.row(itm_btn_5, itm_btn_6)
        return self.markup

    def info_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_button('<<')
        self.markup.row(itm_btn_1)
        return self.markup

    def photo_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_button('<<')
        self.markup.row(itm_btn_1)
        return self.markup


