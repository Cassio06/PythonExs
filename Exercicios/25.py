frase = str(input('Diga uma frase: ')).upper()
print('A letra A aparece {}'.format(frase.count('A')))
print('A letra A aparece primeiro na casa numero {}'.format(frase.find('A')+1))
print('A letra A aparece por ultimo Ana casa numero {}'.format(frase.rfind('A')+1))