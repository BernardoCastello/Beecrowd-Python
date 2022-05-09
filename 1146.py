while True:
    x = int(input())
    if x == 0:
        break
    for c in range(1, x):
        print(c, end=' ')
    print(x)
