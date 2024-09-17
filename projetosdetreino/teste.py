pessoas = {
    "mario":"Lindo",
    "henrique":"OutroLindo",
    "inacio":"Mais lindo"
}



def pessoas_equipe(pessoa):
    pessoa = pessoa.lower()
    if pessoa in pessoas:
        return pessoas[pessoa]
    else:
        print(f"Pessoa nao achada: '{pessoa}'")
        return None
    ## Todo o Processo acima seria caso desse errado onde ele consulta e da o errado ou certo
    
if __name__ == "__main__":
    nome = input(f"digite o nome da pessoa: ")
    resultado = pessoas_equipe(nome)
    if resultado:
        print(f"encontrado! '{resultado}'")
        
## E aqui seria se o processo desse certo 


