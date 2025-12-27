# variável global

dados = {
    "nome": "Alice",
    "idade": 30
}

def exibir_dados() -> None:
    # para modificar uma var global dentro da função, use a palavra-chave 'global'
    global dados
    
    # variável local
    dados_locais = {
        "cidade": "São Paulo",
        "profissão": "Engenheira"
    }
    
    print("Dados Globais:")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    
    print("\nDados Locais:")
    for chave, valor in dados_locais.items():
        print(f"{chave}: {valor}")


exibir_dados()