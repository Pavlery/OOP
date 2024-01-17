class lab_1:
    extinct_animals = []

    def __init__(self, name, order, former_range, date_of_extinction):
        self.name = name
        self.order = order
        self.areal = former_range
        self.year = date_of_extinction

    def print_to_file(self, file):
        file.write(f"{self.name:<30} {self.order:<30} {self.areal:<30} {self.year:<4d}\n")


animals = [
    lab_1("Сумчатый волк", "Сумчатые", "Австралия", 1936),
    lab_1("Стеллерова корова", "Сирены", "Командорские острова", 1768),
    lab_1("Островная хутия", "Грызуны", "Гондурас", 1950),
    lab_1("Сардинская пищуха", "Зайцеобразные", "Италия", 1774),
    lab_1("Незофонт", "Насекомоядные", "Куба", 1500),
    lab_1("Сантакрусский крылан", "Летучие мыши", "Соломоновы острова", 1907),
    lab_1("Тур", "Парнокопытные", "Восточная Европа", 1627),
    lab_1("Олень Шомбурга", "Парнокопытные", "Таиланд", 1938),
    lab_1("Яванский тигр", "Хищные", "Ява", 1976),
    lab_1("Сирийский кулан", "Непарнокопытные", "Аравийский полуостров", 1927),
    lab_1("Западный черный носорог", "Непарнокопытные", "Западная Африка", 2006),
    lab_1("Додо", "Птицы", "Маврикий", 1681)
]

# Сортировка по полю (ввести необходимый "х.___")
animals.sort(key=lambda x: x.year)

# Текстовик
try:
    with open("result.txt", "w") as file:
        file.write("Животное                       Класс                          Ареал                         Вымерло\n")
        file.write("----------------------------------------------------------------------------------------------------\n")
        for animal in animals:
            animal.print_to_file(file)
except FileNotFoundError as something:
    print(something)
