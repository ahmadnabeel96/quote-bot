import os
import time
import threading
from flask import Flask
from telegram import Bot
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def home():
return "Bot is running 🚀"

def run_web():
app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_web).start()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_post():
response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
{"role": "user", "content": "اكتب اقتباس قصير قوي جداً مع ايموجي ✨"}
],
)
return response.choices[0].message.content

def send_post(text):
bot.send_message(chat_id=CHANNEL_ID, text=text)

print("🚀 البوت شغال")

while True:
try:
text = generate_post()
send_post(text)
print("✅ Posted:", text)

```
    time.sleep(60)

except Exception as e:
    print("❌ Error:", e)
    time.sleep(10)
```
