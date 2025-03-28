import telebot
import os
from flask import Flask, request

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("7744399423:AAHZTEV38xGvJrUrEzunmmolp9Sz-S1Rllo")  
if not TOKEN:
    raise ValueError("❌ TOKEN is missing! Set it as an environment variable.")

bot = telebot.TeleBot(TOKEN)

# مقدار درست برای Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ Bot is Running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def getMessage():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "✅ OK", 200

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "سلام! من ربات تلگرام هستم. چطور کمکتان کنم؟")

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=PORT)
