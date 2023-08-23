"""Análise do Problema:criar um programa que receba a média final de um aluno e retorne o conceito correspondente com base nas faixas de notas especificadas
Definição dos Dados: os dados necessários é a média final do aluno que é um valor numérico
Especificações: Assinatura da função: def obter_conceito(media):
    propósito da função: verficar a media dada pelo usuario e retornar qual o seu conceito
    exmplos: media_final({5.8}), (Conceito C)
             media_final({8.8}), (Conceito B)
             media_final({9.8}), (Conceito A)
"""

# implementação


def obter_conceito(media):
    if media >= 0.0 and media <= 4.9:
        return "D"
    elif media <= 6.9:
        return "C"
    elif media <= 8.9:
        return "B"
    elif media <= 10.0:
        return "A"
    else:
        return "Média inválida"


media_final = float(input("Digite a média final do aluno: "))

conceito = obter_conceito(media_final)
print(f"O conceito do aluno é: {conceito}")

#Verificação: ok
#Revisão: ok
