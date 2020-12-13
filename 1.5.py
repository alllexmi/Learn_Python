a = int(input('Введите прибыль: '))
b = int(input('Введите издержки: '))
c = int(input('Введите количество сотрудников: '))
income = a - b
coeff = a / b
person_income = income / c
if a > b:
    print('У Вас прибыль: ', income)
else:
    print('У Вас убыток: ', income)
print('Соотношение прибыли в издержкам: ', coeff)
print('Прибыль на 1 сотрудника: ', person_income)
ю
