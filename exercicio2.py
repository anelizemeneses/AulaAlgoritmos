"""Analise do Problema: Criar uma função que receberá a idade de 4 pessoas, fazer a média entre elas e identificar qual é a mais velha

Definição de dados: são 4valores numéricos(n1, n2, n3, n4) que representarão a idade das pessoas

Especificação: Assinatura da Função: 1°: def calcularMedia(n1: float, n2: float, n3: float, n4: float):
    Propósito da Função: a 1° função tem como propósito receber 4 números e calcular qual é a média desses valores
    Exemplos 1°: calcularMedia({10, 32, 39, 20}),(media: 25.25);
                 calcularMedia({10, 15, 20, 25}),(media: 17.5);

2° Assinatura da função: def maiorNumero(n1, n2, n3, n4):
    propósito da função: a função retorna a idade da pessoa mais velha
    Exemplos: maiorNumero({10, 15, 20, 25}),(mais velha: 25)
              maiorNumero({30, 20, 40, 10}),(mais velha: 40)
"""

# implementação


def calcularMedia(n1: float, n2: float, n3: float, n4: float):
    somaValores = n1 + n2 + n3 + n4
    media = somaValores / 4
    return media


def maiorNumero(n1, n2, n3, n4):
    if n1 >= n2 and n1 >= n3 and n1 >= n4:
        return n1
    elif n2 >= n1 and n2 >= n3 and n2 >= n4:
        return n2
    elif n3 >= n1 and n3 >= n2 and n3 >= n4:
        return n3
    else:
        return n4


n1 = int(input("Digite a idade da primiera pessoa: "))
n2 = int(input("Digite a idade da segunda pessoa: "))
n3 = int(input("Digite a idade da terceira pessoa: "))
n4 = int(input("Digite a idade da quarta pessoa: "))

media = calcularMedia(n1, n2, n3, n4)
pessoa_mais_velha = maiorNumero(n1, n2, n3, n4)

print("A média das idades é: ", media)
print("A idade da pessoa mais velha é: ", pessoa_mais_velha)

#Verificação: ok
#Revisão: ok
