import telebot
import os
import schedule
import time
import threading

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(TOKEN)

horoscopes = {
    "Овен": "Сегодня день для новых начинаний.",
    "Телец": "Будьте внимательнее к деталям.",
    "Близнецы": "Ожидается много общения.",
    "Рак": "Сконцентрируйтесь на семье.",
    "Лев": "Ваше лидерство заметят.",
    "Дева": "День для порядка и анализа.",
    "Весы": "Ищите баланс во всём.",
    "Скорпион": "Интуиция поможет принять решение.",
    "Стрелец": "Хорошо для путешествий и идей.",
    "Козерог": "Работа принесёт плоды.",
    "Водолей": "Неожиданная новость порадует.",
    "Рыбы": "Слушайте свою интуицию."
}

def send_horoscopes():
    for sign, text in horoscopes.items():
        message = f"♈ {sign}\n{text}"
        bot.send_message(CHANNEL_ID, message)

def scheduler():
    schedule.every().day.at("08:00").do(send_horoscopes)
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=scheduler).start()

bot.infinity_polling()
