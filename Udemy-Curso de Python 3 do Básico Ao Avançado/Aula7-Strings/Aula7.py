nome = 'Mainoth'
idade = 22  # int
altura = 1.76  # float
e_maior = idade > 18  # bool
peso = 80
imc = peso / altura ** 2

print(nome, 'tem', idade, 'de idade e seu imc é', imc)

'''Formatando com strings e reduzindo a quantidade de números flutuantes com ":.2f"'''
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

'''Formatando em "format"'''
print('{} tem {} anos de idade e seu imc é {:.2f}'. format(nome, idade, imc))
'''{0} = nome, {1} = idade, {2} =imc'''
print('{0} tem {1} anos e seu imc é {2}'. format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im}'. format(n=nome, i=idade, im=imc))
