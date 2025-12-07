# List comprehension: uma forma concisa de criar listas em Python
# Sintaxe: [expressão for item in iterável if condição]

# Cria uma lista com os quadrados dos números ímpares de 0 a 9
# x**2: eleva x ao quadrado (operador de exponenciação)
# for x in range(10): itera sobre os números de 0 a 9
# if x % 2 != 0: filtra apenas os números ímpares (resto da divisão por 2 diferente de 0)
quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)  # Resultado: [1, 9, 25, 49, 81]

# String para análise de caracteres
frase = "Python é incrível"

# List comprehension para filtrar apenas vogais
# c.lower(): converte o caractere para minúsculo para garantir comparação case-insensitive
# if c.lower() in 'aeiouéíáóú': verifica se o caractere é uma vogal (incluindo acentuadas)
char = [c for c in frase if c.lower() in 'aeiouéíáóú']

# List comprehension para filtrar consoantes, espaços e outros caracteres (não-vogais)
# if c.lower() not in 'aeiouéíáóú': verifica se o caractere NÃO é uma vogal
char_two = [c for c in frase if c.lower() not in 'aeiouéíáóú']

print(char)      # Resultado: ['o', 'é', 'i', 'í', 'e']
print(char_two)  # Resultado: ['P', 'y', 't', 'h', 'n', ' ', ' ', 'n', 'c', 'r', 'v', 'l']