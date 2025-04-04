import tkinter
from tkinter import messagebox
import customtkinter as ctk


class Converter:
    def __init__(self, root, input_entry, output_entry, system_var_input, system_var_output):
        self.root = root
        self.input_entry = input_entry
        self.output_entry = output_entry

        # Определение system_var_input и system_var_output
        self.system_var_input = system_var_input
        self.system_var_output = system_var_output

    def converter_num(self):
        """Функция для вычисления конвертации"""

        self.conversion_result = ""
        # Преобразуем число в десятичную систему
        self.decimal_number = 0  # Значение по умолчанию
        self.power = 0

        # Получаем число из поля ввода
        self.input_value = self.input_entry.get()
        # Получаем выбранные системы счисления
        self.input_system = self.system_var_input.get()
        self.output_system = self.system_var_output.get()

        try:
            if (self.check_correct_notation()):
                self.convert_to_decimal()  # Конвертация в десятичную систему

                self.convert_to_result()  # Конвертация из десятичной в целевую систему

                self.print_result()

        except ValueError:
            tkinter.messagebox.showerror("Ошибка", "Некорректный ввод или система счисления")

    def convert_to_decimal(self):
        """Преобразует число из выбранной системы счисления в десятичную."""
        if self.input_system == "Двоичная":
            self.bin_to_decimal()

        elif self.input_system == "Восьмеричная":
            self.oct_to_decimal()

        elif self.input_system == "Десятичная":
            self.decimal_number = int(self.input_value)

        elif self.input_system == "Шестнадцатеричная":
            self.hex_to_decimal()

    def convert_to_result(self):
        """Преобразует десятичное число в целевую систему счисления."""
        if self.output_system == "Двоичная":
            self.decimal_to_bin()

        elif self.output_system == "Восьмеричная":
            self.decimal_to_oct()

        elif self.output_system == "Десятичная":
            self.conversion_result = str(self.decimal_number)

        elif self.output_system == "Шестнадцатеричная":
            self.decimal_to_hex()

        else:
            raise ValueError("Некорректная целевая система счисления")

    def bin_to_decimal(self):
        for digit in self.input_value[::-1]:
            if digit == "1":
                self.decimal_number += 2 ** self.power
            self.power += 1

    def oct_to_decimal(self):
        for digit in self.input_value[::-1]:
            self.decimal_number += int(digit) * 8 ** self.power
            self.power += 1

    def hex_to_decimal(self):
        for digit in self.input_value[::-1]:
            if digit.isdigit():
                self.decimal_number += int(digit) * 16 ** self.power
            else:
                self.decimal_number += (ord(digit.upper()) - ord('A') + 10) * 16 ** self.power
            self.power += 1

    def decimal_to_bin(self):
        while self.decimal_number > 0:
            remainder = self.decimal_number % 2
            self.conversion_result = str(remainder) + self.conversion_result
            self.decimal_number //= 2

    def decimal_to_oct(self):
        while self.decimal_number > 0:
            remainder = self.decimal_number % 8
            self.conversion_result = str(remainder) + self.conversion_result
            self.decimal_number //= 8

    def decimal_to_hex(self):
        while self.decimal_number > 0:
            remainder = self.decimal_number % 16
            if remainder < 10:
                self.conversion_result = str(remainder) + self.conversion_result
            else:
                self.conversion_result = chr(ord('A') + remainder - 10) + self.conversion_result
            self.decimal_number //= 16

    def print_result(self):
        self.output_entry.configure(state="normal")
        self.output_entry.delete(0, ctk.END)
        self.output_entry.insert(0, self.conversion_result)
        self.output_entry.configure(state="readonly")

    def check_correct_notation(self):
        # Проверка на отрицательные числа
        if self.input_value.startswith('-'):
            tkinter.messagebox.showerror("Ошибка", "Система счисления не поддерживает отрицательные числа!")
            return False

        # Проверяем, что система счисления для ввода выбрана
        if self.input_system == "Выберите систему счисления для ввода:":
            tkinter.messagebox.showerror("Ошибка", "Выберите систему счисления для ввода!")
            return False

            # Проверяем соответствие числа выбранной системе счисления
        if self.input_system == "Двоичная":
            if not all(digit in "01" for digit in self.input_value):
                tkinter.messagebox.showerror("Ошибка",
                                             "Число не соответствует двоичной системе счисления!")
                return False

        elif self.input_system == "Восьмеричная":
            if not all(digit in "01234567" for digit in self.input_value):
                tkinter.messagebox.showerror("Ошибка",
                                             "Число не соответствует восьмеричной системе счисления!")
                return False
        elif self.input_system == "Шестнадцатеричная":
            if not all(digit in "0123456789ABCDEF" for digit in self.input_value.upper()):
                tkinter.messagebox.showerror("Ошибка",
                                             "Число не соответствует шестнадцатеричной системе счисления!")
                return False

        return True
