from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageDraw
import file
import converter
import authorWindow
import infoWindow
import pyperclip  # Импортируем для копирования в буфер обмена
import helpWindow


class MainWindow:
    def __init__(self, master):
        self.master = master  # Сохраняем корневое окно
        self.main_window = ctk.CTkToplevel()
        # Создаем меню
        self.menubar = Menu(self.main_window)
        # Добавляем меню "Файл"
        self.filemenu = Menu(self.menubar, tearoff=0, font=("Calibri", 12))

        # Добавляем меню "Информация"
        self.info_nemu = Menu(self.menubar, tearoff=0, font=("Calibri", 12))
        # Добавляем меню "Помощь"
        self.help_menu = Menu(self.menubar, tearoff=0, font=("Calibri", 12))

        # Frame для перевода чисел
        self.frame_calculate = ctk.CTkFrame(self.main_window, fg_color="#F0F8FF")
        # Поле ввода числа
        self.input_label = ctk.CTkLabel(self.frame_calculate, text="Введите число:", bg_color="#F0F8FF")
        self.input_entry = ctk.CTkEntry(self.frame_calculate)

        # Поле вывода результата
        self.output_label = ctk.CTkLabel(self.frame_calculate, text="Результат:", bg_color="#F0F8FF")
        self.output_entry = ctk.CTkEntry(self.frame_calculate, state="readonly")

        # Считывание и форматирование изображения
        self.image_main = Image.open("images/numbers.jpg")
        # Закругляем углы
        self.rounded_image = self.round_image(self.image_main, 60)
        self.photo_main = ctk.CTkImage(light_image=self.rounded_image, dark_image=self.rounded_image,
                                       size=(216, 144))
        # Создание изображения
        self.image_label_main = ctk.CTkLabel(self.frame_calculate, image=self.photo_main, text="")

        # Создаём объект класса File
        self.file = file.File(self.master, self.input_entry, self.output_entry)

        # Создаем список систем счисления
        self.systems = ["Двоичная", "Восьмеричная", "Десятичная", "Шестнадцатеричная"]
        # Создаем переменную для хранения выбранной системы
        self.system_var_input = StringVar(self.main_window)
        # Создаем выпадающий список (combobox)
        self.system_combobox_input = ctk.CTkOptionMenu(
            self.frame_calculate,
            width=165,
            variable=self.system_var_input,
            values=self.systems,
            state="readonly"  # Запрещаем редактирование
        )

        # Создаем переменную для хранения выбранной системы
        self.system_var_output = StringVar(self.main_window)
        # Создаем метку для выбора системы счисления
        self.system_label_input = ctk.CTkLabel(self.frame_calculate,
                                               text="Выберите систему\nсчисления для ввода:", bg_color="#F0F8FF")
        # Создаем метку для выбора системы счисления
        self.system_label_output = ctk.CTkLabel(self.frame_calculate,
                                                text="Выберите систему\nсчисления для вывода:", bg_color="#F0F8FF")

        # Создаем выпадающий список (combobox)
        self.system_combobox_output = ctk.CTkOptionMenu(
            self.frame_calculate,
            width=165,
            variable=self.system_var_output,
            values=self.systems,
            state="readonly"  # Запрещаем редактирование
        )

        # Создаём объект класса Converter
        self.converter = converter.Converter(self.master, self.input_entry,
                                             self.output_entry, self.system_var_input,
                                             self.system_var_output)
        # Frame для кнопок вычислить, копировать и очистить
        self.frame_buttons = ctk.CTkFrame(self.frame_calculate, fg_color="#F0F8FF")
        # Кнопка "Вычислить"
        self.calculate_button = ctk.CTkButton(self.frame_buttons, text="Вычислить",
                                              command=self.converter.converter_num, width=110)
        # Кнопка "Копировать"
        self.copy_button = ctk.CTkButton(self.frame_buttons, text="Копировать",
                                         command=self.copy_to_clipboard, width=110)
        # Кнопка "Очистить"
        self.clear_button = ctk.CTkButton(self.frame_buttons, text="Очистить",
                                          command=self.clear_entry, width=110)
        # Кнопка перестановки
        self.swap_button = ctk.CTkButton(self.frame_buttons, text="Переставить",
                                         command=self.swap_values, width=110)

        self.new_width = 30
        self.new_height = 30
        # Загрузка изображения для всплывающей информации о системах счисления
        self.image_numbers_info = Image.open("images/question.png")
        self.image_numbers_info = self.image_numbers_info.resize((self.new_width, self.new_height))
        self.photo_numbers_info = ctk.CTkImage(self.image_numbers_info)
        # Создаем метку с картинкой
        self.label_image_info = ctk.CTkLabel(self.frame_calculate, text="",
                                             image=self.photo_numbers_info,
                                             bg_color="#F0F8FF")  # Без рамки по умолчанию

        # Frame для кнопок навигации
        self.frame_btn_navigate = ctk.CTkFrame(self.main_window, width=575, height=110)
        # Кнопка "Информация об авторе"
        # Загрузка изображения для кнопки "Информация об авторе"
        self.image_author = Image.open("images/author_button.png")

        self.photo_author = ctk.CTkImage(light_image=self.image_author, dark_image=self.image_author,
                                         size=(30, 30))
        self.author_button = ctk.CTkButton(self.frame_btn_navigate, text="Информация\n    об авторе",
                                           image=self.photo_author, compound="top",  # Текст над изображением
                                           command=self.show_author_info, width=110, height=75)
        # Кнопка "Информация о приложении"
        # Загрузка изображения для кнопки "Информация о приложении"
        self.image_info = Image.open("images/info.png")

        self.photo_info = ctk.CTkImage(light_image=self.image_info, dark_image=self.image_info,
                                       size=(30, 30))
        self.button_info = ctk.CTkButton(self.frame_btn_navigate, text=" Информация\nо приложении",
                                         image=self.photo_info, command=self.show_app_info,
                                         compound="top", width=110, height=75)
        # Кнопка "Помощь"
        # Загрузка изображения для кнопки "Информация о приложении"
        self.image_help = Image.open("images/help.png")

        self.photo_help = ctk.CTkImage(light_image=self.image_help, dark_image=self.image_help,
                                       size=(30, 30))
        self.button_help = ctk.CTkButton(self.frame_btn_navigate, text="Помощь",
                                         image=self.photo_help, command=self.show_theory_info,
                                         compound="top", width=110, height=75)
        # Кнопка "Выход"
        # Загрузка изображения для кнопки "Выход"
        self.image_exit = Image.open("images/exit5.png")

        self.photo_exit = ctk.CTkImage(light_image=self.image_exit, dark_image=self.image_exit,
                                       size=(30, 30))
        self.close_all_button = ctk.CTkButton(self.frame_btn_navigate, text="Выход",
                                              image=self.photo_exit, command=self.close_all_windows,
                                              compound="top", width=110, height=75)

        self.create_main_window()
        self.create_main_frame()
        self.create_frame_navigate()
        self.create_menu()

    def create_main_window(self):
        self.main_window.title("Конвертер чисел и системы счисления")

        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Вычисляем координаты для центрирования окна
        window_width = 640
        window_height = 550
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        # Устанавливаем геометрию окна
        self.main_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_menu(self):
        self.menubar.add_cascade(label="Файл", menu=self.filemenu)
        self.filemenu.add_command(label="Открыть", command=self.file.open_file)
        self.filemenu.add_command(label="Сохранить", command=self.file.save_file)

        self.menubar.add_cascade(label="Информация", menu=self.info_nemu)
        self.info_nemu.add_command(label="Об авторе", command=self.show_author_info)
        self.info_nemu.add_command(label="О приложении", command=self.show_app_info)

        self.menubar.add_cascade(label="Помощь", menu=self.help_menu)
        self.help_menu.add_command(label="Теория", command=self.show_theory_info)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Выход", command=self.close_all_windows)

        # Устанавливаем меню
        self.main_window.config(menu=self.menubar)

    def create_main_frame(self):
        self.frame_calculate.pack(fill="x", padx=25, pady=25)

        self.input_label.grid(column=0, row=0, sticky="w", padx=20)
        self.input_entry.grid(column=0, row=1, sticky="w", padx=20)

        self.output_label.grid(column=0, row=5, sticky="w", padx=20)
        self.output_entry.grid(column=0, row=6, sticky="w", padx=20)

        self.image_label_main.image = self.photo_main  # Чтобы картинка не исчезала
        self.image_label_main.grid(column=2, row=0, rowspan=5, sticky="ew")

        self.system_var_input.set(self.systems[2])  # Устанавливаем начальное значение

        self.system_label_input.grid(column=1, row=0, padx=15)

        self.system_combobox_input.grid(column=1, row=1, padx=15)

        self.system_var_output.set(self.systems[0])  # Устанавливаем начальное значение

        self.system_label_output.grid(column=1, row=5, padx=15)
        self.system_combobox_output.grid(column=1, row=6, padx=15)

        self.frame_buttons.grid(column=0, columnspan=3, row=7,
                                sticky="ew", pady=(50, 5))

        self.calculate_button.grid(column=0, row=0, pady=10, padx=(25, 15))
        self.copy_button.grid(column=1, row=0, pady=5, padx=15)
        self.clear_button.grid(column=2, row=0, pady=5, padx=15)
        self.swap_button.grid(column=3, row=0, padx=(15, 25))

        self.label_image_info.image = self.photo_numbers_info  # Сохраняем ссылку на фото для предотвращения удаления
        self.label_image_info.grid(column=2, row=6, sticky="w", pady=5, padx=5)

        # Добавляем изображение с вопросом и подсказку
        self.add_image_with_tooltip()

    def create_frame_navigate(self):
        self.frame_btn_navigate.pack(fill="x", padx=25, pady=(40, 0))

        self.author_button.image = self.photo_author  # Сохраняем ссылку на объект PhotoImage
        self.author_button.grid(column=0, row=0, padx=(30, 15), pady=10)

        self.button_info.image = self.photo_info
        self.button_info.grid(column=1, row=0, padx=15, pady=10)

        self.button_help.image = self.photo_help
        self.button_help.grid(column=2, row=0, padx=15, pady=10)

        self.close_all_button.image = self.photo_exit
        self.close_all_button.grid(column=3, row=0, pady=10, padx=(15, 20), sticky="e")

    def add_image_with_tooltip(self):
        # Привязываем функции к событиям клика на картинку и наведения курсора
        self.label_image_info.bind("<Enter>", self.on_hover)  # Изменение при наведении
        self.label_image_info.bind("<Leave>", self.on_leave)  # Возвращение к исходному состоянию
        self.label_image_info.bind("<Button-1>", self.show_tooltip)  # Показать всплывающую подсказку при нажатии
        self.label_image_info.bind("<ButtonRelease-1>", self.hide_tooltip)  # Скрыть подсказку при отпускании

        # Переменная для хранения ссылки на всплывающую подсказку
        self.tooltip = None

    def show_tooltip(self, event):
        # Функция для создания всплывающей подсказки

        if self.tooltip:
            self.tooltip.destroy()  # Уничтожаем предыдущую подсказку, если она есть

        self.tooltip = ctk.CTkToplevel(self.main_window)
        self.tooltip.overrideredirect(True)  # Скрываем заголовок окна подсказки
        self.tooltip.geometry(
            "+%s+%s" % (event.x_root + 10, event.y_root + 10))  # Позиционируем подсказку рядом с курсором
        self.tooltip.wm_attributes("-topmost", 1)  # Делаем подсказку самой верхней

        # Добавляем текст в подсказку
        text = ("Система счисления — это способ записи чисел с помощью символов по определённым правилам."
                " Каждая система счисления основана на каком-то основании (или базе), которое определяет"
                " количество символов, используемых для представления чисел. В зависимости"
                " от основания системы, используются разные наборы цифр.")
        text_label = ctk.CTkLabel(self.tooltip, text=text, wraplength=190, bg_color="#D3D3D3")
        text_label.pack()

    def hide_tooltip(self, event):
        # Функция для скрытия подсказки

        if self.tooltip:
            self.tooltip.destroy()  # Уничтожаем всплывающую подсказку

    def on_hover(self, event):
        # Функция для изменения визуального состояния при наведении

        self.label_image_info.configure(cursor="hand2")  # изменение курсора

    def on_leave(self, event):
        # Функция для возврата к исходному состоянию

        self.label_image_info.configure(cursor="")  # курсор по умолчанию

    # Функция для создания изображения с закругленными углами

    def round_image(self, image_main, radius):
        # Конвертируем изображение в формат RGBA (с альфа-каналом для прозрачности)
        image_main = image_main.convert("RGBA")
        width, height = image_main.size

        # Создаем маску с закругленными углами
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=255)

        # Добавляем маску к изображению
        image_main.putalpha(mask)

        return image_main

    def swap_values(self):
        """Меняет местами значения в полях ввода."""

        temp = self.input_entry.get()
        self.input_entry.delete(0, END)
        self.input_entry.insert(0, self.output_entry.get())
        self.output_entry.configure(state="normal")
        self.output_entry.delete(0, END)
        self.output_entry.insert(0, temp)
        self.output_entry.configure(state="readonly")

    def clear_entry(self):
        """Очищает поля ввода и вывода"""

        self.input_entry.delete(0, END)
        self.output_entry.configure(state="normal")
        self.output_entry.delete(0, END)
        self.output_entry.configure(state="readonly")

    def show_theory_info(self):
        """Отображение окна с теоретическим материалом"""

        theory_window = helpWindow.HelpWindow(self.master, self.main_window)

        # Скрытие главного окна
        self.main_window.withdraw()
        theory_window.theory_window.deiconify()

    def show_author_info(self):
        """Отображение информации об авторе"""

        author_window = authorWindow.AuthorWindow(self.master, self.main_window)

        # Скрытие главного окна
        self.main_window.withdraw()
        author_window.author_window.deiconify()

    def show_app_info(self):
        """Отображение информации о приложении"""

        info_window = infoWindow.InfoWindow(self.master, self.main_window)

        # Скрытие главного окна
        self.main_window.withdraw()
        info_window.info_window.deiconify()

    def close_all_windows(self):
        """Закрытие всех окон"""

        self.main_window.destroy()  # Закрываем второе окно
        self.master.destroy()  # Закрываем первое окно

    def copy_to_clipboard(self):
        """Копирование результата перевода в буфер обмена"""

        try:
            pyperclip.copy(self.output_entry.get())
            messagebox.showinfo("Успешно", "Результат скопирован в буфер обмена")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка копирования: {e}")
