from handlers.handler_commands import HandlerCommands
from handlers.handler_buttons import HandlerButtons
from handlers.handler_text import HandlerText


class HandlerMain:

    def __init__(self, bot):
        self.bot = bot
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_buttons = HandlerButtons(self.bot)
        self.handler_text = HandlerText(self.bot)

    def handle(self):
        self.handler_commands.handle()
        self.handler_buttons.handle()
        self.handler_text.handle()
        print('bot started')


