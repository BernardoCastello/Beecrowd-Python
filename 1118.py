while True:
    soma = 0
    cont = 0
    while True:
        n = float(input())
        if 0 <= n <= 10:
            soma += n
            cont += 1
            if cont == 2:
                break
        else:
            print('nota invalida')
    print(f'media = {soma/2:.2f}')
    while True:
        print('novo calculo (1-sim 2-nao)')
        r = float(input())
        if r == 1 or r == 2:
            break
    if r == 2:
        break
