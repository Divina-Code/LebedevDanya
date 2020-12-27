print('Привет, парень!')
name = input('Как тебя зовут?     ')
print('Привет, ', name, ',а в твоём имени ', len(name), " буков")
year = int(input('В каком году ты родил(ся/ась)?     '))
old = 2020-year
if old >= 18:
    print (name+", посмотри боевик")
else:
    print (name+", не смотри боевик, смотри комедию")
