while True:
    n = int(input('введите число от 0 до 10: '))
    if 0 < n < 10:
        print('Верно, молодец! :)))')
        print(n ** 2)
        break
    elif n  < 0:
        print('Нужно чуть больше :)) ')
    elif 10 < n:
        print('Нужно чуть меньше :)) ')
        
