"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False  10 == 10
"""
# 'type' para mostrar qual é o tipo do dado primitivo
print(type('Mainoth'))

print('Mainoth', type('Mainoth'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))
print(1 == 10, type(1 == 10))

print('Mainoth', type('Mainoth'), bool('Mainoth'))

# Conversão de str em int
print('10', type('10'), type(int('10')))
print('luiz', int(10))

# Exercicio

# String: nome
print('Mainoth', type('Mainoth'))

# Idade: int
print(22, type(22))

# Altura: float
print(1.82, type(1.82))

# É maior de idade 10 > 20
print(22 > 18, type(22 > 18))
