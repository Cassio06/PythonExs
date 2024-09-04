v = int(input('Diga a velocidade que vc está: '))
vm = 80
multa = (v-vm) * 7
if v >= vm:
    print(f'Você foi multado em R${multa} por estar acima do limite de velocidade de {vm}km/h')
else:
    print('sem multa')