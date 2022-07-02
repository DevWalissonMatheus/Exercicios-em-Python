print("Qual o maior número?\n")
while True:
    try:
        prim_num = float(input('Insira o primeiro número: '))
        if prim_num >= 0:
            break
    except ValueError:
        print('Insira um valor númerico')
while True:
    try:
        seg_num = float(input('Insira o segundo número: '))
        if seg_num >= 0:
            if prim_num > seg_num:
                print('O maior número é: ',prim_num)
                break
            elif seg_num > prim_num:
                print('O maior número é: ',seg_num)
                break
    except ValueError:
        print('Insira um valor númerico')