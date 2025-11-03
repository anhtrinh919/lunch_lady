import telebot, schedule, time, threading

TOKEN = "8394605809:AAFYG4mYGamrfU3y7TsMchP5p9pQIzQA7-s"
CHAT_ID = -232384245 # replace with your group ID
bot = telebot.TeleBot(TOKEN)

def send_reminder():
    bot.send_message(CHAT_ID, "Daily reminder message")

schedule.every().day.at("12:00").do(send_reminder)

def loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=loop).start()
bot.polling()
