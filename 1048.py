x = float(input())
if x <= 400:
    y = x * 0.15
    print(f'''Novo salario: {(x+y):.2f}
Reajuste ganho: {y:.2f}
Em percentual: 15 %''')
elif x <= 800:
    y = x * 0.12
    print(f'''Novo salario: {(x + y):.2f}
Reajuste ganho: {y:.2f}
Em percentual: 12 %''')
elif x <= 1200:
    y = x * 0.10
    print(f'''Novo salario: {(x + y):.2f}
Reajuste ganho: {y:.2f}
Em percentual: 10 %''')
elif x <= 2000:
    y = x * 0.07
    print(f'''Novo salario: {(x + y):.2f}
Reajuste ganho: {y:.2f}
Em percentual: 7 %''')
else:
    y = x * 0.04
    print(f'''Novo salario: {(x + y):.2f}
Reajuste ganho: {y:.2f}
Em percentual: 4 %''')
