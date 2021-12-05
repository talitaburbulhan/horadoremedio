import requests
import os


token = os.environ["TELEGRAM_TOKEN"] 
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_id = 1007648629, 1884457800
text = "Olá, bom dia! É hora de tomar 2 florinefes/n 1 mesalazina/n 1 azatioprina."
mensagem = {"chat_id": chat_id, "text": text}
requests.post(url, data = mensagem)
