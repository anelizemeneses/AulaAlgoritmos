"""Analise do Problema: Criar uma função para verificar se três valores dados (X, Y e Z) podem formar os comprimentos dos lados de um triângulo e, se possível, identificar o tipo de triângulo formado.

Definição de dados: valores reais (X, Y e Z)

Especificação: Assinatura da Função 1° def validar_triangulo(x, y, z):
    Propósito da Função: Retorna true se os valores podem formar um triângulo, senão, retorna false
    Exemplos: validar_triangulo{(3, 4, 5)},(true);

Assinatura da função: 2°: def identificar_tipo_triangulo(x, y, z):
    propósito da função: identifica e retorna o tipo de triângulo com base nos critérios: equilátero, isósceles ou escaleno.
    exemplos:identificarTriangulo({3, 3, 3}), (Triângulo Equilátero)
    identificarTriangulo({4, 4, 5}), (Triângulo Isóceles)
    identificarTriangulo({3, 4, 5}), (Triângulo Escaleno)
"""

# implementação


def validar_triangulo(x, y, z):
    if x < y + z and y < x + z and z < x + y:
        return True
    else:
        return False


def identificarTriangulo(x, y, z):
    if x == y == z:
        return "Triângulo Equilátero"
    elif x == y or x == z or y == z:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = float(input("Digite o valor de Z: "))

if validar_triangulo(x, y, z):
    tipo_triangulo = identificarTriangulo(x, y, z)
    print("É possível formar um triângulo:", tipo_triangulo)
else:
    print("Não é possível formar um triângulo com esses valores.")

#Verificação: ok
#Revisão: ok
