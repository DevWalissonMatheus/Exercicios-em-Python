print('Valor decrecente.\n')

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

if num1 == num2 == num3:
    print('Todos os valores iguais!')
if num1 > num3 > num2:
    print(num1, num3, num2)
if num2 > num1 > num3:
    print(num2, num1, num3)
if num2 > num3 > num1:
    print(num2, num3, num1)
if num3 > num1 > num2:
    print(num3, num1, num2)
if num3 > num2 > num1:
    print(num3, num2, num1)