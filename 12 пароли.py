from random import choice, randint
letters = str('abcdefghijklmnopqrstuvwxyz')
symb = str('!@#$%^&*')
numbers = str('0123456789')
let1 = 0 #кол-во букв
sym1 = 0 #кол-во символов
num1 = 0#кол-во цифр
passed = False # порверка пароля на подходяшность

while not passed:
    password = ('')
    for a in range(8):
        b = randint(1,3) #выбор из цифр, букв и символов
        if b == 1: # буквы
            c = choice(letters)
            d = randint(1,2)
            if d == 1:
                c=c.upper()
            password += c
        elif b == 2: # сиволы
            password += choice(symb)
        elif b == 3:# цифры
            password += choice(numbers)
        if b == 1:
            let1 += 1
        elif b == 2:
            sym1 += 1
        elif b == 3:
            num1 += 1
        if let1>0 and sym1>0 and num1>0:
            passed=True #проверка пароля на подходяшность
print (password)
