while True:
    try:
        A, B, C = input().split()
        if A != B and A != C:
            print('A')
        elif B != A and B != C:
            print('B')
        elif C != A and C != B:
            print('C')
        else:
            print('*')
    except EOFError:
        break
