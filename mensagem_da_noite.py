import requests
import os


token = os.environ["TELEGRAM_TOKEN"] 
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_ids = 1007648629, 1884457800
for chat_id in chat_ids:
    text = "Olha eu aqui de novo!\n\n🌚 Antes de dormir <b>não esqueça</b> de tomar:\n\n1️⃣ Azatioprina\n1️⃣ Luvox."
    mensagem = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    requests.post(url, data = mensagem)

