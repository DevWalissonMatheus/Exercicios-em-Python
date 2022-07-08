print('Período do dia\n')

while True:
    turn = input('Em que turno você estuda?\n'
                   'M - Matutino, V - Vespertino e N - Noturno\n'
                   '>> ').lower()
    if turn == 'm':
        print('Bom dia!')
        break
    elif turn == 'v':
        print('Boa tarde!')
        break
    elif turn == 'n':
        print('Boa noite!')
        break
    else:
        print('ERRO!')
        continue