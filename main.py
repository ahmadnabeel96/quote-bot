import asyncio
import os
import random
from datetime import datetime, timedelta
import pytz
from telegram import Bot
from openai import OpenAI

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = "@Quote0me"
CHANNEL_LINK = "https://t.me/Quote0me"

bot = Bot(token=TELEGRAM_TOKEN)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔥 توقيت الأردن
tz = pytz.timezone("Asia/Amman")

# ====== توليد منشور ======
def generate_post():
    prompt = """
اكتب اقتباس قصير جداً بأسلوب viral.

- سطر أو سطرين
- مؤثر
- بسيط
- أضف ايموجي أحياناً (🤍 ✨ 🌙)
"""
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=prompt,
        max_output_tokens=80,
    )
    return response.output[0].content[0].text.strip()

# ====== منشور الرابط ======
def generate_promo():
    return f"""🌙 سيعوضك الله عن كل شيء...

✨ انضم الآن:
{CHANNEL_LINK}"""

# ====== حساب الوقت القادم ======
def seconds_until(hour):
    now = datetime.now(tz)
    target = now.replace(hour=hour, minute=0, second=0, microsecond=0)

    if target < now:
        target += timedelta(days=1)

    return (target - now).total_seconds()

# ====== النظام ======
async def main():
    while True:
        print("🚀 جدول الأردن شغال")

        await asyncio.sleep(seconds_until(10))
        await bot.send_message(chat_id=CHANNEL_ID, text=generate_post())

        await asyncio.sleep(seconds_until(13))
        await bot.send_message(chat_id=CHANNEL_ID, text=generate_post())

        await asyncio.sleep(seconds_until(16))
        await bot.send_message(chat_id=CHANNEL_ID, text=generate_post())

        await asyncio.sleep(seconds_until(19))
        await bot.send_message(chat_id=CHANNEL_ID, text=generate_post())

        await asyncio.sleep(seconds_until(22))
        await bot.send_message(chat_id=CHANNEL_ID, text=generate_post())

        await asyncio.sleep(seconds_until(0))
        await bot.send_message(chat_id=CHANNEL_ID, text=generate_promo())

if __name__ == "__main__":
    asyncio.run(main())