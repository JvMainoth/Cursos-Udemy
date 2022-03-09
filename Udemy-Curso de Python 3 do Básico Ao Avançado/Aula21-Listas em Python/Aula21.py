"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# #         0    1    2    3    4
# lista = ['A', 'B', 'C', 'D', 'E']
# #     -   5    4    3    2    1
# print(lista[1])
# print(lista[:3])
# print(lista[3:])
"""
l1 = [1,2,3]
l2 = [4,5,6]
# l3 = l1 + l2
#l1.extend((l2))
l1.extend('a')
l2.append('b')  # insere o valor no final
l2.insert(0,'banana')  # inserindo o valor 'banana' no indice 0
l2.pop()  # exclui 1 valor da lista

print(l1)
print(l2)
# print(l3)
"""
"""
l2 = [1,2,3,4,5,6,7,8,9]
print(l2)
l2.insert(0, 'Banana')
print(l2)
del(l2[0])  # deletando valores da lista
print(l2)

print(max(l2))  # Mostrar o valor max
print(min(l2))  # Mostrar o valor min
"""
"""
l2 = list(range(0, 100, 8))
print(l2)

for valor in l2:
    print(valor)
"""
"""
l2 = [0,1,2,3,4,5,6,7,8,9]

soma = 0
for valor in l2:
    soma = soma + valor
    print(f'{soma} + {valor} = {soma}')
print(soma)
"""
"""
# checando os elementos da lista

l2 = ['String', True, 10, -20.5]

for elem in l2:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')
"""
# jogo de adivinhação
secreto = 'perfume'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhuuuul, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Affffs, a letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'Apalavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')


