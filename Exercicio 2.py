print('Número Positivo ou Negativo?\n')
while True:
    try:
        num1 = float(input('Insira o primeiro número: '))
        if num1 < 0:
            print('O número é Negativo.')
        elif num1 > 0:
            print('O número é Positivo.')
        else:
            print('Número Neutro.')
    except ValueError:
        print('Insira um valor númerico.')
