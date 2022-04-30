from handlers.handler import Handler


class HandlerCommands(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' приветствую! Что пожелаете?',
                              reply_markup=self.keyboards.start_menu())

    def handle(self):
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            print(message)
            if message.text == '/start':
                self.pressed_btn_start(message)
            else:
                self.bot.send_message(message.chat.id, 'Укажите команду из доступных действий')
            self.DB.add_new_user(message.from_user.id, message.from_user.first_name)
