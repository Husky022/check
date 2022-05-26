from handlers.handler import Handler
from settings import configuration
from services import api_request, validators, errors_handlers
from settings.messages import car_report_message, fines_message, fssp_message


class HandlerText(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def incorrect_input_regnumber(self, message):
        self.bot.send_message(message.chat.id, 'Введите корректный номер авто формата Х777ХХ197. Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def incorrect_input_stsnumber(self, message):
        self.bot.send_message(message.chat.id, 'Введите корректный номер CTC. Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def incorrect_input_mileage(self, message):
        self.bot.send_message(message.chat.id, 'Введите корректное значение пробега. Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def incorrect_input_vin(self, message):
        self.bot.send_message(message.chat.id, 'Введите корректный VIN (17 знаков). Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def incorrect_input_fio(self, message):
        self.bot.send_message(message.chat.id, 'Введите корректные данные!. Повторите ввод',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def get_photos_report(self, message):
        alert, answer = errors_handlers.photos(api_request.request_photo(message.text))
        if not alert:
            for el in answer:
                self.bot.send_message(message.chat.id, el, parse_mode='HTML')
        else:
            self.bot.send_message(message.chat.id, answer,
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())

    def get_gibdd_report(self, message):
        alert, answer = errors_handlers.gibdd(api_request.request_gibdd(message.text))
        if not alert:
            msg_to_user = car_report_message(answer)
        else:
            msg_to_user = answer
        self.bot.send_message(message.chat.id, msg_to_user,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def get_fines_report(self, message, regnum):
        alert, answer = errors_handlers.fines(api_request.request_fines(regnum, message.text))
        if not alert:
            msg_to_user = fines_message(answer)
        else:
            msg_to_user = answer
        self.bot.send_message(message.chat.id, msg_to_user,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def get_price(self, message, cache, probeg):
        alert, answer = errors_handlers.car_price(api_request.request_price(cache, probeg))
        if not alert:
            msg_to_user = f"Ориентировочная рыночная стоимость составляет {answer['cost']} руб.\n " \
                          f"Если рассматривать Traid In, то {answer['cost_trade_in']} руб."
        else:
            msg_to_user = answer
        self.bot.send_message(message.chat.id, msg_to_user,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    # работа с фото

    def handle(self):
        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['PHOTO_SET_REGNUMBER'])
        def entering_number_photo(message):
            if validators.reg_numder(message.text):
                self.get_photos_report(message)
                self.DB.reset_user_data(message)
            else:
                self.incorrect_input_regnumber(message)

        # работа с отчетом по vin

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['GIBDD_SET_VIN'])
        def entering_vin_gibdd(message):
            if validators.vin(message.text):
                self.get_gibdd_report(message)
                self.DB.reset_user_data(message)
            else:
                self.incorrect_input_vin(message)

        # работа со штрафами

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['FINES_SET_REGNUMBER'])
        def entering_regnum_fines(message):
            if validators.reg_numder(message.text):
                self.DB.set_user_state(message, configuration.STATES['FINES_SET_STSNUMBER'])
                self.DB.set_user_cache(message, {'regnum': message.text})
                self.bot.send_message(message.chat.id, 'Теперь введите номер свидетельства ТС',
                                      parse_mode='HTML',
                                      reply_markup=self.keyboards.menu_with_btn_back())
            else:
                self.incorrect_input_regnumber(message)

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['FINES_SET_STSNUMBER'])
        def entering_sts_fines(message):
            if validators.sts_number(message.text):
                current_user = self.DB.choose_user(message)
                self.get_fines_report(message, current_user.cache['regnum'])
                self.DB.reset_user_data(message)
            else:
                self.incorrect_input_stsnumber(message)

        # работа с оценкой

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['PRICE_SET_PROBEG'])
        def entering_probeg_checkprice(message):
            if validators.mileage(message.text):
                current_user = self.DB.choose_user(message)
                self.get_price(message, current_user.cache, message.text)
                self.DB.reset_user_data(message)
            else:
                self.incorrect_input_mileage(message)

        # работа с фссп

        @self.bot.message_handler(func=lambda message: self.DB.get_user_state(
            message) == configuration.STATES['FSSP_FIO'])
        def entering_fio_fssp(message):
            alert, answer = errors_handlers.regions(api_request.request_regions())
            if not alert:
                if validators.fio(message.text):
                    self.DB.set_user_state(message, configuration.STATES['FSSP_REGION_NAME'])
                    user_data = message.text.split()
                    if len(user_data) == 3:
                        self.DB.set_user_cache(message,
                                               {
                                                   'lastname': message.text.split()[0],
                                                   'firstname': message.text.split()[1],
                                                   'secondname': message.text.split()[2]
                                               })
                    elif len(user_data) == 2:
                        self.DB.set_user_cache(message,
                                               {
                                                   'lastname': message.text.split()[0],
                                                   'firstname': message.text.split()[1],
                                                   'secondname': None
                                               })
                    self.bot.send_message(message.chat.id, 'Выберите регион поиска',
                                          parse_mode='HTML',
                                          reply_markup=self.keyboards.keybord_inline(list(answer)))
                else:
                    self.incorrect_input_fio(message)
            else:
                self.bot.send_message(message.chat.id, answer,
                                      parse_mode='HTML',
                                      reply_markup=self.keyboards.menu_with_btn_back())
