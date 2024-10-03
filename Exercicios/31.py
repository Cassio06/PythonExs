y = int(input('Diga um ano e direi se é bissexto: '))
a = y % 4
if a == 0:
    print(f'O ano de {y} é bissexto ')
else:
    print(f'O ano de {y} não é bissexto ')