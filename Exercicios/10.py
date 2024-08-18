altura = int(input('Diga a altura da parede: '))
largura = int(input('Diga a largura da parede: '))
print('Farei os calculos que resultarão na quantidade de tinta necessaria para pintar a area total da parede')
area = altura*largura
tinta = area/2
print(f'A quantidade de tinta necessaria para preencher a area de {area}m2 é {tinta}L')