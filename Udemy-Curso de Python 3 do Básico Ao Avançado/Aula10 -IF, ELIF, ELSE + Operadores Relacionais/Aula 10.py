"""
Operadores Relacionais
==, >, >=, <, <=,
!= - Diferente
"""
# '==' pergunta se 2 é igual 2
print(2 == 2)
print(2 == 1)

num_1 = 2  # int
num_2 = '2'  # str

print(num_1 == num_2)

num_1 = 2  # int
num_2 = 2  # int

expressao = (num_1 == num_2)

print(expressao)

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

# limite para pegar emprestimo
menor = 20  # muito jovem
maior = 30  # passou da idade

if idade >= menor and idade <= maior:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} não pode pegar o empréstimo.')


