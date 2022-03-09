"""
Formando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casa decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(divisao)
print( '{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'João Mainoth'
print(f'{nome:s}')

num_3 = 1
print(f'{num_3:0>10}')

num_4 = 1150
print(f'{num_4:0>10}')

num_5 = 1150
print(f'{num_5:0^10}')  # coloca o número no centro

num_6 = 1150
print(f'{num_6:0<10}')

num_7 = 1150
print(f'{num_7:.2f}')  # formatando em float

num_8 = 1150
print(f'{num_8:0>10.2f}')

nome_2 = 'João Mainoth'
print(f'{nome:#^50}')

nome_formatado = '{:@>50}'.format(nome_2)
print(nome_formatado)

print(nome.lower())  # Tudo minusculo
print(nome.upper())  # Tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas

