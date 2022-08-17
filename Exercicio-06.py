print('Maior entre 3 números\n')
while True:
    try:
        num1 = float(input('Insira o primeiro número: '))
        break
    except ValueError:
        print('Insira um valor númerico!')
while True:
    try:
        num2 = float(input('Insira o segundo número: '))
        break
    except ValueError:
        print('Insira um valor númerico!')
while True:
    try:
        num3 = float(input('Insira o terceiro número: '))
        break
    except ValueError:
        print('Insira um valor númerico!')

if num1 > num2 and num1 > num3:
    print('O maior número é', num1)
elif num2 > num1 and num2 > num3:
    print('O maior número é', num2)
elif num3 > num1 and num3 > num2:
    print('O maior número é', num3)
else:
    print('Todos iguais', num3)