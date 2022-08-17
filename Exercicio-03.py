print('F -> Feminino ou M -> Masculino\n')
while True:
    sex = input('Qual seu Sexo?\n'
                'F -> Feminino ou M -> Masculino\n'
                '>>> ')
    if sex == 'F' or sex == 'f':
        print('Feminino')
        break
    elif sex == 'M' or sex == 'm':
        print('Masculino')
        break
    else:
        print('Sexo Inválido.')
        continue