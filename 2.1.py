# 1. Создать список и заполнить его элементами различных типов данных.
#    Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
#    для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

a = list()
a.append(9)
a.append("abc")
a.append(["abc", 99])
a.append((11234))
a.append(None)

# print(a)
# a.reverse()
print(type(a))
def my_type(el):
    for el in range(len(a)):
        print(type(a[el]))
    return
my_type(a)