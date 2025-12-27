"""
Exercício: Calculadora Simples com Funções

Objetivo: Criar uma calculadora simples que pode realizar 
quatro operações básicas: adição, subtração, multiplicação e divisão.

O usuário deverá fornecer dois números e a operação desejada. A solução 
deve ser implementada usando funções.

Instruções:

    Defina quatro funções: adicionar(), subtrair(), multiplicar() e dividir(). 
    
    - Cada função deve aceitar dois parâmetros (números) e retornar o resultado 
    da operação correspondente.
    - Peça ao usuário para inserir dois números.
    - Peça ao usuário para escolher uma das quatro operações (por exemplo, 
    ele pode digitar "adicionar" para adição).
    - Com base na escolha do usuário, chame a função correspondente e imprima o resultado.

"""
def calculadora() -> None:
    
    input("Bem-vindo à Calculadora Simples!\nPressione Enter para continuar...")
    input("Você pode realizar as seguintes operações: adicionar, subtrair, multiplicar, dividir.\nPressione Enter para continuar...")
    choice  = int(input('Escolha uma operação: \n 1. adicionar \n 2. subtrair \n 3. multiplicar \n 4. dividir \nDigite sua escolha: '))
    print(f'Você escolheu: {choice}')
    input("Pressione Enter para continuar...")
    
    # Definindo a função para adicionar dois números
    def adicionar(a, b):
        
        # Retorna a soma de a e b
        return a + b  

    # Definindo a função para subtrair um número do outro
    def subtrair(a, b):
        
        # Retorna a diferença entre a e b
        return a - b  

    # Definindo a função para multiplicar dois números
    def multiplicar(a, b):
        
        # Retorna o produto de a e b
        return a * b  

    # Definindo a função para dividir um número pelo outro
    def dividir(a, b):
        
        # Retorna a divisão de a por b
        return a / b  
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if choice == 1:
        print(f"{num1} + {num2} = {adicionar(num1, num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif choice == 3:
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif choice == 4:
        if num2 != 0:
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Erro: Divisão por zero não é permitida.")
            
    else:
        print("Operação inválida. Por favor, escolha adicionar, subtrair, multiplicar ou dividir. sendo os numeros 1, 2, 3 ou 4 respectivamente.")

calculadora()