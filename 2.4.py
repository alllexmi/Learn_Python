# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
# только первые 10 букв в слове.

a = input("введите строку ")
b = []
i = 1
for el in range(a.count(' ') + 1):
    b = a.split()
    print(f" {i} {b[el][0:10]}")
    i += 1
