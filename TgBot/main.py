import telebot
import subprocess
import json
import time
import threading

TOKEN = '7970731723:AAE9t3XsfLKTFRpW9LYvirOQ91RWgh7Aug0'
bot = telebot.TeleBot(TOKEN)

CHAT_ID = None
notified = False

def get_battery():
    result = subprocess.check_output(["termux-battery-status"])
    data = json.loads(result)
    return data['percentage']

@bot.message_handler(commands=['start'])
def start(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    battery = get_battery()
    bot.send_message(CHAT_ID, f'Привет! \nТекущий заряд батареи: {battery}%')

def battery_watcher():
    global notified
    while True:
        if CHAT_ID is not None:
            battery = get_battery()
            if battery <= 30 and not notified:
                bot.send_message(CHAT_ID, f'Внимание! \nЗаряд батареи: {battery}%')
                notified = True
            if battery > 30:
                notified = False
        time.sleep(60)

threading.Thread(target=battery_watcher, daemon=True).start()

bot.polling()