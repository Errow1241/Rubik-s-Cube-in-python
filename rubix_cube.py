import random

colors = ['Red', 'Green', 'Blue']

color = random.choice(colors)
color1 = random.choice(colors)
color2 = random.choice(colors)
color3 = random.choice(colors)
color4 = random.choice(colors)
color5 = random.choice(colors)
color6 = random.choice(colors)
color7 = random.choice(colors)
color8 = random.choice(colors)

red = ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', ]
green = ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', ]
blue = ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', ]

color_array = [color,color1,color2,color3,color4,color5,color6,color7,color8]

print("%s|%s|%s" % (color,color1,color2))
print("%s|%s|%s" % (color3,color4,color5))
print("%s|%s|%s" % (color6,color7,color8))

if color_array == green or cary == red or cary == blue:
    print('You Win')
