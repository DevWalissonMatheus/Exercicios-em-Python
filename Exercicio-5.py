print('Média de 2 notas\n')
while True:
    try:
        not1 = float(input('Insira a primeira nota: '))
        if not1 >= 0 or not1 <= 10:
            break
        elif not1 < 0 or not1 > 10:
            print('Valor inválido')
            continue
    except ValueError:
        print('ERRO!')
while True:
    try:
        not2 = float(input('Insira a segunsa nota: '))
        if not2 >= 0 or not2 <= 10:
            break
        elif not2 < 0 or not2 > 10:
            print('Valor inválido')
            continue
    except ValueError:
        print('ERRO!')
med = (not1 + not2) / 2

if med == 10:
    print('Aprovado com Distinção')
elif med < 10 and med >= 7:
    print('Aprovado')
elif med < 7:
    print('Reprovado')