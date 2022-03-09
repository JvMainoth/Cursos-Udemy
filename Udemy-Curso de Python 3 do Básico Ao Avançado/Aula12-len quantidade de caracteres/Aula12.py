usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)  # O que é retornado da função len vem em int

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema.')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')

print(len(string2))
print(string2.__len__())

print(len(123456))  # Objeto do tipo inteiro, float e bool ira dar erro com a função len
