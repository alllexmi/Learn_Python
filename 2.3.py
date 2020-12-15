a = int(input('Введите месяц: '))
b = ['Зима', 'Весна', 'Лето', 'Осень']
c = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if a == 1 or a == 12 or a == 2:
    print(b[0])
    print(c.get(1))
elif a == 3 or a == 4 or a == 5:
    print(b[1])
    print(c.get(2))
elif a == 6 or a == 7 or a == 8:
    print(b[2])
    print(c.get(3))
elif a == 9 or a == 10 or a == 11:
    print(b[3])
    print(c.get(4))
else:
    print("Такого месяца не существует")
