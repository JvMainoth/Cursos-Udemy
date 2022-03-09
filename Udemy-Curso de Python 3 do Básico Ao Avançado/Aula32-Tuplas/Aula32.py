# Somando Tuplas

t1 = 1,2,3,4,5
t2 = 6,7,8,9,10
t3 = t1 + t2
print(t3)

# desempacotando em variaveis

t1 = 1,2,'Luiz',4,5
t2 = 6,7,8,9,10
t3 = t1 + t2

n1, n2, n3, *_, n10 = t3

print(n10)

# Exibindo a tupla varias vezes

t1 = (1,2,'Luiz',4,5) * 20

# transformando tupla em lista e alterando algo nela

t1 = (1,2,3,4,5)
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

print(t1)



