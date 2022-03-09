"""
Operadores Lógicos
and, or, not
in e not in
"""
# Verdadeiro E Verdadeiro = Verdadeiro
# Verdadeiro E Falso = Falso
"""comparacao1 and comparacao2

# Verdadeiro OU Verdadeiro = Verdadeiro
comp1 or comp2"""

# not inverte os valores
a = 2
b = 3

if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')

a = ''
b = 0

if not a:
    print('Por favor, preencha o valor de B')

#in e not in
nome = 'Mainoth'

if 'a' in nome:
    print('Existe a letra A no seu nome.')
else:
    print('Não existe.')

nome = 'Mainoth'

if 'ain' in nome:
    print('Existe a letra A no seu nome.')
else:
    print('Não existe.')

nome = 'Mainoth'

if 'a' not in nome:
    print('Executei')
else:
    print('Existe o texto.')


"""
Usuario e senha
"""
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Mainoth'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce está logado')
else:
    print('Usuario ou senha inválidos')




