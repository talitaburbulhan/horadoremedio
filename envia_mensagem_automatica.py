import requests
import os


token = os.environ["TELEGRAM_TOKEN"] 
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_id = 1007648629
text = "Olá, hora de tomar o remédio!"
mensagem = {"chat_id": chat_id, "text": text}
requests.post(url, data = mensagem)
