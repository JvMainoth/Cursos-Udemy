"""
* Enumerate - Enumerar elementos da lista #lista
"""
#           0      1       2
# lista = ['Edu', 'João', 'Luiz']

lista = [
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Helena', 'Ed', 'Lu'],  # 2
]

# enumerada = enumerate(lista)
# print(list(enumerada))

for v1, v2 in enumerate(lista):
    print(v1, v2)