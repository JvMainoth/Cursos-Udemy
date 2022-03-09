"""
for / while
while é usado para quando nos n sabemos quando a condição vai ter fim
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
# Maneira que eu fiz
cont = 0
num_decre = 10

while cont <= 10:
    print(f'{cont}, {num_decre}')
    cont = cont + 1
    num_decre = num_decre - 1

print('Terminamos a contagem!')

# Como o professor fez

for p, r in enumerate(range(10, 0, -1)):
    print (p, r)
