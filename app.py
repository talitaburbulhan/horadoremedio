from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá, <b>pessoal</b>!</p>"

### Site para o robô do telegram enviar dados das atualizações:


from flask import request
import requests


@app.route("/telegram", methods = ["POST"])  ### crio uma nota página (/telegram) e informo que esse será um página para receber dados (post).
def telegram():  ### dentro da função serão processados os dados enviados pelo Telegram. Colocar tokens/senhas no código NÃO é uma boa prática. 
    token = "2140351582:AAEMn6lRZTeV3ekUICnWV82MD85gW3bx7mg" ### API fornecida pelo @BotFather
    dados = request.json  ### "peguei os dados enviados pelo telegram". Request é um objeto do flask, que representa a requisição (o telegram está chamando/requisitando o site e passando os dados em json. O request pega o json enviado. Essas infomrações são armazendas na variável "dados". Na variável dados estará todo update que houver no meu robô)
    mensagem = {"chat_id": dados["message"]["chat"]["id"], "text": "Oi!"}  ### aqui constam os dados que serão enviados para o robô
    url = f"https://api.telegram.org/bot{token}/sendMessage"    
    requests.post(url, data=mensagem)   ### No código acima faço uma requisição para a API do telegram. 
    return "ok"  ### precisa ter o return pq precisamos devolver algo para o telegram. Ele fez um requisição e precisa ter uma devolutiva. 

    
