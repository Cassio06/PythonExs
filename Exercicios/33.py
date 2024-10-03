num = int(input('Diga o seu salario: '))
if num >= 1250:
    aumento = num + (num/10)
    print(aumento)
if num < 1250:
    aumento1 = num+(num/100 * 15)
    print(aumento1)