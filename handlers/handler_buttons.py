from handlers.handler import Handler
from settings import configuration, messages
from settings.configuration import AUTHOR, VERSION
from services import api_request, errors_handlers, pdf_creator
from settings.messages import cash_message, operations_message
from pprint import pprint

class HandlerButtons(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_back(self, message):
        user = self.DB.choose_user(message)
        self.bot.send_message(message.chat.id, 'Вы вернулись назад',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.start_menu(user))
        self.DB.reset_user_data(message)

    # кнопки админки

    def pressed_btn_admin(self, message):
        self.bot.send_message(message.chat.id, 'Меню админ-панели',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.admin_menu_with_btn_back())

    def pressed_btn_cash(self, message):
        alert, answer = errors_handlers.cash(api_request.request_cash())
        if not alert:
            msg_to_user = cash_message(answer)
        else:
            msg_to_user = answer
        self.bot.send_message(message.chat.id, msg_to_user,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def pressed_btn_operations(self, message):
        alert, answer = errors_handlers.operations(api_request.request_operations())
        if not alert:
            msg_to_user = operations_message(answer)
        else:
            msg_to_user = answer
        self.bot.send_message(message.chat.id, msg_to_user,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    def pressed_btn_add_subscribe(self, message):
        self.bot.send_message(message.chat.id, 'Введите ник пользователя',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.set_user_state(message, configuration.STATES['ADD_SUBSCRIBE'])

    def pressed_btn_qt_users(self, message):
        users_count = self.DB.get_users_count()
        self.bot.send_message(message.chat.id, f'Всего сейчас {users_count} пользователей',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())

    # общие

    def pressed_btn_info(self, message):
        self.bot.send_message(message.chat.id, messages.info_message(VERSION, AUTHOR),
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.reset_user_data(message)

    def pressed_btn_report(self, message):
        self.bot.send_message(message.chat.id, 'Введите VIN автомобиля',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.set_user_state(message, configuration.STATES['GIBDD_SET_VIN'])

    def pressed_btn_photo(self, message):
        self.bot.send_message(message.chat.id, 'Введите номер автомобиля',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.set_user_state(message, configuration.STATES['PHOTO_SET_REGNUMBER'])

    def pressed_btn_fines(self, message):
        self.bot.send_message(message.chat.id, 'Введите номер автомобиля',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.set_user_state(message, configuration.STATES['FINES_SET_REGNUMBER'])

    def pressed_btn_price(self, message):
        self.bot.send_message(message.chat.id, 'Выберите марку автомобиля',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.keybord_inline(configuration.AUTOS))
        self.DB.set_user_state(message, configuration.STATES['PRICE_SET_MARKA'])

    def pressed_btn_fssp(self, message):
        self.bot.send_message(message.chat.id, 'Введите Фамилию Имя Отчество через пробел',
                              parse_mode='HTML',
                              reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.set_user_state(message, configuration.STATES['FSSP_FIO'])

    def get_report_fssp(self, callback_data):
        current_user = self.DB.choose_user(callback_data)
        alert, answer = errors_handlers.fssp(api_request.request_fssp(current_user.cache))
        if not alert:
            self.bot.send_message(callback_data.message.chat.id, messages.fssp_message(answer),
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())
        else:
            self.bot.send_message(callback_data.message.chat.id, answer,
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.reset_user_data(callback_data.message)

    def send_pdf_car_report(self, message):
        cache = self.DB.get_user_cache(message)
        pdf_creator.CarReport(cache)
        doc = open(f'./reports/{cache["report_id"]}.pdf', 'rb')
        self.bot.send_document(message.chat.id, doc, reply_markup=self.keyboards.menu_with_btn_back())
        # self.bot.send_message(message.chat.id, f'Готовится отчет',
        #                       parse_mode='HTML',
        #                       reply_markup=self.keyboards.menu_with_btn_back())
        self.DB.reset_user_data(message)


    def handle(self):
        @self.bot.message_handler(func=lambda message: message.text in configuration.KEYBOARD.values())
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
            if message.text == configuration.KEYBOARD['FSSP']:
                self.pressed_btn_fssp(message)
            if message.text == configuration.KEYBOARD['ADMIN']:
                self.pressed_btn_admin(message)
            if message.text == configuration.KEYBOARD['CASH']:
                self.pressed_btn_cash(message)
            if message.text == configuration.KEYBOARD['OPERATIONS']:
                self.pressed_btn_operations(message)
            if message.text == configuration.KEYBOARD['ADDSUBSCRIBE']:
                self.pressed_btn_add_subscribe(message)
            if message.text == configuration.KEYBOARD['QT_USERS']:
                self.pressed_btn_qt_users(message)
            if message.text == configuration.KEYBOARD['DOWNLOAD_PDF']:
                self.send_pdf_car_report(message)

            # работа с оценкой авто

        @self.bot.callback_query_handler(func=lambda callback_data: self.DB.get_user_state(
            callback_data) == configuration.STATES['PRICE_SET_MARKA'])
        def handle_inline(callback_data):
            alert, answer = errors_handlers.models(api_request.request_models(callback_data.data))
            if not alert:
                self.bot.send_message(callback_data.message.chat.id, 'Теперь выберите модель авто',
                                      parse_mode='HTML',
                                      reply_markup=self.keyboards.keybord_inline(answer))
                self.DB.set_user_state(callback_data, configuration.STATES['PRICE_SET_MODEL'])
                self.DB.set_user_cache(callback_data, {'marka': callback_data.data})
            else:
                self.bot.send_message(message.chat.id, answer,
                                      parse_mode='HTML',
                                      reply_markup=self.keyboards.menu_with_btn_back())

        @self.bot.callback_query_handler(func=lambda callback_data: self.DB.get_user_state(
            callback_data) == configuration.STATES['PRICE_SET_MODEL'])
        def handle_inline(callback_data):
            alert, answer = errors_handlers.years(
                api_request.request_year(self.DB.get_user_cache(callback_data)['marka'],
                                         callback_data.data))
            if not alert:
                self.bot.send_message(callback_data.message.chat.id, 'Укажите год авто',
                                      parse_mode='HTML',
                                      reply_markup=self.keyboards.keybord_inline(answer))
                self.DB.set_user_state(callback_data, configuration.STATES['PRICE_SET_YEAR'])
                self.DB.set_user_cache(callback_data, {
                    'marka': self.DB.get_user_cache(callback_data)['marka'],
                    'model': callback_data.data
                })
            else:
                self.bot.send_message(message.chat.id, answer,
                                      parse_mode='HTML',
                                      reply_markup=self.keyboards.menu_with_btn_back())

        @self.bot.callback_query_handler(func=lambda callback_data: self.DB.get_user_state(
            callback_data) == configuration.STATES['PRICE_SET_YEAR'])
        def handle_inline(callback_data):
            self.bot.send_message(callback_data.message.chat.id, 'Укажите пробег авто в км',
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())
            self.DB.set_user_state(callback_data, configuration.STATES['PRICE_SET_PROBEG'])
            self.DB.set_user_cache(callback_data, {
                'marka': self.DB.get_user_cache(callback_data)['marka'],
                'model': self.DB.get_user_cache(callback_data)['model'],
                'year': callback_data.data
            })

            # работа с фссп

        @self.bot.callback_query_handler(func=lambda callback_data: self.DB.get_user_state(
            callback_data) == configuration.STATES['FSSP_REGION_NAME'])
        def handle_inline(callback_data):
            self.DB.set_user_cache(callback_data, {
                'lastname': self.DB.get_user_cache(callback_data)['lastname'],
                'firstname': self.DB.get_user_cache(callback_data)['firstname'],
                'secondname': self.DB.get_user_cache(callback_data)['secondname'],
                'region': callback_data.data
            })
            self.get_report_fssp(callback_data)

            # работа с добавкой подписки

        @self.bot.callback_query_handler(func=lambda callback_data: self.DB.get_user_state(
            callback_data) == configuration.STATES['QT_SUBSCRIBES'])
        def handle_inline(callback_data):
            cache = self.DB.get_user_cache(callback_data)
            self.DB.add_subscribe_for_user(cache.get('subscribe_for_user'), int(callback_data.data))
            self.bot.send_message(callback_data.message.chat.id, f'Добавлено {callback_data.data} подписок пользователю {cache.get("subscribe_for_user")}',
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.menu_with_btn_back())



