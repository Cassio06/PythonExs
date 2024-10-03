num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))
if num1 + num2 > num3:
    l1 = True
else:
    l1 = False
if num2 + num3 > num1:
    l2 = True
else:
    l2 = False
if num3 + num1 > num2:
    l3 = True
else:
    l3 = False
if l1 == True and l2 == True and l3 == True:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')