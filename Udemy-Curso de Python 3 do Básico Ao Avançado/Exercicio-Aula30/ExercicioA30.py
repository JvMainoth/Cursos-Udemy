"""
1 - Crie uma função que exibe uma saudação com os parâmetros cumprimento e nome
"""


def cumprimento(saudacao='Ola', nome='Mainoth'):
    print(saudacao, nome)


cumprimento()


"""
2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""


def soma(soma_1, soma_2, soma_3):
    print(soma_1 + soma_2 + soma_3)


soma(2, 4, 5)
"""
3-Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex.10%).Retorne (return) o 
valor do primeiro número somado do aumento do percentual do mesmo.
"""


def porcentagem(n1, n2):
    return n1 + (n1 * n2/100)


funcao = porcentagem(100, 10)
print(funcao)

funcao = porcentagem(500, 50)
print(funcao)

funcao = porcentagem(300, 25)
print(funcao)


"""
4-Fizz Buzz - Se o parâmetro da função for divisivel por 3, retorne fizz, se o parâmetro da função for divisível por 5, 
retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne fizzbuzz, caso contrário, retorne o número 
enviado.
"""


def fizzbuzz(n1):

    if n1 % 5 == 0 and n1 % 3 == 0:
        return 'buzzfizz'
#  n precisa de elif pois tem o return
    if n1 % 5 == 0:
        return 'buzz'

    if n1 % 3 == 0:
        return 'fizz'
#  n precisa de else pois tem o return
    return n1


poft = fizzbuzz(50)
print(poft)

poft = fizzbuzz(9)
print(poft)

poft = fizzbuzz(30)
print(poft)

poft = fizzbuzz(98)
print(poft)

"""
1-Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""


# def func1():
#     valor = 2
#     return valor
#
#
# def func2(funcao):
#     return funcao()
#
#
# var = func2(func1)
# print(var)



"""
2-Crie uma função1 que recebe uma função2 como parámetro e retorne o valor da função2 executada. Faça a função1 executar 
duas funções que recebebam um número diferente de argumentos.
"""


def func1(n10):
    return n10

def func2(nome, anos):
    return f'{nome}, {anos}'

def func_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


executando = func_mestre(func1, 'Luiz')
executando2 = func_mestre(func2, 'Marcelo', anos='TikTok')
print(executando)
print(executando2)

