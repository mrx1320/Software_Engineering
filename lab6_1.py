from get_datetime import get_datetime
get_datetime()

user_input = input("Введите числа, разделенные пробелом: ")
numbers_list = user_input.split()
numbers_tuple = tuple(numbers_list)
print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)