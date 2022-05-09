n = int(input())
m = int(input())
lista = []

t = m
for c in range(n):
  lista.append(int(input()))

if(n==m):
  print(n)
elif(m>n):
  print(n)
else:
  lista.sort(reverse=True)

  corte = lista[m]
  del lista[:m-1]
  soma = lista.count(corte) - 1

  print(t + soma)
