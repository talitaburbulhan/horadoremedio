# horadoremedio

## Introdução:

Este repositório contém o site do robô **"Hora do remédio"** 🤖, uma automação criada para rodar no Telegram, que três vezes ao dia envia mensagens para meu pai, informando as medicações que ele deve tomar. Ele foi criado como trabalho final da disciplina de Algoritmos de Automação, do Insper, conduzida por [Álvaro Justen](https://github.com/turicas). 

## Instalação:

O site foi feito para rodar no [Heroku](https://www.heroku.com/) e depende das seguintes **bibliotecas**:

- ⚙️ flask
- ⚙️ requests
- ⚙️ os

## Sumário:

Este repositório é composto pelas seguintes pastas:

- 📂 .github/workflows/deploy.yml<br>Serve para informar ao Gitbub que qualquer mudança no site tem que ser subida no Heroku. No arquivo deploy.yml informo para qual app do Heroku, o Github deve enviar as alterações. 
- 📂 procfile<br/> Arquivo que informa o Heroku como ele deve rodar o site. Neste caso, executando o app.py. 
- 📂 app.py<br>É o código do meu site. 
- 📂 mensagem_da_manha.py<br>Contém o código da mensagem que o robô envia no período da manhã. 
- 📂 mensagem_da_noite.py<br>Contém o código da mensagem que o robô envia no período da tarde.
- 📂 mensagem_da_tarde.py<br>Contém o código da mensagem que o robô envia no período da noite.
- 📂 requirements.txt<br>Contém arquivo que informa quais são as bibliotecas necessárias para rodar o site. Bibliotecas que já vem com o Python **NÃO** podem ser colocadas. 

## Melhorias:
