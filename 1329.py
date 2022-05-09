while True:
    n = int(input())
    if n == 0:
        break
    
    lista = list(map(int, input().split()))
    maria = lista.count(0)
    joao = lista.count(1)

    print(f'Mary won {maria} times and John won {joao} times')
