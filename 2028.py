cont = 1
while True:
    try:
        x = int(input())
        n = 1
        for h in range(x+1):
            n += h
        if x == 0:
            print(f'Caso {cont}: {n} numero')
            print(0)
        else:
            print(f'Caso {cont}: {n} numeros')
            print(0, end=' ')
            for c in range(x+1):
                for i in range(c):
                    if c == x and i == (c-1):
                        print(c)
                    else:
                        print(c, end=' ')
        cont += 1
        print()
    except EOFError:
        break
