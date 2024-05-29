from get_datetime import get_datetime
get_datetime()

class ValueTooLargeError(Exception):
    def __init__(self, value, max_value):
        self.value = value
        self.max_value = max_value
        self.message = f"Значение {value} превышает максимальное допустимое значение {max_value}"
        super().__init__(self.message)

def check_value(value, max_value):
    if value > max_value:
        raise ValueTooLargeError(value, max_value)

def process_data(data, threshold):
    for value in data:
        try:
            if value > threshold:
                raise ValueTooLargeError(value, threshold)
        except ValueTooLargeError as e:
            print(f"Ошибка обработки данных: {e}")

# Первый фрагмент
try:
    check_value(100, 50)
except ValueTooLargeError as e:
    print(e)

# Второй фрагмент
data = [30, 40, 60, 70]
threshold = 50
process_data(data, threshold)
