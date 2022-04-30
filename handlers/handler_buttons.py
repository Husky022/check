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

    def pressed_btn_info(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['info'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.info_menu())

    def pressed_btn_report(self, message):
        self.bot.send_message(message.chat.id, 'test',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.photo_menu())

    def pressed_btn_photo(self, message):
        self.bot.send_message(message.chat.id, 'Введите номер автомобиля',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.photo_menu())
        self.DB.set_user_state(message.from_user.id, configuration.STATES['PHOTO_SET_REGNUMBER'])

    def pressed_btn_fines(self, message):
        self.bot.send_message(message.chat.id, 'test',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.photo_menu())

    def pressed_btn_price(self, message):
        self.bot.send_message(message.chat.id, 'test',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.photo_menu())

    def handle(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
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

