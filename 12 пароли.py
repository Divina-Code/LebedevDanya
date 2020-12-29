from random import choice, randint
letters = str('abcdefg')
symb = str('!@#$%^&*')
numbers = str('0123456789')

password = ('')
for a in range(8):
    b = randint(1,3)
    if b == 1:
        c = choice(letters)
        d = randint(1,2)
        if d == 1:
            c=c.upper()
        password += c
    if b == 2:
        password += choice(symb)
    if b == 3:
        password += choice(numbers)
print (password)
