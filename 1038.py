lista = [0, 4.00, 4.50, 5.00, 2.00, 1.50]
a, b = map(int, input().split())
total = lista[a] * b
print(f'Total: R$ {total:.2f}')
