import random
import unicodedata
import json
from difflib import SequenceMatcher 

arquivo_respostas = 'respostas.json'


def carregar_respostas():
    try:
        with open(arquivo_respostas, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def salvar_respostas(respostas):
    with open(arquivo_respostas, 'w') as f:
        json.dump(respostas, f, ensure_ascii=False, indent=4)


respostas = carregar_respostas()


if not respostas:
    respostas = {
        "qual seu nome?": "eu sou um gpt!",
        "como você está": "estou apenas um código, mas estou funcionando bem!",
        "o que você pode fazer?": "posso responder a perguntas básicas e manter uma conversa simples.",
        "qual é o sentido da vida?": "o sentido da vida é 42... pelo menos é o que dizem!",
        "qual a capital do brasil?": "brasilia",
        "quem descobriu a america?": "cristovao colombo",
        "em que ano foi a independencia do brasil?": "1822",
        "qual é a fórmula química da água?": "h2o",
        "quem escreveu o livro dom quixote?": "miguel de cervantes",
        "qual é o maior planeta do sistema solar?": "jupiter",
        "qual o rio mais longo do mundo?": "nilo",
        "quem pintou a mona lisa?": "leonardo da vinci",
        "qual é a moeda oficial do japão?": "iene",
        "quem foi o primeiro homem a pisar na lua?": "neil armstrong",
    }

def normalizar_texto(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return texto.lower()

def encontrar_melhor_correspondencia(pergunta):
    pergunta = normalizar_texto(pergunta)
    melhor_correspondencia = None
    maior_similaridade = 0.0
    
    for chave in respostas: 
        chave_normalizada = normalizar_texto(chave)
        similaridade = SequenceMatcher(None, pergunta, chave_normalizada).ratio()
        if similaridade > maior_similaridade:
            maior_similaridade = similaridade
            melhor_correspondencia = chave
    
    return melhor_correspondencia if maior_similaridade > 0.6 else None

def adicionar_resposta(pergunta, resposta):
    respostas[pergunta.lower()] = resposta
    salvar_respostas(respostas)  # Salva as respostas
    print(f"Nova pergunta e resposta adicionadas:\nPergunta: {pergunta}\nResposta: {resposta}")

def mini_chat_gpt(pergunta):
    pergunta_normalizada = normalizar_texto(pergunta)
    correspondencia = encontrar_melhor_correspondencia(pergunta_normalizada)
    
    if correspondencia:
        return respostas[correspondencia]
    else:
        print("Desculpe, não consegui entender a sua pergunta.")
        adicionar = input("Gostaria de adicionar uma resposta para essa pergunta? (sim/não): ").strip().lower()
        if adicionar == 'sim':
            nova_resposta = input("Por favor, insira a resposta para essa pergunta: ")
            adicionar_resposta(pergunta, nova_resposta)
            return "Resposta adicionada com sucesso!"
        else:
            return "Ok, vamos continuar!"

print("Bem-vindo ao meu Chat! (Digite 'sair' para acabar)")

while True:
    pergunta = input("Você: ")
    if normalizar_texto(pergunta) == "sair":
        print("Encerrado!")
        break
    resposta = mini_chat_gpt(pergunta)
    print("Mini Chat Gpt: " + resposta)
