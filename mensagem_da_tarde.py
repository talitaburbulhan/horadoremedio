import requests
import os


token = os.environ["TELEGRAM_TOKEN"] 
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_id = 1007648629, 1884457800
text = "Oi Flávio, boa tarde! Agora é hora de tomar 2 florinefes, 1 velus, 1 azatioprina."
mensagem = {"chat_id": chat_id, "text": text}
requests.post(url, data = mensagem)
