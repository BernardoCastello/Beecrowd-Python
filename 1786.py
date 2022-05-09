while True:
    try:
        x =input()
        b1 = 0
        b2 = 0
        
        c1 = 1
        c2 = 9

        for i in range(9):
            b1 += int(x[i]) * c1
            b2 += int(x[i]) * c2
            c1 += 1
            c2 -= 1

        if b1 % 11 == 10:
            b1 = 0
        else:
            b1 = b1 % 11

        if b2 % 11 == 10:
            b2 = 0
        else:
            b2 = b2 % 11 
        
        print(f'{x[0]}{x[1]}{x[2]}.{x[3]}{x[4]}{x[5]}.{x[6]}{x[7]}{x[8]}-{b1}{b2}')
        
    except EOFError:
        break
