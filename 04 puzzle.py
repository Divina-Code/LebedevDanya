zagadka = "когда отец ушёл за хлебом, он был на 18 лет старше сына\nчерез 4 года, когда он вернулся и стал в два раза старше сына \nсколько лет было сыну, когда отец ушёл за хлебом?"
print (zagadka)
k=False
otvet=int(input())
while k!=True:
    if otvet==14:
        print ("да, ты узнал когда отец ушёл за хлебом")
        k = True
    else:
        print ("ты так и не узнал, когда отец ушёл за хлебом \nпопробуй ещё")
        otvet = int(input())
        k = False
print ('Спасибо за ответ!')
