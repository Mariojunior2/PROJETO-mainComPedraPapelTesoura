import random  # Para escolher perguntas aleatórias
import json  # Para salvar e carregar o progresso do usuário e banco de perguntas
import unicodedata  # Para normalizar e remover acentuação das strings
from difflib import SequenceMatcher  # Para comparar similaridade entre respostas

# Dicionário de perguntas e respostas
quiz = {
    "Qual a capital do Brasil?": "brasilia",
    "Nome do Criador do Jogo": "mario",
    "O presidente atual": "lula",
    "O melhor amigo do patrick": "bob esponja",
    "League of Legends é?": "ruim"
}


perguntas = list(quiz.keys())
respostas = list(quiz.values())


def fazer_quiz():
    for i in range(len(perguntas)):
        print(f"Pergunta {i+1}: {perguntas[i]}")
        respostau = input('Responda! ').lower() 
        
        if respostau == respostas[i]:
            print('Acertou!\n')
        else:
            print(f'Errou! A resposta correta era: {respostas[i]}\n')


fazer_quiz()



   




