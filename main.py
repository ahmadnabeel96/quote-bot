import os
import time
import threading
from datetime import datetime
import pytz
from telegram import Bot
from flask import Flask

# 🔐 البيانات (من Variables)
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME")

bot = Bot(token=TOKEN)

# 🌐 Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive 🚀"

# 🇯🇴 توقيت الأردن
tz = pytz.timezone("Asia/Amman")

# 💬 عبارات
quotes = [
    "✨ لا تيأس فالله معك دائمًا ❤️",
    "🌙 اذكر الله يطمئن قلبك 🤍",
    "🤍 كن قريبًا من الله تجد السلام 🌿",
    "💫 لا تحزن إن الله معنا ✨",
    "🌿 توكّل على الله فهو حسبك ❤️"
]

# ⏰ جدول النشر (نفس القديم)
schedule = [
    (9, 0),
    (12, 0),
    (15, 0),
    (18, 0),
    (21, 0),
    (0, 0)
]

last_post = None
index = 0

# 🤖 البوت
def run_bot():
    global last_post, index

    print("🚀 BOT LOOP STARTED")

    while True:
        try:
            now = datetime.now(tz)

            for h, m in schedule:
                if now.hour == h and now.minute == m:
                    key = f"{h}:{m}"

                    if last_post != key:

                        if index < 5:
                            text = quotes[index]
                        else:
                            text = f"""✨ اقتباسات يومية

{quotes[index % len(quotes)]}

📌 https://t.me/{CHANNEL.replace('@','')}"""

                        bot.send_message(chat_id=CHANNEL, text=text)

                        print("✅ Sent:", text)

                        index = (index + 1) % 6
                        last_post = key

            time.sleep(30)

        except Exception as e:
            print("❌ ERROR:", e)
            time.sleep(10)

# 🔥 keep alive (مهم جدًا)
def keep_alive():
    while True:
        print("💡 still alive...")
        time.sleep(300)

# 🚀 تشغيل
threading.Thread(target=run_bot).start()
threading.Thread(target=keep_alive).start()

# 🌐 تشغيل السيرفر
port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
