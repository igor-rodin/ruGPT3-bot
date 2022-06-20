import telebot

if __name__ == '__main__':
    telebot.bot.infinity_polling(skip_pending=True)
