print('find the mystery number')
k = False
answer =int(input('число_'))
while k != True:
    if answer == 147:
        print('ты угадал')
        k = True
    elif answer > 147:
        print('число меньше')
        answer =int(input('число_'))
    elif answer < 147:
        print('число больше')
        answer =int(input('число_ '))
print('МОЛОДЕЦ')
