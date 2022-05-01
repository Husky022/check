from handlers.handler import Handler
from settings import configuration
from services import api_request


class HandlerText(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def get_photos_report(self, message):
        for el in api_request.request_photo(message.text):
            self.bot.send_message(message.chat.id, el, parse_mode='HTML')

    def handle(self):
        print('handle_text_start')
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            print('handle_text')
            if self.DB.get_user_state(message.from_user.id) == configuration.STATES['PHOTO_SET_REGNUMBER']:
                print('entering_regnumber_for_photo')
                self.get_photos_report(message)

