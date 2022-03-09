
# nome = input('Qual o seu nome? ')

# print(nome or None or False or 0 or 'Você não digitou nada!' or 'Outra coisa')
# print(nome or 'Você não digitou nada!')

"""
Ao inves disso usar o que está acima
if nome:
    print(nome)
else:
    print('Você não digitou nada =(')
"""
# ele so vai para no valor verdadeiro
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g

print (variavel)

