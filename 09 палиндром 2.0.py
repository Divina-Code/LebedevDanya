slova = input()
slova = slova.split()
for a in range (len(slova)):
    k1 = slova[a]
    k2 = k1[::-1].lower()
    if k1.lower() == k2:
        print (slova[a], "это палиндром")
    else:
        print (slova[a], "это не палиндром")
