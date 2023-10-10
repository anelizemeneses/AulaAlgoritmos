"""Analise do Problema:
      calcular o fatorial de um número inteiro não negativo "n".
  Definição dos dados: 
    entrada um numero inteiro nao negativo, e saída será um numero inteiro que representa o fatorial de 'n'
"""

import doctest


def fatorial(n: int) -> int:
    # implementação e especificação
    """
    Calcula o fatorial de um número inteiro n
        >>> fatorial(0)
        1
        >>> fatorial(1)
        1
        >>> fatorial(5)
        120
    """
    # base: fatorial de 0 é 1
    if n == 0:
        return 1
    # recursivo: fatorial de n é n multiplicado pelo fatorial de (n-1)
    else:
        return n * fatorial(n - 1)


"""Validação:
print(fatorial(0))  # Deve imprimir 1 (0! é definido como 1)
print(fatorial(1))  # Deve imprimir 1 (1! é 1)
print(fatorial(5))  # Deve imprimir 120 (5! é 120)
print(fatorial(10))  # Deve imprimir 3628800 (10! é 3628800)"""
