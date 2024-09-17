import requests 

dicionario = {
    "for": "O loop for itera sobre uma sequência (lista, string, etc.)",
    "if": "O if é usado para avaliar uma condição em Python.",
    "function": "Uma função é um bloco de código que só é executado quando é chamado.",
    "list": "Uma lista é uma coleção que é ordenada e mutável. Permite valores duplicados."
}

def pequisar_termo_local(termo):
    termo = termo.lower()
    if termo in dicionario:
        return dicionario[termo]
    else: 
        return None
    
def pesquisar_api(termo):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{termo}"
    resposta = requests.get(url)
        
    if resposta.status_code == 200:
        dados = resposta.json()
        definicao = dados[0]['meanings'][0]['definitions'][0]['definition']
        return definicao
    else:
        return "não encontrado."
    
def pesquisar_termo():
    termo = input("Digite Oque deseja: ")
        
        
    definicao_local = pequisar_termo_local(termo)
        
    if definicao_local:
        print(f"Definicao encontrada:  {definicao_local}")
    else:
        print("Termo nao encontrado procurando em outro local...")
        definicao_externa = pesquisar_api(termo)
        print(f"Definicao encontrada: {definicao_externa}")
            
            
            
if __name__ == "__main__":
    pesquisar_termo()