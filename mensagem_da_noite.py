import requests
import os


token = os.environ["TELEGRAM_TOKEN"] 
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_ids = 1007648629, 1884457800
for for_id in chat_ids:
  text = "Olha eu aqui de novo 🌚! Antes de dormir <b>não esqueça</b> de tomar 1️⃣ azatioprina e 1️⃣ luvox."
  mensagem = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
  requests.post(url, data = mensagem)
