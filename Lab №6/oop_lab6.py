import tkinter as tk
import threading
import time
import random

class MovingObject:
    def __init__(self, canvas, color, size, speed):
        # Инициализация объекта
        self.canvas = canvas
        self.color = color
        self.size = size
        self.speed = speed
        # Параметры координат для появления объекта и направления движения
        self.x = random.randint(50, 450)
        self.y = random.randint(50, 150)
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        # Создание объекта на холстре
        self.obj = canvas.create_oval(self.x, self.y, self.x + size, self.y + size, fill=color)

    def move(self):
        while True:
            # Осуществление перемещения в зависимости от начальной координаты и одного из направлений
            self.x += self.dx
            self.y += self.dy
            self.check_boundaries()
            self.canvas.coords(self.obj, self.x, self.y, self.x + self.size, self.y + self.size)
            time.sleep(self.speed)

    def check_boundaries(self):
        # Проверка границ окна и отражения объекта
        if self.x <= 0 or self.x + self.size >= self.canvas.winfo_width():
            self.dx *= -1
        if self.y <= 0 or self.y + self.size >= self.canvas.winfo_height():
            self.dy *= -1

class MovingObjectsGUI:
    # UI
    def __init__(self, root):
        self.root = root
        self.root.title("Шарики")

        self.canvas = tk.Canvas(root, width=500, height=200, bg='white')
        self.canvas.pack()

        self.objects = []
        # Изменить кол-во объектов по необходимости (for _ in range(___))
        for _ in range(5):
            # Создание объектов и запуск их движения в отдельных потоках
            obj = MovingObject(self.canvas, self.random_color(), 30, 0.025)
            self.objects.append(obj)
            thread = threading.Thread(target=obj.move)
            thread.daemon = True
            thread.start()

    def random_color(self):     # По приколу чисто
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

if __name__ == "__main__":
    root = tk.Tk()
    app = MovingObjectsGUI(root)
    root.mainloop()