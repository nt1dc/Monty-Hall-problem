import random
n=1000000
door_value=3
win=0
for i in range(n):
    priz_door = random.randint(0,door_value - 1)
    door=[]
    # прячим приз
    for i in range(door_value):
        if i == priz_door:
            door.append(1)
        else:
            door.append(0)
        ##print(door[i])

    choise = random.randint(0,door_value - 1)
    # открываем другую дверь
    if choise == priz_door:
        closed=random.randint(0,door_value - 1)
        while closed == choise:
            closed = random.randint(0,door_value - 1)
    else:
        closed = priz_door    
    ## меняем выбор
    choise = closed
    if choise == priz_door:
        win=win+1
print("Вероятность выигрыша при смене выбора равна:"  )
print(win/n)
    
