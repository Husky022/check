from handlers.handler import Handler
from settings import configuration
from services import api_request


class HandlerText(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def get_photos_report(self, message):
        for el in api_request.request_photo(message.text):
            self.bot.send_message(message.chat.id, el, parse_mode='HTML')


    def get_gibdd_report(self, vin):
        api_request.request_gibdd(vin)


    def get_fines_report(self, regnum, sts):
        api_request.request_fines(regnum, sts)


    def get_price(self, message, cache, probeg):
        price = api_request.request_price(cache, probeg)
        self.bot.send_message(message.chat.id, f'Ориентировочная рыночная стоимость составляет {price["cost"]} руб. ' +
                              f'Если рассматривать Traid In, то {price["cost_trade_in"]} руб.',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())



    def handle(self):
        print('handle_text_start')

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['PHOTO_SET_REGNUMBER'])
        def entering_number_photo(message):
            print('handle_text')
            print('entering_regnumber_for_photo')
            self.get_photos_report(message)
            self.DB.reset_user_data(message.from_user.id)

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['GIBDD_SET_VIN'])
        def entering_vin_gibdd(message):
            print('handle_text')
            print('entering_vin_gibdd')
            self.get_gibdd_report(message.text)

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['FINES_SET_REGNUMBER'])
        def entering_regnum_fines(message):
            print('handle_text')
            print('entering_regnum_fines')
            self.DB.set_user_state(message.from_user.id, configuration.STATES['FINES_SET_STSNUMBER'])
            self.DB.set_user_cache(message.from_user.id, {'regnum': message.text})
            self.bot.send_message(message.chat.id, 'Теперь введите номер свидетельства ТС',
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['FINES_SET_STSNUMBER'])
        def entering_sts_fines(message):
            print('handle_text')
            print('entering_sts_fines')
            current_user = self.DB.choose_user(message.from_user.id)
            self.get_fines_report(current_user.cache['regnum'], message.text)
        #
        # @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
        #     message.from_user.id) == configuration.STATES['GIBDD_SET_REGNUMBER'])
        # def entering_number_gibdd(message):
        #     print('handle_text')
        #     print('entering_number_gibdd')
        #     current_user = self.DB.choose_user(message.from_user.id)
        #     self.get_gibdd_report(message.text, current_user.cache['vin'])

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['PRICE_SET_PROBEG'])
        def entering_probeg_checkprice(message):
            print('handle_text')
            print('entering_sts_fines')
            current_user = self.DB.choose_user(message.from_user.id)
            self.get_price(message, current_user.cache, message.text)
