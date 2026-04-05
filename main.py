import os
import time
from datetime import datetime
import pytz
from telegram import Bot

# 🔐 بيانات من Railway
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME")

bot = Bot(token=TOKEN)

# 🇯🇴 توقيت الأردن
tz = pytz.timezone("Asia/Amman")

# 💬 العبارات
quotes = [
    "✨ لا تيأس فالله معك دائمًا ❤️",
    "🌙 اذكر الله يطمئن قلبك 🤍",
    "🤍 كن قريبًا من الله تجد السلام 🌿",
    "💫 لا تحزن إن الله معنا ✨",
    "🌿 توكّل على الله فهو حسبك ❤️"
]

# ⏰ أوقات النشر
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

print("🚀 BOT STARTED 24/7")

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
