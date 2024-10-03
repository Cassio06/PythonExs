km = int(input('Diga a quantidade de KM a ser percorrida na sua viagem: '))
if km <= 200:
    km1 = km * 0.5
    print(f'O preço da passagem será {km1}')
else:
    km2 = km*0.45
    print(f'O preço da passagem será {km2}')