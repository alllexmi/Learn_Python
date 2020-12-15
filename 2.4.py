a = input('Введите несколько слов: ')
b = []
i = 1
for el in range(a.count(' ') + 1):
    b = a.split()
    if len(str(b)) <= 10:
        print(f" {i} {b [el]}")
        i += 1
    else:
        print(f" {i} {b [el] [0:10]}")
        i += 1
print(a)
print(b)