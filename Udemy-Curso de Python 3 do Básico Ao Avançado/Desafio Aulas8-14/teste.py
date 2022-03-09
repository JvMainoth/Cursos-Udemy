nome = input ('Digite seu nome: ')
letras = len(nome)

if letras <= 4:
    print('Seu nome é curto')
if letras >= 5 and letras <= 6:
    print('Seu nome é normal')
if letras > 6:
    print('Seu nome é muito grande')
