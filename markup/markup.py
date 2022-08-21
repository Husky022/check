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

    def start_menu(self, user):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_button('CAR_REPORT')
        itm_btn_2 = self.set_button('CAR_PHOTO')
        itm_btn_3 = self.set_button('PRICE')
        itm_btn_4 = self.set_button('FINES')
        itm_btn_5 = self.set_button('FSSP')
        itm_btn_6 = self.set_button('INFO')
        self.markup.row(itm_btn_1, itm_btn_2)
        self.markup.row(itm_btn_3, itm_btn_4)
        if user.is_admin:
            itm_btn_7 = self.set_button('ADMIN')
            self.markup.row(itm_btn_5, itm_btn_7, itm_btn_6)
        else:
            self.markup.row(itm_btn_5, itm_btn_6)
        return self.markup

    def admin_menu_with_btn_back(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_button('CASH')
        itm_btn_2 = self.set_button('OPERATIONS')
        itm_btn_3 = self.set_button('QT_USERS')
        itm_btn_4 = self.set_button('ADDSUBSCRIBE')
        itm_btn_5 = self.set_button('<<')
        self.markup.row(itm_btn_1, itm_btn_2)
        self.markup.row(itm_btn_3, itm_btn_4)
        self.markup.row(itm_btn_5)
        return self.markup

    def menu_with_btn_back(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_button('<<')
        self.markup.row(itm_btn_1)
        return self.markup

    def save_report_with_btn_back(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_button('<<')
        itm_btn_2 = self.set_button('DOWNLOAD_PDF')
        self.markup.row(itm_btn_1, itm_btn_2)
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

    def keybord_inline(self, current_list):
        self.markup = Keyboa(items=current_list, copy_text_to_callback=True,
                             items_in_row=4).keyboard
        return self.markup
