'''
Crie uma forma de retangulo e uma forma de triangulo usando o loop for aninhado.
Exiba no console cada forma com asteriscos (*).
'''
# argparse: módulo da biblioteca padrão para criar interfaces de linha de comando
import argparse

# Função para desenhar um retângulo com asteriscos
# Type hint None indica que a função não retorna valor
def desenhar_retangulo(altura: int, largura: int) -> None:
    """
    Desenha um retângulo usando asteriscos.
    
    Utiliza loops for aninhados:
    - Loop externo: controla as linhas (altura)
    - Loop interno: controla as colunas (largura)
    
    Args:
        altura: número de linhas do retângulo
        largura: número de colunas do retângulo
    """
    # Loop externo: percorre cada linha (altura)
    # range(altura): gera sequência de 0 até altura-1
    for i in range(altura):
        # Loop interno aninhado: percorre cada coluna (largura)
        # Este loop é executado completamente a cada iteração do loop externo
        for j in range(largura):
            # print com end=' ': imprime asterisco seguido de espaço na mesma linha
            # end=' ' substitui o comportamento padrão de quebra de linha
            print('*', end=' ')
        # print() sem argumentos: quebra de linha após completar uma linha do retângulo
        print()

# Função para desenhar um triângulo centralizado        
def desenhar_triangulo(altura: int) -> None:
    """
    Desenha um triângulo isósceles centralizado usando asteriscos.
    
    Utiliza loops for aninhados:
    - Loop externo: controla as linhas (altura)
    - Primeiro loop interno: adiciona espaços para centralizar
    - Segundo loop interno: adiciona asteriscos para formar o triângulo
    
    Padrão de crescimento:
    - Linha 0: 1 asterisco (2*0 + 1)
    - Linha 1: 3 asteriscos (2*1 + 1)
    - Linha 2: 5 asteriscos (2*2 + 1)
    
    Args:
        altura: número de linhas do triângulo
    """
    # Loop externo: para cada linha do triangulo
    for i in range(altura):
        # Primeiro loop interno: adiciona espaços à esquerda para centralizar
        # altura - i - 1: calcula quantidade de espaços decrescente
        # Exemplo: altura=5, linha 0 -> 4 espaços, linha 1 -> 3 espaços, etc.
        for j in range(altura - i - 1):
            # print com end='': imprime espaço sem quebra de linha
            print(' ', end='')
        
        # Segundo loop interno: imprime asteriscos que formam a base crescente
        # 2 * i + 1: fórmula para quantidade ímpar crescente de asteriscos
        # Garante simetria no triângulo (1, 3, 5, 7, 9, ...)
        for k in range(2 * i + 1):
            print('*', end='')
        
        # Quebra de linha após completar uma linha do triângulo
        print()

# Bloco principal: só executa se o arquivo for rodado diretamente
# __name__ == "__main__": verifica se não foi importado como módulo
if __name__ == "__main__":
    # ArgumentParser: cria um parser para argumentos de linha de comando
    parser = argparse.ArgumentParser()
    
    # add_argument: define os argumentos aceitos pelo programa
    # --function: argumento nomeado para escolher a forma
    # choices: lista de valores válidos
    # required=True: torna o argumento obrigatório
    parser.add_argument('--function', type=str, choices=['retangulo', 'triangulo'], 
                       required=True, help='Forma a ser desenhada: retangulo ou triangulo')
    
    # --altura: argumento para definir a altura da forma
    # type=int: converte o valor para inteiro
    parser.add_argument('--altura', type=int, required=True, help='Altura da forma')
    
    # --largura: argumento opcional (required não especificado)
    # Necessário apenas para retângulo
    parser.add_argument('--largura', type=int, help='Largura do retangulo (necessario apenas para retangulo)')
    
    # parse_args(): processa os argumentos da linha de comando
    # Retorna um objeto com os valores fornecidos
    args = parser.parse_args()
    
    # Estrutura condicional para decidir qual forma desenhar
    if args.function == 'retangulo':
        # Validação: verifica se a largura foi fornecida
        if args.largura is None:
            # Lança exceção se largura não foi especificada
            raise ValueError("A largura é obrigatoria para desenhar um retangulo.")
        # Chama a função para desenhar o retângulo
        desenhar_retangulo(args.altura, args.largura)
    elif args.function == 'triangulo':
        # Chama a função para desenhar o triângulo
        desenhar_triangulo(args.altura)
