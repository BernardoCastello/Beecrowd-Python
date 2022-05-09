n = int(input())
one = ['o', 'n', 'e']
two = ['t', 'w', 'o']
for c in range(n):
    x = []
    x = list(input())
    if len(x) > 3:
        print(3)
    else:
        if x[0] == 'o' and x[1] == 'n' or x[0] == 'o' and x[2] == 'e' or x[1] == 'n' and x[2] == 'e':
            print(1)
        else:
            print(2)
