"""
Funções - def em Python (Parte 1)


def funcao():
    print('Hello World!')

funcao()
funcao()
funcao()
funcao()
"""

def saudacao(msg='Ola', nome='usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)

saudacao(nome='Zezinho', msg='Hi')
saudacao()
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
saudacao('Olá', 'Mainoth')

"""
Funções - def em Python (Parte 2)

def funcao(var):
    return var

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

def divisao(n1, n2):
    if n2 == 0:
        return n1 / n2

    return n1 / n2

divide = divisao(8,4)

if divide:
    print(divide)
else:
    print('Conta inválida.')
"""
def dumb():
    return 1

var = dumb()
print(var, type(var))

"""
Funções (def) em Python - *args **kwargs
(Parte 3)
"""


def func(*args, **kwargs):
    print(args)
    idade = kwargs['idade']
    print(idade)


lista = [1,2,3,4,5]
lista2 =[10,20,30,40,50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)

"""
Parte 4
"""

variavel = 'valor'

def func():
    print(variavel)

def func2():
    global variavel   # edita a variavel globalmente
    variavel = 'Outro valor'  # muda a variavel so aqui dentro da função
    print(variavel)

func()
func2()

print(variavel)