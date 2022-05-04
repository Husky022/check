from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from settings import configuration
from database.dbalchemy import DBManager
from keyboa import Keyboa


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
        itm_btn_5 = self.set_button('FSSP')
        itm_btn_6 = self.set_button('INFO')
        self.markup.row(itm_btn_1, itm_btn_2)
        self.markup.row(itm_btn_3, itm_btn_4)
        self.markup.row(itm_btn_5, itm_btn_6)
        return self.markup

    def menu_with_btn_back(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_button('<<')
        self.markup.row(itm_btn_1)
        return self.markup

    def menu_fssp(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_button('FIZ')
        itm_btn_2 = self.set_button('YUR')
        itm_btn_3 = self.set_button('ID')
        itm_btn_4 = self.set_button('<<')
        self.markup.row(itm_btn_1, itm_btn_2)
        self.markup.row(itm_btn_3, itm_btn_4)
        return self.markup

    def menu_autos(self, autos_list):
        self.markup = Keyboa(items=autos_list, copy_text_to_callback=True,
                             items_in_row=4).keyboard
        return self.markup
