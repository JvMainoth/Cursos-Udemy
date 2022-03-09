"""
Split, Join, Enumerate
* Split - Dividir uma string #str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # interáveis e utiliza touplas
* Strip - Retira o espaço do inicio e fim da string
* Capitalize - Deixa a primeira letra maiuscula
"""
# string = 'O Brasil é o país do futebol, o Brasil é penta.'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# # print(lista_2)
# # palavra = ''
# # contagem = 0
# #
# # for valor in lista_1:
# #     # print(valor)
# #     # print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase')
# #     qtd_vezes = lista_1.count(valor)
# #     if qtd_vezes > contagem:
# #         contagem = qtd_vezes
# #         palavra = valor
# #
# # print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
#
# for valor in lista_2:
#     print(valor.strip().capitalize())

# string = 'O Brasil é penta.'
# lista = string.split(' ')
# # string_2 = ','.join(lista)
# #
# # print(string)
# # print(lista)
# # print(string_2)
# for v1_indice, v2_valor in enumerate(lista):
#     print(v1_indice,v2_valor ,lista[v1_indice])

# lista = [
#     [0,'João'],
#     [1,'Victor'],
#     [2,'Mainoth'],
# ]
# for indice, nome in lista:
#     # print(v[0], v[1])
#     print(indice, nome)

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)
