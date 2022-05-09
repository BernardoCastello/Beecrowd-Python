a, b = map(int, input().split(' '))
t = a * b
for c in range(1, 9):
    num = t * (c/10)
    inte = int(num)
    if num > inte:
        print(inte + 1, end=' ')
    else:
        print(inte, end=' ')
num = t * (9/10)
inte = int(num)
if num > inte:
    print(inte + 1)
else:
    print(inte)
