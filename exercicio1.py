"""Análise do Problema: Projetar uma função para um sistema de segurança, cuja a senha é Giva123, e retornar se a senha está correta ou não

Definição dos dados: entrada e saída são strings

Especifição:Assinatura da função, propósito da função e exemplos
Assinatura da função: def verificarSenha(senhaDigitada):
Propósito da função: verificar se a senha digitada pelo usuário é igual à variável senhaCorreta
Exemplos:verificarSenha({lua123},{Senha incorreta});
	     verificarSenha({Ga3r3lo},{Senha incorreta});
	     verificarSenha({Giva123,{Senha correta});
"""


def verificarSenha(senhaDigitada: str):
    senhaCorreta = "Giva123"

    if senhaDigitada == senhaCorreta:
        print("A senha está correta!!")
    else:
        print("A senha está incorreta")


senhaDigitada = input('Digite a senha: ')

resultado = verificarSenha(senhaDigitada)
print(resultado)

#Verificação: ok
#Revisão: ok
