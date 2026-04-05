import os
import time
from datetime import datetime
import pytz
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME")

if not TOKEN or not CHANNEL:
    print("❌ Missing TOKEN or CHANNEL")
    while True:
        time.sleep(60)

bot = Bot(token=TOKEN)
tz = pytz.timezone("Asia/Amman")

quotes = [
    "✨ لا تيأس فالله معك دائمًا ❤️",
    "🌙 اذكر الله يطمئن قلبك 🤍",
    "🤍 كن قريبًا من الله تجد السلام 🌿",
    "💫 لا تحزن إن الله معنا ✨",
    "🌿 توكّل على الله فهو حسبك ❤️"
]

schedule = [
    (9, 0),
    (12, 0),
    (15, 0),
    (18, 0),
    (21, 0),
    (0, 0)
]

last_post_time = None
post_index = 0

print("🚀 Bot is running 24/7...")

while True:
    try:
        now = datetime.now(tz)

        for hour, minute in schedule:
            if now.hour == hour and now.minute == minute:

                current_time = f"{hour}:{minute}"

                if last_post_time != current_time:

                    if post_index < 5:
                        text = quotes[post_index]
                    else:
                        text = f"""✨ اقتباسات يومية 🤍

{quotes[post_index % len(quotes)]}

📌 تابعنا:
https://t.me/{CHANNEL.replace('@','')}

❤️ لا تنسَ التفاعل"""

                    bot.send_message(chat_id=CHANNEL, text=text)

                    print("✅ Posted:", text)

                    post_index = (post_index + 1) % 6
                    last_post_time = current_time

        time.sleep(30)

    except Exception as e:
        print("❌ Error:", e)
        time.sleep(10)
