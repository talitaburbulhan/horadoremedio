import requests
import os


token = os.environ["TELEGRAM_TOKEN"] 
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_ids = 1007648629, 1884457800
for for_id in chat_ids:
  text = "Olha eu aqui de novo!! Antes de dormir não esqueça de tomar 1 azatioprina e 1 luvox."
  mensagem = {"chat_id": chat_id, "text": text}
  requests.post(url, data = mensagem)
