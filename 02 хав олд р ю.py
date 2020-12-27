print('Привет, парень!')
name = input('Как тебя зовут?     ')
print('Привет, ', name, 'а в твоём имени ', len(name), " буков")
year = int(input('В каком году ты родил(ся/ась)?     '))
if len(str(year)) ==4:
    print('А ',year,' неплохой год')
    print('Но получается вам ',2020-year,' лет')
else:
    print ('ты блин ошибся')
