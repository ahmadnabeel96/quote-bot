import os
import time
from datetime import datetime
import pytz
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME")

if not TOKEN or not CHANNEL:
    print("❌ Missing TOKEN or CHANNEL")
    exit()

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

last_post = None
index = 0

print("🚀 BOT RUNNING...")

while True:
    try:
        now = datetime.now(tz)

        # 🔥 heartbeat قوي (مهم)
        print(f"💡 Alive at {now.strftime('%H:%M:%S')}")

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

        time.sleep(10)  # ⬅️ قللناها (مهم)

    except Exception as e:
        print("❌ ERROR:", e)
        time.sleep(5)
