import telebot

from settings import configuration

from handlers.handler_main import HandlerMain


class CMVBot:

    __version__ = configuration.VERSION
    __author__ = configuration.AUTHOR

    def __init__(self):
        self.token = configuration.TOKEN
        self.bot = telebot.TeleBot(self.token)
        self.handler = HandlerMain(self.bot)

    def run(self):
        self.handler.handle()
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = CMVBot()
    bot.run()


