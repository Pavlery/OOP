# Импорт библиотеки для GUI
import tkinter as tk
from tkinter import ttk

class HealthCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор калорий")

        self.label_weight = tk.Label(master, text="Вес (кг):")
        self.label_weight.grid(row=0, column=0)
        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=0, column=1)

        self.label_height = tk.Label(master, text="Рост (см):")
        self.label_height.grid(row=1, column=0)
        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=1, column=1)

        self.label_age = tk.Label(master, text="Возраст:")
        self.label_age.grid(row=2, column=0)
        self.entry_age = tk.Entry(master)
        self.entry_age.grid(row=2, column=1)

        self.label_gender = tk.Label(master, text="Пол:")
        self.label_gender.grid(row=3, column=0)

        self.gender_options = ['Male', 'Female']
        self.gender_var = tk.StringVar()
        self.gender_var.set(self.gender_options[0])

        self.gender_menu = ttk.Combobox(master, textvariable=self.gender_var, values=self.gender_options)
        self.gender_menu.grid(row=3, column=1)

        self.button_calories = tk.Button(master, text="Рассчитать калории", command=self.calculate_calories)
        self.button_calories.grid(row=4, column=0, columnspan=2)

        self.result_text = tk.Text(master, height=4, width=40)
        self.result_text.grid(row=5, columnspan=2)

    def calculate_calories(self):
        weight = float(self.entry_weight.get())
        height = float(self.entry_height.get())
        age = int(self.entry_age.get())
        gender = self.gender_var.get()

        health_calc = HealthCalculator(weight, height, age, gender)
        calories_result = health_calc.calculate_daily_calories()

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Дневная норма калорий: {calories_result:.2f}")

class HealthCalculator:
    def __init__(self, weight, height, age, gender):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender

    def calculate_daily_calories(self):
        if self.gender.lower() == 'male':
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161


        activity_factor = 1.2               #сидячий образ жизни
        daily_calories = bmr * activity_factor
        return daily_calories

# Главное окно
root = tk.Tk()
app = HealthCalculatorGUI(root)
root.mainloop()