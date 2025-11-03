import os
import telebot
import schedule
import time
import threading

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TOKEN)

def send_reminder():
    bot.send_message(CHAT_ID, "🍱 Lunch reminder: don't forget to eat!")

schedule.every().day.at("05:00").do(send_reminder)  # 05:00 UTC = 12:00 Vietnam

def loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=loop, daemon=True).start()
bot.polling(none_stop=True)
