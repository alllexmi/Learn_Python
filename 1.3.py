n = str(input('Введите число: '))

a = n + n
b = n + n + n
r = int(n) + int(a) + int(b)
print(a)
print(b)
print(r)

# I don`t know, but it works!
print(f"{int(n) + int(n + n) + int(n + n + n)}")
