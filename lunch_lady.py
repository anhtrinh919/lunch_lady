import os
import telebot

def send_reminder():
    bot = telebot.TeleBot(TOKEN)
    bot.send_message(CHAT_ID, MESSAGE)
    bot.stop_polling()

if __name__ == "__main__":
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    # Example message — change as needed
    MESSAGE = "🍱 Ăn thôi anh em ơi!"
    
    if not TOKEN or not CHAT_ID:
        raise RuntimeError("Missing TELEGRAM_TOKEN or TELEGRAM_CHAT_ID env vars")
    
    send_reminder()
