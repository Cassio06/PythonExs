import random
n = int(input('Digite um numero de 1 a 5 e tente acertar: '))
n1 = random.randint(1,5)
if n == n1:
    print('ACERTOU')
else:
    print(f'O numero {n} é diferente de {n1}')