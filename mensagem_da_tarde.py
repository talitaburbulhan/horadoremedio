import requests
import os


token = os.environ["TELEGRAM_TOKEN"] 
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_ids = 1007648629, 1884457800
for chat_id in chat_ids:
  text = "<b>Oi Flávio, boa tarde!</b>\n\nAgora é hora de tomar:\n\n2️⃣ Florinefes\n1️⃣ Velus\n1️⃣ Azatioprina."
  mensagem = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
  requests.post(url, data = mensagem)
