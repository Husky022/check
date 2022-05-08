from handlers.handler import Handler
from settings import configuration
from services import api_request


class HandlerText(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def get_photos_report(self, message):
        for el in api_request.request_photo(message.text):
            self.bot.send_message(message.chat.id, el, parse_mode='HTML')


    def get_gibdd_report(self, message):
        self.bot.send_message(message.chat.id, api_request.request_gibdd(message.text),
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())


    def get_fines_report(self, regnum, sts):
        api_request.request_fines(regnum, sts)


    def get_price(self, message, cache, probeg):
        price = api_request.request_price(cache, probeg)
        self.bot.send_message(message.chat.id, f'Ориентировочная рыночная стоимость составляет {price["cost"]} руб. ' +
                              f'Если рассматривать Traid In, то {price["cost_trade_in"]} руб.',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())


    # работа с фото

    def handle(self):
        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['PHOTO_SET_REGNUMBER'])
        def entering_number_photo(message):
            self.get_photos_report(message)
            self.DB.reset_user_data(message.from_user.id)

        # работа с отчетом по vin

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['GIBDD_SET_VIN'])
        def entering_vin_gibdd(message):
            self.get_gibdd_report(message)

        # работа со штрафами

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['FINES_SET_REGNUMBER'])
        def entering_regnum_fines(message):
            self.DB.set_user_state(message.from_user.id, configuration.STATES['FINES_SET_STSNUMBER'])
            self.DB.set_user_cache(message.from_user.id, {'regnum': message.text})
            self.bot.send_message(message.chat.id, 'Теперь введите номер свидетельства ТС',
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['FINES_SET_STSNUMBER'])
        def entering_sts_fines(message):
            current_user = self.DB.choose_user(message.from_user.id)
            self.get_fines_report(current_user.cache['regnum'], message.text)

        # работа с оценкой

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['PRICE_SET_PROBEG'])
        def entering_probeg_checkprice(message):
            current_user = self.DB.choose_user(message.from_user.id)
            self.get_price(message, current_user.cache, message.text)

        # работа с фссп

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['FSSP_FIZ_L_NAME'])
        def entering_lastname_fssp(message):
            self.DB.set_user_state(message.from_user.id, configuration.STATES['FSSP_FIZ_F_NAME'])
            self.DB.set_user_cache(message.from_user.id, {'lastname': message.text})
            self.bot.send_message(message.chat.id, 'Введите имя',
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['FSSP_FIZ_F_NAME'])
        def entering_firstname_fssp(message):
            self.DB.set_user_state(message.from_user.id, configuration.STATES['FSSP_FIZ_REGION_NAME'])
            self.DB.set_user_cache(message.from_user.id,
                                   {
                                       'lastname': self.DB.get_user_cache(message.from_user.id)['lastname'],
                                       'firstname': message.text
                                   })
            self.bot.send_message(message.chat.id, 'Выберите регион поиска',
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.keybord_inline(list(api_request.request_regions(
                                  ).keys())))

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['FSSP_YUR_NAME'])
        def entering_yurname_fssp(message):
            self.DB.set_user_state(message.from_user.id, configuration.STATES['FSSP_YUR_REGION_NAME'])
            self.DB.set_user_cache(message.from_user.id, {'yurname': message.text})
            self.bot.send_message(message.chat.id, 'Выберите регион поиска',
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.keybord_inline(list(api_request.request_regions(
                                  ).keys())))

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message.from_user.id) == configuration.STATES['FSSP_ID'])
        def entering_id_fssp(message):
            current_user = self.DB.choose_user(message.from_user.id)
            api_request.request_fssp_id(current_user.cache)

