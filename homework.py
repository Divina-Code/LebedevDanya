import random
cislo=random.randint(1, 100)
print('Угадай число')
k = False
answer =int(input('число_'))
while k != True:
    if answer == cislo:
        print('ты угадал')
        k = True
    elif answer > cislo:
        print('число меньше')
        answer =int(input('число_'))
    elif answer < cislo:
        print('число больше')
        answer =int(input('число_ '))
print('МОЛОДЕЦ')
