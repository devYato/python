## Explicação do código `nested_for.py`

O arquivo `nested_for.py` cria uma lista com os quadrados dos números ímpares de `0` a `9` usando list comprehension e imprime o resultado:

```python
quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)
```

- `range(10)` gera os inteiros de `0` a `9`.
- O filtro `if x % 2 != 0` mantém apenas os valores ímpares.
- A expressão `x**2` é aplicada a cada `x` filtrado, produzindo o quadrado.
- O resultado final é uma lista: `[1, 9, 25, 49, 81]`.

### O que é uma list comprehension

List comprehension é uma forma concisa de criar listas em Python a partir de iteráveis, permitindo mapear valores e aplicar filtros em uma única expressão. A sintaxe geral é:

```python
[expressao for item in iteravel if condicao_opcional]
```

- `expressao`: o valor calculado para cada item que passa pela condição.
- `for item in iteravel`: itera sobre cada elemento do iterável.
- `if condicao_opcional`: filtro para incluir apenas itens que satisfaçam a condição (pode ser omitido).

Ela substitui laços `for` mais longos, tornando o código mais legível e compacto quando a lógica é simples.
