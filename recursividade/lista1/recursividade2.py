"""Analise do Problema:
      Projetar uma função que calcule a potencia de um numero "num" elevado a um expoente

  Definição dos dados:
      Dois numeros inteiros como entrada, e saida um valor inteiro
"""

import doctest


def potencia(num: int, expoente: int) -> int:
    # Especificão e Implementação:
    """
    Calcula a potência num^expoente.

    Examples:
        >>> potencia(2, 3)
        8
        >>> potencia(3, 4)
        81
        >>> potencia(5, 0)
        1
    """
    # Caso base: se expoente for igual a 0, o resultado é 1
    if expoente == 0:
        return 1
    # Caso recursivo: calcular num^expoente como num * num^(expoente-1)
    else:
        return num * potencia(num, expoente - 1)


"""Validação:
print(potencia(2, 3))  # Deve imprimir 8
print(potencia(3, 4))  # Deve imprimir 81
print(potencia(5, 0))  # Deve imprimir 1"""

# Revisão: para expoentes muito grandes, pode ser que haja um numero muito grande de chamadas recursivas
