n = int(input())
anos = n // 365
meses = (n - (anos * 365)) // 30
dias  = n - (anos * 365) - (30 * meses)
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
