import os
import time
from datetime import datetime
from telegram import Bot
import pytz

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME")

bot = Bot(token=TOKEN)

# 🇯🇴 توقيت الأردن
timezone = pytz.timezone("Asia/Amman")

quotes = [
    "✨ لا تيأس فالله معك دائمًا ❤️",
    "🌙 اذكرِ الله يطمئنُ قلبك 🤍",
    "🤍 كن قريبًا من الله تجد السلام 🌿",
    "💫 لا تحزن إن الله معنا ✨",
    "🌿 توكّل على الله فهو حسبك ❤️"
]

post_count = 0
last_minute = None

while True:
    now = datetime.now(timezone)

    # ⏰ التوقيتات (عدّلها إذا بدك)
    schedule = [
        (9, 0),
        (12, 0),
        (15, 0),
        (18, 0),
        (21, 0),
        (0, 0)
    ]

    for hour, minute in schedule:
        if now.hour == hour and now.minute == minute:
            if last_minute != now.minute:

                # 📌 أول 5 منشورات = عبارات
                if post_count < 5:
                    text = quotes[post_count % len(quotes)]

                # 🔥 المنشور السادس = مع رابط
                else:
                    text = f"""✨ اقتباسات يومية 🤍

{quotes[post_count % len(quotes)]}

📌 تابعنا:
https://t.me/{CHANNEL.replace('@','')}

❤️ لا تنسَ التفاعل"""

                bot.send_message(chat_id=CHANNEL, text=text)

                print("Posted:", text)

                post_count = (post_count + 1) % 6
                last_minute = now.minute

    time.sleep(30)
