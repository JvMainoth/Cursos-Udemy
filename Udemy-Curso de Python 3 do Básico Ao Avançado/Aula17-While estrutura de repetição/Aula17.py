"""
While em Python
Utilizado para realizar ações enquanto
uma condição for verdadeiro
"""
"""
while True:  # loop infinito
    nome = input('Qual o seu nome? ')
    print(f'Olá {nome}!')

print('Não será executada. ') pois vai estar em loop ali em cima
"""
"""
x = 0
while x < 10:
   if x == 3:
        x = x + 1
        continue  # faz ele continuar codigo e sair do bloco, assim saindo do laço e loop
   
   print(x)
   x = x + 1

print('Acabou!')
"""
"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break  # quebra o laço e o prgrama

    print(x)
    x = x + 1

print('Acabou!')
"""

"""
x = 0  # coluna

while x < 10:
    y = 0  # Linha

    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1  # x = x + 1

print('Acabou!')
"""

####################Calculadora############################
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número. ')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)


