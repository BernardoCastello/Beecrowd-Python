n = int(input())
cont = 0
while True:
    for c in range(n):
        print(f'N[{cont}] = {c}')
        cont += 1
        if cont == 1000:
            break
    if cont == 1000:
        break
