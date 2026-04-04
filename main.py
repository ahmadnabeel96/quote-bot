import os
import time
import openai
from telegram import Bot
from flask import Flask
import threading

# ===== Web Server =====
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_web():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_web).start()

# ===== Config =====
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

# ===== Generate =====
def generate_post():
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "اكتب اقتباس قصير جميل مع ايموجي ✨"}],
    )
    return response.choices[0].message.content

# ===== Send =====
def send_post():
    text = generate_post()
    bot.send_message(chat_id=CHANNEL_ID, text=text)
    print("✅ Posted:", text)

# ===== Test Run =====
print("🚀 البوت رح ينشر بعد دقيقة...")

time.sleep(60)

send_post()

# خليه شغال
while True:
    print("⏳ waiting...")
    time.sleep(30)
