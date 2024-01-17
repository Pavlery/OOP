import tkinter as tk

class Combobox:
    def __init__(self, master):
        self.master = master
        master.title("Иллюзия")

        # Создаем комбинированный список
        self.combobox = tk.StringVar()
        self.combobox.set("Выбери")  # Значение по умолчанию

        options = ["Ну ладно", "Вот это", "Не выбирать"]
        self.dropdown = tk.OptionMenu(master, self.combobox, *options)
        self.dropdown.pack(pady=20)

        # Привязываем событие изменения комбинированного списка к функции
        self.combobox.trace_add("write", self.on_combobox_change)

        # Создаем метку для отображения текста
        self.label = tk.Label(master)

        # Создаем виджет, где будет текст
        self.text_widget = tk.Text(master, width=40, height=12, wrap=tk.WORD)
        self.text_widget.pack(pady=20)

    def on_combobox_change(self, *args):
        selected_option = self.combobox.get()

        # В зависимости от выбранной опции, устанавливаем соответствующий текст
        if selected_option == "Ну ладно":
            text = "Смирение - добродетель. Смирение - видение своих грехов, надежда только на чудо. Поэтому смиренно ожидаем зачет."
        elif selected_option == "Вот это":
            text = "Ты какой-то правильный что ли? Читать умеешь? Это выбор человека, который точно уже получит зачёт."
        else:
            text = "Читать не умеешь или не хочешь - это многое говорит о тебе. И чё ты теперь удивляешься, что ничего не успеваешь сдать?"

        self.label.config(text=text)

        # Очищаем и устанавливаем новый текст в виджет
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, text)

class Checkbox:
    def __init__(self, master):
        self.master = master
        master.title("Аминь")

        self.check_var = tk.BooleanVar()
        self.check_var.set(False)

        self.check_button = tk.Checkbutton(master, text="Зачёт", variable=self.check_var, command=self.checkbox_changed)
        self.check_button.pack(pady=10)

        self.label = tk.Label(master, text="")
        self.label.pack()

        self.input_entry = tk.Entry(master, state="normal")
        self.input_entry.pack(pady=10)

    def checkbox_changed(self):
        if self.check_var.get():
            self.label.config(text="Completed! You're star")
            self.input_entry.config(state="disabled")
        else:
            self.label.config(text="Опять на пересдачу =(")
            self.input_entry.config(state="normal")

class Keyboard:
    def __init__(self, master):
        self.master = master
        master.title("Бей по клаве")

        self.text_entry = tk.Entry(master)
        self.text_entry.pack(pady=15)

        self.text_entry.bind("<Key>", self.key_pressed)

        self.label_key = tk.Label(master, text="")
        self.label_key.pack()

        self.label_text = tk.Label(master, text="")
        self.label_text.pack()

    def key_pressed(self, event):
        key = event.char
        current_text = self.text_entry.get()
        self.label_key.config(text=f"Ты жмал на: {key},")
        self.label_text.config(text=f"а получилось - {current_text}")

def main():
    root = tk.Tk()
    # выбрать название необходимого класса (app = ___(root))
    app = Keyboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()