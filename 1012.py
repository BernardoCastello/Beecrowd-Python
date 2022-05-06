a, b, c = map(float, input().split())
tri = (a*c)/2
circ = 3.14159 * (c**2)
tra = ((a + b)/2)* c
qua = b*b
ret = a * b
print(f'''TRIANGULO: {tri:.3f}
CIRCULO: {circ:.3f}
TRAPEZIO: {tra:.3f}
QUADRADO: {qua:.3f}
RETANGULO: {ret:.3f}''')
