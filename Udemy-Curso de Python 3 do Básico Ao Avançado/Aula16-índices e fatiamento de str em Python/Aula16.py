"""
Manipulando
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""
# positivos [012345678]
texto =     'Python s2'
#negativos -[987654321]
print(texto[2])

url = 'www.google.com.br/'
#negativos -[987654321]
print(url[:-1])  # vai sair sem a barra

# fatiando uma string
nova_string = texto[2:6]
print(nova_string)

nova_string_2 = texto[:6]  # pega desdo primeiro caractere
print(nova_string_2)

nova_string_3 = texto[7:]  # vai até o último caractere
print(nova_string_3)

nova_string_4 = texto[0:6:2]  # [0:6:2] o último digito diz de quantos em quantos caracteres pular
print(nova_string_4)

nova_string_4 = texto[0::2]  # pular de 2 em 2 a string inteira
print(nova_string_4)





