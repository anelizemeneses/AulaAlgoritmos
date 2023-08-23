"""Analise do problema: projetar uma função que calcule o valor total da compra de laranjas com base em diferentes preços, dependendo da quantidade comprada
  Definição dos dados: Quantidade de laranjas compradas
  Especificação: Assinatura da função:def calcularTotal_laranjas(quantidade):
    Propósito:Define um preço por unidade de laranja, dependendo da quantidade comprada. Depois calcula e retorna o valor total da compra
    Exemplos: laranjas compradas = 8 -> total da compra: R$2,80
    laranjas compradas = 15 -> total da compra: R$4,50
    laranjas compradas = 5 -> total da compra: R$1,75
"""

# implementação


def calcularTotal_laranjas(quantidade):
    precoUND_laranja = 0.35  # Preço por laranja se compradas menos de uma dúzia
    if quantidade >= 12:
        precoUND_laranja = 0.30  # Preço por laranja se compradas pelo menos uma dúzia

    valor_total = quantidade * precoUND_laranja
    return valor_total


quantidade_laranjas = int(input("Digite o número de laranjas compradas: "))
valor_total = calcularTotal_laranjas(quantidade_laranjas)

print(f"O valor total da compra é: R${valor_total:.2f}")
#Verificação: ok
#Revisão: ok
