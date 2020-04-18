phrase = str(input('Write a phrase: '))
print('Pick a color:')
print('Red          Yellow')
print('Blue         White')
print('Purple       Green')
color = str(input('Cyan         Inverted\n')).lower()
colors = {    #normal colors

         'red':'\033[31m',
         'blue':'\033[34m',
         'yellow':'\033[33m',
         'white':'\033[30m',
         'purple':'\033[35m',
         'green':'\033[32m',
         'cyan':'\033[36m',
         'clean':'\033[m',
         'inverted':'\033[7;30;m',

         }
print('{}{}{}'.format(colors[color],phrase,colors['clean']))
