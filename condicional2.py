temperatura =int(input('Digita la temperatura: '))
gradosAlcohol = int(input('Digita grados de alcohol actual: '))

if temperatura>50 or gradosAlcohol>5:
    print('Alarma')
else:
    print('Normal')