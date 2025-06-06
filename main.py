import os
import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from keep_alive import keep_alive

# Start Flask server
keep_alive()

# Telegram bot credentials
BOT_TOKEN = BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']


def send_poll():
    now = datetime.now().strftime('%Y-%m-%d')
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"

    question = f"Mutabaah Amal ({now})"
    options = ["Mathurat Pagi", "Mathurat Petang", "1 muka Al-Quran sehari", "Solat berjemaah", "Riadah 1 minggu skali", "Ana tak sempat/terlupa"]

    payload = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": options,
        "is_anonymous": False,   # Not anonymous
        "allows_multiple_answers": True  # Can choose multiple
    }

    response = requests.post(url, json=payload)
    print(response.json())

# ✅ Send poll immediately upon start
send_poll()

# Scheduler
scheduler = BlockingScheduler(timezone="Asia/Kuala_Lumpur")
scheduler.add_job(send_poll, 'cron', hour=23, minute=0)  

# Start
scheduler.start()
