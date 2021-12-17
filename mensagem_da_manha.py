import requests
import os


token = os.environ["TELEGRAM_TOKEN"] 
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_ids = 1007648629, 1884457800
for chat_id in chat_ids:
  text = "<b>Olá,🌞 bom dia!</b>\nÉ hora de tomar: \n2️⃣florinefes, \n1️⃣ mesalazina, \n1️⃣ azatioprina."
  mensagem = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
  requests.post(url, data = mensagem)
