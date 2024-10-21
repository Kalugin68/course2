import tkinter as tk
import tkinter
from tkinter import messagebox


class CalculateNumbers:
    def __init__(self, root, input_entry, output_entry, system_var_input, system_var_output):
        self.root = root
        self.input_entry = input_entry
        self.output_entry = output_entry

        # Определение system_var_input и system_var_output
        self.system_var_input = system_var_input
        self.system_var_output = system_var_output

    def calculate_num(self):
        """Функция для вычисления конвертации"""

        try:
            # Получаем число из поля ввода
            input_value = self.input_entry.get()

            # Получаем выбранные системы счисления
            input_system = self.system_var_input.get()
            output_system = self.system_var_output.get()

            # Проверяем, что система счисления для ввода выбрана
            if input_system == "Выберите систему счисления для ввода:":
                tkinter.messagebox.showerror("Ошибка", "Выберите систему счисления для ввода!")
                return

            # Проверка на отрицательные числа
            if input_value.startswith('-'):
                tkinter.messagebox.showerror("Ошибка", "Система счисления не поддерживает отрицательные числа!")
                return

                # Проверяем соответствие числа выбранной системе счисления
            if input_system == "Двоичная":
                if not all(digit in "01" for digit in input_value):
                    tkinter.messagebox.showerror("Ошибка",
                                                 "Число не соответствует двоичной системе счисления!")
                    return

            elif input_system == "Восьмеричная":
                if not all(digit in "01234567" for digit in input_value):
                    tkinter.messagebox.showerror("Ошибка",
                                                 "Число не соответствует восьмеричной системе счисления!")
                    return
            elif input_system == "Шестнадцатеричная":
                if not all(digit in "0123456789ABCDEF" for digit in input_value.upper()):
                    tkinter.messagebox.showerror("Ошибка",
                                                 "Число не соответствует шестнадцатеричной системе счисления!")
                    return

            # Преобразуем число в десятичную систему
            decimal_number = 0  # Значение по умолчанию
            power = 0
            if input_system == "Двоичная":
                for digit in input_value[::-1]:
                    if digit == "1":
                        decimal_number += 2 ** power
                    power += 1

            elif input_system == "Восьмеричная":
                for digit in input_value[::-1]:
                    decimal_number += int(digit) * 8 ** power
                    power += 1

            elif input_system == "Десятичная":
                decimal_number = int(input_value)

            elif input_system == "Шестнадцатеричная":
                for digit in input_value[::-1]:
                    if digit.isdigit():
                        decimal_number += int(digit) * 16 ** power
                    else:
                        decimal_number += (ord(digit.upper()) - ord('A') + 10) * 16 ** power
                    power += 1

            conversion_result = ""
            # Преобразуем число в соответствующую систему счисления
            if output_system == "Двоичная":
                while decimal_number > 0:
                    remainder = decimal_number % 2
                    conversion_result = str(remainder) + conversion_result
                    decimal_number //= 2

            elif output_system == "Восьмеричная":
                while decimal_number > 0:
                    remainder = decimal_number % 8
                    conversion_result = str(remainder) + conversion_result
                    decimal_number //= 8

            elif output_system == "Десятичная":
                conversion_result = str(decimal_number)

            elif output_system == "Шестнадцатеричная":
                while decimal_number > 0:
                    remainder = decimal_number % 16
                    if remainder < 10:
                        conversion_result = str(remainder) + conversion_result
                    else:
                        conversion_result = chr(ord('A') + remainder - 10) + conversion_result
                    decimal_number //= 16

            else:
                raise ValueError

            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, conversion_result)  # Now using conversion_result
            self.output_entry.config(state="readonly")
        except ValueError:
            tkinter.messagebox.showerror("Ошибка", "Некорректный ввод или система счисления")
