print('Produto mais barato\n')

while True:
    try:
        prod1 = float(input('Insira o valor do primeiro produto: '))
        break
    except ValueError:
        print('Insira um valor númerico!')
while True:
    try:
        prod2 = float(input('Insira o valor do segundo produto: '))
        break
    except ValueError:
        print('Insira um valor númerico!')
while True:
    try:
        prod3 = float(input('Insira o valor do terceiro produto: '))
        break
    except ValueError:
        print('Insira um valor númerico!')
if prod1 < prod2 and prod1 < prod3:
    print(f'Recomendamos o primeiro produto custando {prod1:.2f} reais')
elif prod2 < prod1 and prod2 < prod3:
    print(f'Recomendamos o segundo produto custando {prod2:.2f} reais')
elif prod3 < prod1 and prod3 < prod2:
    print(f'Recomendamos o terceiro produto custando {prod2:.2f} reais')
else:
    print('Todos os produtos custão o mesmo valor.')