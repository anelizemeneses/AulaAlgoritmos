"""Análise do Problema:
      O problema é calcular a multiplicação de dois números naturais "n1" e "n2".
  Definição dos dados: 
      Dois números inteiros
"""

import doctest


# Especificação e Implementação
def multiplicacao_recursiva(n1: int, n2: int):
    """
    Multiplica dois números naturais n1 e n2 através de somas sucessivas.
    Exemplos:
        >>> multiplicacao_recursiva(6, 4)
        24
        >>> multiplicacao_recursiva(0, 5)
        0
        >>> multiplicacao_recursiva(3, 0)
        0
    """
    # base: Se um dos números for igual a 0, o resultado é 0
    if n1 == 0 or n2 == 0:
        return 0
    # recursivo: Somar n2 com a multiplicação de (n1 - 1) por n2
    else:
        return n2 + multiplicacao_recursiva(n1 - 1, n2)


# Validação
print(multiplicacao_recursiva(6, 4))  # Deve imprimir 24
print(multiplicacao_recursiva(0, 5))  # Deve imprimir 0
print(multiplicacao_recursiva(3, 0))  # Deve imprimir 0
