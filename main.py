import time
from telegram import Bot
from datetime import datetime
import pytz
import random
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = "@Quote0me"

bot = Bot(token=TOKEN)

# توقيت الأردن
timezone = pytz.timezone("Asia/Amman")

# أوقات النشر
schedule_times = ["10:00", "13:00", "16:00", "19:00", "22:00", "00:00"]

# اقتباسات
quotes = [
    "الإصرار هو مفتاح النجاح ✨",
    "لا تيأس، فالأجمل لم يأتِ بعد 💙",
    "كل يوم هو فرصة جديدة 🌿",
    "كن سبباً في سعادة من حولك ❤️",
    "ثق بنفسك دائماً 💪",
    "الأحلام لا تتحقق إلا بالسعي 🔥"
]

last_sent = None

print("🚀 البوت شغال بنظام الجدولة")

while True:
    now = datetime.now(timezone)
    current_time = now.strftime("%H:%M")

    if current_time in schedule_times and current_time != last_sent:
        quote = random.choice(quotes)

        message = f"""✨ {quote}

💭 اقتباسات يومية
📌 تابعنا: https://t.me/Quote0me
❤️ لا تنسى التفاعل"""

        try:
            bot.send_message(chat_id=CHANNEL_ID, text=message)
            print(f"✅ Posted at {current_time}")
            last_sent = current_time
        except Exception as e:
            print("❌ Error:", e)

    time.sleep(30)
