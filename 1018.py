n = int(input())
valor = n
cem = n // 100
n = n - (cem *100)
cinq = n // 50
n = n -(cinq*50)
vint = n // 20
n = n -(vint*20)
dez = n // 10
n = n -(dez*10)
cinc = n // 5
n = n -(cinc*5)
doi = n // 2
um = n - (doi*2)


print(f'''{valor}
{cem} nota(s) de R$ 100,00
{cinq} nota(s) de R$ 50,00
{vint} nota(s) de R$ 20,00
{dez} nota(s) de R$ 10,00
{cinc} nota(s) de R$ 5,00
{doi} nota(s) de R$ 2,00
{um} nota(s) de R$ 1,00''')
