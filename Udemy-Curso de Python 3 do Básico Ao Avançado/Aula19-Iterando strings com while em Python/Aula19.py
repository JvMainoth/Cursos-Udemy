#        índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
contador = 0
# print(frase[5])
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')
# Iteração <- Iterar
while contador < tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]
    # if letra == 'r':
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
        # nova_string += 'R'
        #nova_string += frase[contador]
    # print(nova_string)
    else:
        nova_string += letra
    contador += 1

print(nova_string)
