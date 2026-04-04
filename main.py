import os
import time
import threading
from flask import Flask
from telegram import Bot
from openai import OpenAI

# ===== Web Server =====

app = Flask(**name**)

@app.route('/')
def home():
return "Bot is running 🚀"

def run_web():
app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_web).start()

# ===== Variables =====

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

# ===== Generate Post =====

def generate_post():
response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
{"role": "user", "content": "اكتب اقتباس قصير قوي جداً وجذاب مع ايموجي ✨"}
],
)
return response.choices[0].message.content

# ===== Promo Post =====

def generate_promo():
return "🌙 الفرج قريب... فقط ثق بالله.\n\n✨ انضم:\nhttps://t.me/Quote0me"

# ===== Send =====

def send_post(text):
bot.send_message(chat_id=CHANNEL_ID, text=text)

# ===== Schedule =====

def run_schedule():
posted_today = set()

```
while True:
    now = time.strftime("%H:%M")

    schedule = {
        "10:00": 1,
        "13:00": 2,
        "16:00": 3,
        "19:00": 4,
        "22:00": 5,
        "00:00": 6,
    }

    if now in schedule and now not in posted_today:
        try:
            if schedule[now] == 6:
                text = generate_promo()
            else:
                text = generate_post()

            send_post(text)
            print("✅ Posted:", text)

            posted_today.add(now)

        except Exception as e:
            print("❌ Error:", e)

    # Reset daily
    if now == "00:01":
        posted_today.clear()

    time.sleep(30)
```

# ===== Start =====

print("🚀 البوت شغال 24/7")
run_schedule()
