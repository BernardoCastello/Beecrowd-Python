x = int(input())
c = 0
while True:
    if x % 2 ==1:
        c += 1
        print(x)
    x += 1
    if c == 6:
        break
