"""
Inicio
"""
def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)

a = lambda x, y: x * y

print(a(2,2))

"""
Exemplo 1 - ordenando lista
"""

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

# def func(item):
#     return item[1]
#
# lista.sort(key=func, reverse=True)
# print(lista)
# ao inves disso utilizar

lista.sort(key=lambda item: item[1])
print(lista)

# outro exemplo de ordenança reverse=True oredena ao contrario

print(sorted(lista, key=lambda i: i[1], reverse=True))

# ordenando pelo nome do produto

print(sorted(lista, key=lambda i: i[0], reverse=True))