import requests
import os


token = os.environ["TELEGRAM_TOKEN"] 
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_ids = 1007648629, 1884457800
for chat_id in chat_ids:
    text = "<b>Olha eu aqui de novo!</b> 🌚\n\nAntes de dormir não esqueça de tomar:\n\n1️⃣ Azatioprina\n\n1️⃣ Luvox"
    mensagem = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    requests.post(url, data = mensagem)

