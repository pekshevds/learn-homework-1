"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from local_settings import telegram_bot_token


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def show_planet_info(update, context):
    
    update.message.reply_text("input a value of [mars, moon, mercury, jupiter, venus, saturn, sun]")


def talk_to_me(update, context):
    user_text = update.message.text


    if user_text.lower() == 'mars':
        planet = ephem.Mars()
    elif user_text.lower() == 'moon':
        planet = ephem.Moon()
    elif user_text.lower() == 'mercury':
        planet = ephem.Mercury()
    elif user_text.lower() == 'jupiter':
        planet = ephem.Jupiter()
    elif user_text.lower() == 'venus':
        planet = ephem.Venus()
    elif user_text.lower() == 'saturn':
        planet = ephem.Saturn()
    elif user_text.lower() == 'sun':
        planet = ephem.Sun()
    else:
        update.message.reply_text('unknown planet')
        return

    planet.compute(date.today())
    update.message.reply_text(str(ephem.constellation(planet)[1]))


def main():
    #mybot = Updater(telegram_bot_token, request_kwargs=PROXY, use_context=True)
    mybot = Updater(telegram_bot_token, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", show_planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

