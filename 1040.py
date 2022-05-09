a, b, c, d = map(float, input().split())
media = (a*2 + b*3 + c*4 + d) / 10
print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif 5 <= media < 7:
    print('Aluno em exame.')
    rec = float(input())
    print(f'Nota do exame: {rec}')
    final = (rec + media) / 2
    if final >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reaprovado.')
    print(f'Media final: {final:.1f}')
else:
    print('Aluno reprovado.')
