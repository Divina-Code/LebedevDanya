import random
a=int(0)
p1 = False
p2 = False
p3 = False
prog1 = False
prog2 = False
prog3 = False
player1 = random.randint(11, 11)
player2 = random.randint(11, 11)
player3 = random.randint(11, 11)
winner=0
prover1=0
prover2=0
prover3=0
while p1 is False or p2 is False or p3 is False:
    prover1=0
    prover2=0
    prover3=0
    if player1 < 22:
        print('У игрока1 счёт', player1)
        if not p1:
            while prover1 !=1:
                beresh1 = input('Игрок1, будешь брать карту?_')
                print('')
                if beresh1 == 'да':
                    prover1=1
                    k1 = random.randint(11, 11)
                    player1 += k1
                    print('Игроку1 выпало', k1)
                    if player1==21:
                        print('Игрок1 победил со счётом 21\n')
                        break
                    elif player1>21:
                        print("Игрок1 проиграл, т.к. его счёт", player1, 'больше 21\n')
                        p1=True
                        prog1 = True
                    else:
                        print('У игрока1 счёт', player1, '\n')
                elif beresh1 == 'нет':
                    prover1=1
                    p1=True
                else:
                    print('Ошибка ввода')
            beresh1=str('нет')
    else:
        print("Игрок1 вышел из игры, так как его счёт", player1,'больше 21\n')
    if player2 < 22:
        print('У игрока2 счёт', player2)
        if not p2:
            while prover2 !=1:
                beresh2 = input('Игрок2, будешь брать карту?_')
                print('')
                if beresh2 == 'да':
                    prover2=1
                    k1 = random.randint(11, 11)
                    player2 += k1
                    print('Игроку2 выпало', k1)
                    if player2==21:
                        print('Игрок2 победил со счётом 21\n')
                        break
                    elif player2>21:
                        print("Игрок2 проиграл, т.к. его счёт", player2, 'больше 21\n')
                        p2=True
                        prog2 = True
                    else:
                        print('У игрока2 счёт', player2, '\n')
                elif beresh2 == 'нет':
                    prover2=1
                    p2=True
                else:
                    print('Ошибка ввода')
            beresh2=str('нет')
    else:
        print("Игрок2 вышел из игры, так как его счёт", player2,'больше 21\n')
    if player3 < 22:
        print('У игрока3 счёт', player3)
        if not p3:
            while prover3!=1:
                beresh3 = input('Игрок3, будешь брать карту?_')
                print('')
                if beresh3 == 'да':
                    prover1=1
                    k1 = random.randint(11, 11)
                    player3 += k1
                    print('Игроку3 выпало', k1)
                    if player3==21:
                        print('Игрок3 победил со счётом 21\n')
                        break
                    elif player3>21:
                        print("Игрок3 проиграл, т.к. его счёт", player3, 'больше 21\n')
                        p3=True
                        prog3=True
                    else:
                        print('У игрока3 счёт', player3, '\n')
                elif beresh3 == 'нет':
                    prover3=1
                    p3=True
                else:
                    print('Ошибка ввода')
            beresh3=str('нет')
    else:
        print("Игрок3 вышел из игры, так как его счёт", player3,'больше 21\n')
    if prog1 and prog2 and prog3:
        print('Все поиграли')
    elif (prog1 and prog2) or (prog1 and prog3) or (prog2 and prog3):
        if prog1 and prog2:
            print('победитель Игрок3')
        elif prog1 and prog3:
            print('победитель Игрок2')
        elif prog2 and prog3:
            print('победитель Игрок1')
        break
    else:
        if player1<22:
            ochki1=player1
        else:
            ochki1=0
        if player2<22:
            ochki2=player2
        else:
            ochki2=0
        if player3<22:
            ochki3=player3
        else:
            ochki3=0
        ######################
        ######################
        if ochki1>ochki2:
            a=ochki1
            winner=1
        else:
            a=ochki2
            winner=2
        if a<ochki3:
            a=ochki3
            winner=3
    break
if winner==1:
    print('Победитель игрок1')
if winner==2:
    print('Победитель игрок2')
if winner==3:
    print('Победитель игрок3')
print(prog1, prog2, prog3)


