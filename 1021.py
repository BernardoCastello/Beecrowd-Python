n = float(input())
notas = int(n)
moedas = int((n - int(n)) * 100)
_100 = notas // 100
notas = notas % 100
_50 = notas // 50
notas = notas % 50
_20 = notas // 20
notas = notas % 20
_10 = notas // 10
notas = notas % 10
_5 = notas // 5
notas = notas % 5
_2 = notas // 2
_1 = notas % 2
m50 = moedas // 50
moedas = moedas % 50
m25 = moedas // 25
moedas = moedas % 25
m10 = moedas // 10
moedas = moedas % 10
m05 = moedas // 5
m01 = moedas % 5
print(f'''NOTAS:
{_100} nota(s) de R$ 100.00
{_50} nota(s) de R$ 50.00
{_20} nota(s) de R$ 20.00
{_10} nota(s) de R$ 10.00
{_5} nota(s) de R$ 5.00
{_2} nota(s) de R$ 2.00
MOEDAS:
{_1} moeda(s) de R$ 1.00
{m50} moeda(s) de R$ 0.50
{m25} moeda(s) de R$ 0.25
{m10} moeda(s) de R$ 0.10
{m05} moeda(s) de R$ 0.05
{m01} moeda(s) de R$ 0.01''')
