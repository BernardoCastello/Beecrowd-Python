n = int(input())
for c in range(n):
    s = 0
    x = str(input())
    for c in x:
        if c=='1':
            s += 2
        elif c=='2':
            s += 5
        elif c=='3':
            s += 5    
        elif c=='4':
            s += 4
        elif c=='5':
            s += 5
        elif c=='6':
            s += 6
        elif c=='7':
            s += 3
        elif c=='8':
            s += 7
        elif c=='9':
            s += 6
        elif c=='0':
            s += 6
    print(f'{s} leds')
