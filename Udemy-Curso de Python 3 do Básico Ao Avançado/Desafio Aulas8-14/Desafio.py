# Programa 1
num = input('Digite um número inteiro: ')
if num.isdigit():
    num = int(num)

    if num % 2 == 0:
        print('Esse número é par.')
    else:
        print('Esse número é ímpar.')

else:
    print('Isso não é um número inteiro')

# Programa 2

horas = input('Digite um horário(0-23): ')

if horas.isdigit():
    horas = int(horas)

    if horas < 0 or horas > 23:
        print("Horário deve estar entre 0 e 23")
    else:
        if horas <= 11:
            print('Bom dia.')
        elif horas <= 17:
            print('Boa Tarde.')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite um horário entre 0 e 23')

# Programa 3

nome = input ('Digite seu nome: ')
letras = len(nome)

if letras <= 4:
    print('Seu nome é curto.')
elif letras <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
