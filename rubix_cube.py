import random

ary = ['Red', 'Green', 'Blue']

color = random.choice(ary)
color1 = random.choice(ary)
color2 = random.choice(ary)
color3 = random.choice(ary)
color4 = random.choice(ary)
color5 = random.choice(ary)
color6 = random.choice(ary)
color7 = random.choice(ary)
color8 = random.choice(ary)

red = ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', ]
green = ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', ]
blue = ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', ]

cary = [color,color1,color2,color3,color4,color5,color6,color7,color8]

print("%s|%s|%s" % (color,color1,color2))
print("%s|%s|%s" % (color3,color4,color5))
print("%s|%s|%s" % (color6,color7,color8))

if cary == green or cary == red or cary == blue:
    print('You Win')
