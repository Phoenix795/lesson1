# step 3(Простые типы данных)
v = input('Введите число от 1 до 10: ')
print(int(v) + 10) 

name = input('Введите ваше имя: ')
name_output = 'Привет, {}! Как дела?'.format(name)
print(name_output)

print(float('1'), int(2.5), bool(1), bool(''), bool(0))