from tkinter import *
from tkinter import ttk
import customtkinter as ctk


class TheoryWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window

        self.theory_window = ctk.CTkToplevel()
        self.theory_window.title("Конвертер чисел и системы счисления")

        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Вычисляем координаты для центрирования окна
        window_width = 800
        window_height = 670
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Устанавливаем геометрию окна
        self.theory_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Основной Frame для размещения текста
        self.main_frame = ctk.CTkFrame(self.theory_window, corner_radius=15)
        self.main_frame.pack(padx=10, pady=10, fill="x", expand=True)

        # Оформление заголовков и текста
        header_font = ("Arial", 18, "bold")
        body_font = ("Arial", 16)

        # Заголовок
        ctk.CTkLabel(self.main_frame, text="Виды систем счисления:",
              font=("Arial", 22, "bold")).pack(anchor="w", padx=30, pady=10)

        # Десятичная система
        ctk.CTkLabel(self.main_frame, text="1. Десятичная система (основание 10)",
              font=header_font).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(self.main_frame, text=(
            "Десятичная система — это наиболее привычная для нас система счисления. Она "
            "использует десять цифр: 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9. "
            "Число в десятичной системе представляется как сумма произведений цифр"
            " на соответствующие степени числа 10.\n"
            "Например, число 345 можно записать как: 3 × 10² + 4 × 10¹ + 5 × 10⁰ = 300 + 40 + 5."
        ), font=body_font, wraplength=750).pack(anchor="w", padx=20, pady=5)

        # Двоичная система
        ctk.CTkLabel(self.main_frame, text="2. Двоичная система (основание 2)",
              font=header_font).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(self.main_frame, text=(
            "Двоичная система используется в компьютерной технике."
            " Она состоит только из двух цифр: 0 и 1. "
            "Число в двоичной системе представляется как сумма произведений"
            " цифр на соответствующие степени числа 2.\n"
            "Например, число 1011 в двоичной системе:"
            " 1 × 2³ + 0 × 2² + 1 × 2¹ + 1 × 2⁰ = 8 + 0 + 2 + 1 = 11 в десятичной системе."
        ), font=body_font, wraplength=750).pack(anchor="w", padx=20, pady=5)

        # Шестнадцатеричная система
        ctk.CTkLabel(self.main_frame, text="3. Шестнадцатеричная система (основание 16)",
              font=header_font).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(self.main_frame, text=(
            "Шестнадцатеричная система используется для сокращённого представления"
            " больших двоичных чисел. В этой системе, кроме цифр от 0 до 9, используются буквы A, B, C, D, E, F, "
            "которые представляют значения от 10 до 15. Например, число 2F в шестнадцатеричной"
            " системе можно представить как: 2 × 16¹ + 15 × 16⁰ = 32 + 15 = 47 в десятичной системе."
        ), font=body_font, wraplength=750).pack(anchor="w", padx=20, pady=5)

        # Восьмеричная система
        ctk.CTkLabel(self.main_frame, text="4. Восьмеричная система (основание 8)",
              font=header_font).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(self.main_frame, text=(
            "В восьмеричной системе используются цифры от 0 до 7. Эта система"
            " использовалась в ранней вычислительной технике, "
            "так как она является кратной двоичной системе (каждая цифра"
            " восьмеричной системы соответствует трём битам двоичной). "
            "Например, число 127 в восьмеричной системе эквивалентно 87 в десятичной."
        ), font=body_font, wraplength=750).pack(anchor="w", padx=20, pady=5)

        # Кнопка закрытия окна
        close_button = ctk.CTkButton(self.theory_window, text="Назад",
                                  command=self.back_button_clicked)
        close_button.pack(side=RIGHT, pady=15, padx=30)

    def back_button_clicked(self):
        """Возвращение назад к главнмоу окну"""

        self.theory_window.withdraw()
        self.main_window.deiconify()
