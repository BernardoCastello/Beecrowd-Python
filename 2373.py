n = int(input())
quebrados = 0

for c in range(n):
    a, b = map(int, input().split())
    if a > b:
        quebrados += b

print(quebrados)
