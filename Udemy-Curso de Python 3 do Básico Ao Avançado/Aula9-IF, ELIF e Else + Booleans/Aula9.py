"""
Condiçoes IF, ELIF e ELSE
"""
#If
if True:
    print('Verdadeiro.')

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)

if False:
    print('Verdadeiro.')
print('A minha expressão não é verdadeira.')

#Else
if False:
    print('Verdadeiro.')
else:
    print('Não é verdadeiro.')

#Elif
if False:
    print('Verdadeiro.')
elif True:
    print('Agora é verdadeiro.')
    nome = input('Qual o seu nome? ')

    print(f'Seu nome é {nome}.')
elif False:
    print('Mais uma é verdadeira.')
else:
    print('Não é verdadeiro.')


