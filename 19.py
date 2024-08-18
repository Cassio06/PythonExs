import random
a1 = str(input('Diga o nome do aluno: '))
a2 = str(input('Diga o nome do aluno: '))
a3 = str(input('Diga o nome do aluno: '))
a4 = str(input('Diga o nome do aluno: '))
al = [a1, a2, a3, a4]
random.shuffle(al)
print(al)
