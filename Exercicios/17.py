import math
an = int(input('Diga um angulo: '))
tg = math.tan(math.radians(an))
cos = math.cos(math.radians(an))
sen = math.sin(math.radians(an))
print(f'O cos, Tg e Sen de {an} é {cos}, {tg}, {sen}')