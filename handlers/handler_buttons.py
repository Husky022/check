from handlers.handler import Handler
from settings import configuration
from settings.messages import MESSAGES
from services import api_request


class HandlerButtons(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_back(self, message):
        self.bot.send_message(message.chat.id, 'Вы вернулись назад',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.start_menu())
        self.DB.reset_user_data(message.from_user.id)


    def pressed_btn_info(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['info'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def pressed_btn_report(self, message):
        self.bot.send_message(message.chat.id, 'Введите VIN автомобиля',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.set_user_state(message.from_user.id, configuration.STATES['GIBDD_SET_VIN'])

    def pressed_btn_photo(self, message):
        self.bot.send_message(message.chat.id, 'Введите номер автомобиля',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.set_user_state(message.from_user.id, configuration.STATES['PHOTO_SET_REGNUMBER'])

    def pressed_btn_fines(self, message):
        self.bot.send_message(message.chat.id, 'Введите номер автомобиля',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.set_user_state(message.from_user.id, configuration.STATES['FINES_SET_REGNUMBER'])

    def pressed_btn_price(self, message):
        self.bot.send_message(message.chat.id, 'test',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.set_user_state(message.from_user.id, configuration.STATES['PRICE_SET_MARKA'])

    def pressed_btn_fssp(self, message):
        self.bot.send_message(message.chat.id, 'Выберите нужный пункт',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_fssp())

    def pressed_btn_fiz(self, message):
        pass

    def pressed_btn_yur(self, message):
        pass

    def pressed_btn_id(self, message):
        pass


    def handle(self):
        print('handle_buttons_start')

        @self.bot.message_handler(func=lambda message: message.text in configuration.KEYBOARD.values())
        def handle(message):
            print('handle_buttons')
            if message.text == configuration.KEYBOARD['<<']:
                self.pressed_btn_back(message)
            if message.text == configuration.KEYBOARD['INFO']:
                self.pressed_btn_info(message)
            if message.text == configuration.KEYBOARD['CAR_REPORT']:
                self.pressed_btn_report(message)
            if message.text == configuration.KEYBOARD['CAR_PHOTO']:
                self.pressed_btn_photo(message)
            if message.text == configuration.KEYBOARD['FINES']:
                self.pressed_btn_fines(message)
            if message.text == configuration.KEYBOARD['PRICE']:
                self.pressed_btn_price(message)
            if message.text == configuration.KEYBOARD['FSSP']:
                self.pressed_btn_fssp(message)
            if message.text == configuration.KEYBOARD['FIZ']:
                self.pressed_btn_fiz(message)
            if message.text == configuration.KEYBOARD['YUR']:
                self.pressed_btn_yur(message)
            if message.text == configuration.KEYBOARD['ID']:
                self.pressed_btn_id(message)
