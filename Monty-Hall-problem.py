import random
print("Введите количество дверей")
door_value=int(input())
print("Введите количество опытов")
n=int(input())
win=0
for i in range(n):
    priz_door = random.randint(0,door_value - 1)
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
    
