import os
import time
from datetime import datetime
import pytz
from telegram import Bot
from openai import OpenAI

# 🔐 بيانات
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

# 🇯🇴 توقيت الأردن
tz = pytz.timezone("Asia/Amman")

# ⏰ جدول
schedule = [
    (9, 0),
    (12, 0),
    (15, 0),
    (18, 0),
    (21, 0),
    (0, 0)
]

last_post = None
count = 0

# 🤖 توليد عبارة
def generate_quote():
    prompt = """
اكتب اقتباس ديني قصير جداً:
- سطر أو سطرين
- مؤثر
- مع ايموجي بسيط
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

print("🚀 AI BOT STARTED")

while True:
    try:
        now = datetime.now(tz)

        for h, m in schedule:
            if now.hour == h and now.minute == m:
                key = f"{h}:{m}"

                if last_post != key:

                    text = generate_quote()

                    # 🔥 المنشور السادس مع رابط
                    if count == 5:
                        text += f"""

📌 تابعنا:
https://t.me/{CHANNEL.replace('@','')}"""

                    bot.send_message(chat_id=CHANNEL, text=text)

                    print("✅ Posted:", text)

                    count = (count + 1) % 6
                    last_post = key

        time.sleep(30)

    except Exception as e:
        print("❌ ERROR:", e)
        time.sleep(10)
