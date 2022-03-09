"""
Entrada de dados
"""
input('Qual o seu nome? ')

# Atribuindo isso a uma variavel, na função input qualquer valor volta como string
nome = input('Qual o seu nome? ')
print(f'O usuário digitou {nome} e o tipo de variável é '
      f'{type(nome)}')

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
"""isso aqui da erro por idade ser uma string
ano_nascimento = 2020-idade"""
#maneira correta
ano_nascimento = 2020-int(idade)

print(f'{nome} tem {idade} anos.'
      f'{nome} nasceu em {ano_nascimento}.')

"""
Calculadora so de soma
"""
"""
Isso da erro por fazer somar strings
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
"""
#Maneira correta
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
"""
Ou tambem
numero_2 = int(numero_2)
"""

print( numero_1 + numero_2)
