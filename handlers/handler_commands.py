from handlers.handler import Handler


class HandlerCommands(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        user = self.DB.choose_user(message)
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' приветствую! Что пожелаете?',
                              reply_markup=self.keyboards.start_menu(user))
        print(message.from_user)

    def handle(self):
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                self.pressed_btn_start(message)
            else:
                self.bot.send_message(message.chat.id, 'Укажите команду из доступных действий')
            self.DB.choose_user(message)

        @self.bot.message_handler(commands=['bro'])
        def handle(message):
            self.bot.send_message(message.chat.id, 'Я в порядке!')
