from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá, <b>pessoal</b>!</p>"

### Site para o robô do telegram enviar dados das atualizações:


from flask import request
import requests

@app.route("/telegram", methods=["POST"])
def telegram():
    token = "2140351582:AAEMn6lRZTeV3ekUICnWV82MD85gW3bx7mg"
    dados = request.jsonmensagem = {"chat_id": dados["message"]["chat"]["id"], "text": "Oi!"}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data=mensagem)
    return "ok"
    
