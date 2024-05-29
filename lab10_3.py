from get_datetime import get_datetime
get_datetime()

def add_two(user_input):
    try:
        result = round(2 + float(user_input))
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

add_two("5")
add_two("7.01")
add_two("abcsadadwe")
add_two("13")
