# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

user_input = int(input('Введите время в секундах: '))
hours = user_input // 3600
minutes = user_input % 3600 // 60
seconds = user_input % 60
# result = int(f"{hours:02}':'{minutes:02}':'{seconds:02}")
print(f"{hours:02}:{minutes:02}:{seconds:02}")
