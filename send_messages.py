from cmv_bot import CMVBot



bot = CMVBot()
bot.run()

bot.send_message('', '')

# id чата Эли
self.bot.send_message('248147912', 'Это просто тест',
                      parse_mode='HTML',
                      reply_markup=self.keyboards.start_menu(user))