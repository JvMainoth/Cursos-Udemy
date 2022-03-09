"""
While/Else
contadores
acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break  # Apos o break else n acontece

    acumulador = acumulador + acumulador
    contador += 1
else:
    print('Cheguei no else.')