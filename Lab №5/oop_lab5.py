class lab_5:
    def __init__(self):
        # Исходный массив чисел
        self.array = [1, 5, 19, 23, 107]

    def get_element(self, index):
        try:
            return self.array[index]
        # Обработка ИСКЛЮЧЕНИЯ
        except IndexError:
            raise IndexError("Индекс за пределами массива")

# Создаем объект массива
custom_array = lab_5()

# Пользователь вводит индекс
try:
    index = int(input("Введите индекс элемента (от 0 до 4): "))
    result = custom_array.get_element(index)
    print(f"Значение элемента: {result}")
except IndexError as alarm:
    print(f"Ошибка: {alarm}")
