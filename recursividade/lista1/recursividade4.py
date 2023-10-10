"""Analise do Problema:
      Calcular o valor de uma série chamada série S, a série S é definida como: S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!, onde "n" é um valor inteiro positivo fornecido como parâmetro para a função
      
  Definição dos dados:
      Entrada um valor inteiro 'n', e saída um valor em ponto flutuante que representa o valor da série S calculada para o valor de "n" fornecido
"""

import doctest


# Implementação e especificação:
def fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro não negativo n.

    """
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


def serie_S(n: int) -> float:
    """
    Calcula o valor da série S para um valor inteiro positivo n.
        >>> serie_S(0)
        1.0
        >>> serie_S(1)
        2.0
        >>> serie_S(2)
        2.5
        >>> serie_S(5)
        2.7166666666666663
    """
    if n == 0:
        return
