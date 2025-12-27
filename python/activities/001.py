'''
Crie um programa em python que solicite ao usuario que digite um numero interio positivo n. Em seguida, calcule e exiba o fatorial desse numero n.

exemplo: se o usuario digitar 5, o programa deve calcular 5! = 5 x 4 x 3 x 2 x 1 = 120 e exibir o resultado.
'''

# Função para calcular o fatorial de um número
# Type hints: int -> int indica que recebe um inteiro e retorna um inteiro
def caclular_fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro positivo.
    
    O fatorial de n (n!) é o produto de todos os inteiros positivos de 1 até n.
    Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120
    
    Args:
        n: número inteiro positivo
        
    Returns:
        O fatorial de n
        
    Raises:
        ValueError: se n for negativo
    """
    # Validação: verifica se o número é negativo
    if n < 0:
        # raise: lança uma exceção, interrompendo a execução
        raise ValueError("O numero deve ser um inteiro positivo.")
    
    # Loop for com range decrescente
    # range(n-1, 0, -1): começa em n-1, vai até 1 (0 não é incluído), decrementando de 1 em 1
    # Exemplo: se n=5, range(4, 0, -1) gera: 4, 3, 2, 1
    for i in range(n - 1, 0, -1):
        # f-string: formatação de string para exibir a multiplicação
        print(f'{n} x {i}')
        # Operador *=: multiplicação com atribuição (n = n * i)
        # n acumula o resultado da multiplicação
        n *= i
    
    # Retorna o valor final do fatorial
    return n

# Entrada do usuário
# input(): captura entrada como string
# int(): converte a string para número inteiro
numero = int(input('Digite um numero inteiro positivo:'))

# Chama a função para calcular o fatorial
fatorial = caclular_fatorial(numero)

# Exibe o resultado usando f-string para formatação
print(f'O fatorial de {numero} é {fatorial}.')
