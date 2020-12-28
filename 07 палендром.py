k1 = input("слово_")
k2 = k1[::-1].lower()
if k1.lower() == k2:
    print ("это палиндром")
else:
    print ("это не палиндром")
