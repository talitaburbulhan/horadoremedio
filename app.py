from flask import Flask
from flask import request
import requests
import os



### Página inicial. 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá, <b>pessoal</b>!</p>"

@app.route("/test")
def teste():
    token = os.environ["TELEGRAM_TOKEN"] 
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    chat_ids = 1007648629, 1884457800
    for chat_id in chat_ids:
        text = "Olha eu aqui de novo 🌚! Antes de dormir <b>não esqueça</b> de tomar 1️⃣ azatioprina e 1️⃣ luvox."
        mensagem = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
        requests.post(url, data = mensagem)
    return "ok"


### Site para o robô do telegram enviar dados das atualizações:



@app.route("/telegram", methods = ["POST"])  ### crio uma nota página (/telegram) e informo que esse será um página para receber dados (post).
def telegram():  ### dentro da função serão processados os dados enviados pelo Telegram. Colocar tokens/senhas no código NÃO é uma boa prática. 
    
    
    ## PROCESSA MENSAGEM
    update = request.json  ### "peguei os dados enviados pelo telegram". Request é um objeto do flask, que representa a requisição (o telegram está chamando/requisitando o site e passando os dados em json. O request pega o json enviado. Essas infomrações são armazendas na variável "dados". Na variável dados estará todo update que houver no meu robô)
    chat_id = update["message"]["chat"]["id"]
    text = update["message"]["text"].lower().strip()
    if text in ["oi", "ola", "olá", "olar", "oie", "oiê"]:
        answer = "Oi! Como vai?"
    elif text in ["bom dia", "boa tarde", "boa noite"]:
        answer = text
    elif "remedio" in text:
        answer = f"Os remédios estão no buraco do armário da cozinha."
    else:
        answer = "Não entendi."
    
    
    ## RESPONDE
    token = os.environ["TELEGRAM_TOKEN"]  ### dentro da biblioteca OS tem um dicionário chamado ENVIRON, que possui todas as variáveis de ambiente, que, no caso, o heroku vai passar ro nosso programa (no heroku eu "escondi" o token) 
    message = {"chat_id": chat_id, "text": answer}  ### aqui constam os dados que serão enviados para o robô
    url = f"https://api.telegram.org/bot{token}/sendMessage"    
    response = requests.post(url, data=message)   ### No código acima faço uma requisição para a API do telegram. 
    if response.json()["ok"] == False:
        raise RuntimeError("Erro ao responder API do Telegram")  ### essa etapa é para evitar aquele erro de quando muda o token, mas esquece de configurar ele no webhook (muda só no heroku). Se nao configurar no notebook tb, o robô nao vai mais responder, esse trecho faz aparecer uma mensagem de erro no heroku.  
        
    ## FINALIZAÇÃO
    return "ok"  ### precisa ter o return pq precisamos devolver algo para o telegram. Ele fez um requisição e precisa ter uma devolutiva. 

    
