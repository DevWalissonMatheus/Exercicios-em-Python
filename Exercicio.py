while True:
    try:
        prim_num = float(input('Insira o primeiro número: '))
        seg_num = float(input('Insira o segundo número: '))
        if prim_num > seg_num:
            print('O maior número é: ', prim_num)
            break
        elif seg_num > prim_num:
            print('O maior número é: ', seg_num)
            break
        else:
            print('ERRO!\nTente novamente')
            continue
    except ValueError:
        print('Insira um valor númerico')