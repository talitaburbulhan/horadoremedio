# horadoremedio

![CAPA-github-hora_do_remedio_bot_Prancheta 1_Prancheta 1](https://user-images.githubusercontent.com/89229665/146800221-e998739f-2107-4591-bd6d-240c6ed4bf30.png)

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

O robô está operacional, no entanto ele pode ser aprimorado. Algumas das melhorias em vista são:

- 💡 Criar um único arquivo com as três mensagens automática enviadas ao longo do dia. Para isso, deverá ser usada a **biblioteca datetime** que possibilitará gerar um código que informa o horário de cada string. 
- 💡 Gerar um banco de dados no Google Sheets com as informações de todas as mensagens do robô.
- 💡 Criar um botão no robô que ao ser selecionado devolve como resultado uma lista de todas as medicações em uso. 
