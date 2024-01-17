import tkinter as tk

class LogicalOperation:
    def get_sign(self):
        pass

    def get_name(self):
        pass

    def estimate(self, a, b):
        pass

class AND(LogicalOperation):
    def get_sign(self):
        return "&&"

    def get_name(self):
        return "Logical AND"

    def estimate(self, a, b):
        return a and b

class OR(LogicalOperation):
    def get_sign(self):
        return "||"

    def get_name(self):
        return "Logical OR"

    def estimate(self, a, b):
        return a or b

class XOR(LogicalOperation):
    def get_sign(self):
        return "^"

    def get_name(self):
        return "Logical XOR"

    def estimate(self, a, b):
        return a ^ b

class ShefferStroke(LogicalOperation):
    def get_sign(self):
        return "|"

    def get_name(self):
        return "Sheffer Stroke (Logical NAND)"

    def estimate(self, a, b):
        return not (a and b)

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Logical Calculator")

        self.label1 = tk.Label(master, text="Operand 1:")
        self.label1.grid(row=0, column=0)

        self.operand1_entry = tk.Entry(master)
        self.operand1_entry.grid(row=0, column=1)

        self.label2 = tk.Label(master, text="Operand 2:")
        self.label2.grid(row=1, column=0)

        self.operand2_entry = tk.Entry(master)
        self.operand2_entry.grid(row=1, column=1)

        self.label3 = tk.Label(master, text="Select Operation:")
        self.label3.grid(row=2, column=0)

        self.operations = [AND(), OR(), XOR(), ShefferStroke()]
        self.selected_operation = tk.StringVar(master)
        self.selected_operation.set(self.operations[0].get_sign())

        self.operation_menu = tk.OptionMenu(master, self.selected_operation, *[op.get_sign() for op in self.operations])
        self.operation_menu.grid(row=2, column=1)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def calculate(self):
        try:
            operand1 = int(self.operand1_entry.get())
            operand2 = int(self.operand2_entry.get())

            selected_op_sign = self.selected_operation.get()
            selected_op = next(op for op in self.operations if op.get_sign() == selected_op_sign)

            result = selected_op.estimate(operand1, operand2)
            self.result_label.config(text=f"{selected_op.get_name()} = {result}")
        except ValueError:
            self.result_label.config(text="Invalid input")


root = tk.Tk()
gui = CalculatorGUI(root)
root.mainloop()