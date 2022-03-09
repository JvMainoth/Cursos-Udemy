"""
Desempacotamento de listas
"""
listas = ['Luiz', 'João', 'Maria',1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *_, ultimo_da_lista = listas

print(n1, n2, n3, *_)
print(*_)
print(ultimo_da_lista)