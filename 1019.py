n = int(input())
h = (n//60)//60
n = n - h * 60 * 60
m = n // 60
n = n - (m*60)
print(f'{h}:{m}:{n}')
