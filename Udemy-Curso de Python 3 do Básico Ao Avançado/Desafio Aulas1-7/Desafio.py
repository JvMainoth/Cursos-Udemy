idade = 22
altura = 1.76
peso = 60
nome = 'Mainoth'
ano = 2020
nasc = ano - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}KG')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nasc}')
