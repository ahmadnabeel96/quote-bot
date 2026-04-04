import os
import time
import openai
import pytz
import schedule
from datetime import datetime
from telegram import Bot

# =========================
# إعدادات
# =========================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

# توقيت الأردن
jordan_tz = pytz.timezone("Asia/Amman")

# =========================
# توليد نص
# =========================
def generate_post():
    prompt = "اكتب اقتباس عربي قصير جدًا، مؤثر، viral، سطرين فقط مع ايموجي بسيط"
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    
    return response.choices[0].message.content.strip()

# =========================
# إرسال منشور
# =========================
def send_post(with_link=False):
    try:
        text = generate_post()

        if with_link:
            text += "\n\n✨ انضم: https://t.me/Quote0me"

        bot.send_message(chat_id=CHANNEL_ID, text=text)
        print("✅ Posted:", text)

    except Exception as e:
        print("❌ Error:", e)

# =========================
# جدولة النشر
# =========================
schedule.every().day.at("10:00").do(send_post)
schedule.every().day.at("13:00").do(send_post)
schedule.every().day.at("16:00").do(send_post)
schedule.every().day.at("19:00").do(send_post)
schedule.every().day.at("22:00").do(send_post)
schedule.every().day.at("00:00").do(lambda: send_post(with_link=True))

print("🚀 البوت شغال بتوقيت الأردن")

# =========================
# تشغيل مستمر
# =========================
while True:
    schedule.run_pending()
    time.sleep(30)
