from get_datetime import get_datetime
get_datetime()

try:
    number = float(input("Введите число от 0 до 10: "))
    if not 0 <= number <= 10: print("Число должно быть в диапазоне от 0 до 10.")
    elif number <= 3: print("Число находится в диапазоне от 0 до 3 включительно.")
    elif number <= 6: print("Число находится в диапазоне от 3 до 6.")
    else: print("Число находится в диапазоне от 6 до 10 включительно.")
except ValueError:
    print("Необходимо ввести число.")