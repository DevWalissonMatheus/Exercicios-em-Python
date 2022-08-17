print('Reajuste Salárial\n')

while True:
    try:
        sal_atual = float(input('Insira seu salário: '))
        if sal_atual <= 280:
            sal_ajust = sal_atual + (sal_atual * 20 / 100)
            v_aument = sal_ajust - sal_atual
            print(f'O salário atual é: {sal_atual:.2f}\n'
                   'O percentual de aumento aplicado é: 20%\n'
                  f'O valor do aumento é: {v_aument:.2f}\n'
                  f'O salário ajustado é: {sal_ajust:.2f}')
            break
        elif sal_atual > 280 and sal_atual <= 700:
            sal_ajust = sal_atual + (sal_atual * 15 / 100)
            v_aument = sal_ajust - sal_atual
            print(f'O salário atual é: {sal_atual:.2f}\n'
                   'O percentual de aumento aplicado é: 15%\n'
                  f'O valor do aumento é: {v_aument:.2f}\n'
                  f'O salário ajustado é: {sal_ajust:.2f}')
            break
        elif sal_atual > 700 and sal_atual <= 1500:
            sal_ajust = sal_atual + (sal_atual * 10 / 100)
            v_aument = sal_ajust - sal_atual
            print(f'O salário atual é: {sal_atual:.2f}\n'
                   'O percentual de aumento aplicado é: 10%\n'
                  f'O valor do aumento é: {v_aument:.2f}\n'
                  f'O salário ajustado é: {sal_ajust:.2f}')
            break
        elif sal_atual > 1500:
            sal_ajust = sal_atual + (sal_atual * 5 / 100)
            v_aument = sal_ajust - sal_atual
            print(f'O salário atual é: {sal_atual:.2f}\n'
                   'O percentual de aumento aplicado é: 5%\n'
                  f'O valor do aumento é: {v_aument:.2f}\n'
                  f'O salário ajustado é: {sal_ajust:.2f}')
            break
    except ValueError:
        print('Insira um valor númerico!')