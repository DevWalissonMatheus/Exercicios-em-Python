print('Vogal ou Consoante?\n')
while True:
    letra = input('Insira a letra: ').lower()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('Vogal')
        break
    elif letra == 'b' or letra == 'c' or letra == 'd' or letra == 'f' or letra == 'g' or letra == 'h' or letra == 'j':
        print('Consoante')
        break
    elif letra == 'k' or letra == 'l' or letra == 'm' or letra == 'n' or letra == 'p' or letra == 'q' or letra == 'r':
        print('Consoante')
        break
    elif letra == 's' or letra == 't' or letra == 'v' or letra == 'w' or letra == 'y' or letra == 'z' or letra == 'ç':
        print('Consoante')
        break
    else:
        print('ERRO!')
        continue