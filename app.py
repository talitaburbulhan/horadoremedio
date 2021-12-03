from flask import Flask
from flask import request
import requests
import os

### Página inicial. 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá, <b>pessoal</b>!</p>"




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
    menssage = {"chat_id": chat_id, "text": answer}  ### aqui constam os dados que serão enviados para o robô
    url = f"https://api.telegram.org/bot{token}/sendMessage"    
    requests.post(url, data=menssage)   ### No código acima faço uma requisição para a API do telegram. 
    
    ## FINALIZAÇÃO
    return "ok"  ### precisa ter o return pq precisamos devolver algo para o telegram. Ele fez um requisição e precisa ter uma devolutiva. 

    
