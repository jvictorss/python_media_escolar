# Média escolar:
aluno = input('Digite o nome do aluno: ')
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Número digitado errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Número digitado errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Número digitado errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Número digitado errado. Primeiro bimestre: '))
media = (a + b + c + d) / 4
soma = a + b + c + d
if a, b, c, d <=10:
    print('Média: {}'.format(media))
    if media <= 7:
        print('A média de {} foi {}. Status: REPROVADO.'.format(aluno, media))
    else:
        print('A média de {} foi {}. Status: APROVADO.'.format(aluno, media))
else:
    print('Há uma nota errada. Conserte')
