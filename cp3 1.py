
import requests
import json
import openai
import os
import time

API_KEY = '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'


def ChatGPT():

    #Aqui coloquei um input para o usuario digitar o que ele quer saber do chat gpt, mantive um exemplo somente para a visualização
    quest = 'Quanto tempo tem o planeta terra?'

    headers = {'Authorization': f"Bearer {API_KEY}", 'Content-Type': 'application/json'}

    link = 'https://api.openai.com/v1/chat/completions'

    id_modelo = "gpt-3.5-turbo"
    #Aqui realiza a consulta no GPT e depois retorna o que foi falado
    body_mensagem = {
        "model": id_modelo,
        "messages": [{'role': 'user', 'content': f'{quest}'}]
    }

    body_mensagem = json.dumps(body_mensagem)

    #Os próximos 3 passos é basicammente para printar e mostrar o resultado final  da consulta no GPT, preferi manter os nomes das variaveis que vem como exeplo.
    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    resposta = requisicao.json()
    mensagem = resposta['choices'][0]['message']['content']
    print("A resposta para a sua pergunta: ")
    time.sleep(1)
    print(mensagem)


def main():
    escolha = int(input("\nO que deseja fazer?\n Digite 1 para realizar perguntas para o Chat GPT \n Digite 2 para sair do Sistema\n"))
    if escolha == 1:
        ChatGPT()
    else:
        print("Você encerrou o sistema, Obrigado!")


if __name__== '__main__':
    main()