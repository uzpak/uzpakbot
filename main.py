import telebot

BOT_TOKEN = "8104722787:AAENmV_tuRdjEGVrmvqSrQBcV6iB1LxHgW4"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ассалому алайкум! Бу UzPak бот. Бу ерда буюртма беришингиз мумкин.")

bot.polling()
