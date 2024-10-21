from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import funcFile
import calculate
import authorWindow
import infoWindow
import pyperclip  # Импортируем для копирования в буфер обмена
import theoryWindow


class MainWindow:
    def __init__(self, master):
        self.master = master  # Сохраняем корневое окно

        self.main_window = Toplevel()
        self.main_window.title("Конвертер чисел и системы счисления")

        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Вычисляем координаты для центрирования окна
        window_width = 600
        window_height = 550
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        # Устанавливаем геометрию окна
        self.main_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Frame для перевода чисел
        self.frame_calculate = Frame(self.main_window, borderwidth=1, relief="sunken", bg="#F0F8FF")
        self.frame_calculate.pack(fill="x", padx=25, pady=25)

        # Frame для кнопок навигации
        self.frame_btn_navigate = Frame(self.main_window)
        self.frame_btn_navigate.place(x=15, y=430, width=575, height=110)

        # Поле ввода числа
        self.input_label = Label(self.frame_calculate, text="Введите число:", bg="#F0F8FF")
        self.input_label.grid(column=0, row=0, sticky="w", padx=20)
        self.input_entry = ttk.Entry(self.frame_calculate, width=20)
        self.input_entry.grid(column=0, row=1, sticky="w", padx=20)

        # Поле вывода результата
        self.output_label = Label(self.frame_calculate, text="Результат:", bg="#F0F8FF")
        self.output_label.grid(column=0, row=5, sticky="w", padx=20)
        self.output_entry = ttk.Entry(self.frame_calculate, width=20, state="readonly")
        self.output_entry.grid(column=0, row=6, sticky="w", padx=20)

        # Считывание и форматирование изображения
        self.image_main = Image.open("images/numbers.jpg")
        new_width = int(self.image_main.width / 8.5)
        new_height = int(self.image_main.height / 10)
        self.resized_image_main = self.image_main.resize((new_width, new_height))
        self.photo_main = ImageTk.PhotoImage(self.resized_image_main)

        # Создание изображения
        self.image_label_main = ttk.Label(self.frame_calculate, image=self.photo_main)
        self.image_label_main.image = self.photo_main  # Чтобы картинка не исчезала
        self.image_label_main.grid(column=2, row=0, rowspan=5, sticky="e")

        # Создаём объект класса MyFunctions
        self.my_functions = funcFile.MyFunctions(self.master, self.input_entry, self.output_entry)

        # Создаем меню
        self.menubar = Menu(self.main_window)

        # Добавляем меню "Файл"
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Файл", menu=self.filemenu)
        self.filemenu.add_command(label="Открыть", command=self.my_functions.open_file)
        self.filemenu.add_command(label="Сохранить", command=self.my_functions.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Выход")

        # Добавляем меню "Информация"
        self.info_nemu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Информация", menu=self.info_nemu)
        self.info_nemu.add_command(label="Об авторе", command=self.show_author_info)
        self.info_nemu.add_command(label="О приложении", command=self.show_app_info)
        self.info_nemu.add_separator()
        self.info_nemu.add_command(label="Выход")

        # Добавляем меню "Помощь"
        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Помощь", menu=self.help_menu)
        self.help_menu.add_command(label="Теория", command=self.show_theory_info)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Выход")

        # Устанавливаем меню
        self.main_window.config(menu=self.menubar)

        # Создаем список систем счисления
        self.systems = ["Двоичная", "Восьмеричная", "Десятичная", "Шестнадцатеричная"]
        # Создаем переменную для хранения выбранной системы
        self.system_var_input = StringVar(self.main_window)
        self.system_var_input.set(self.systems[2])  # Устанавливаем начальное значение
        # Создаем метку для выбора системы счисления
        self.system_label = Label(self.frame_calculate,
                                  text="Выберите систему\nсчисления для ввода:", bg="#F0F8FF")
        self.system_label.grid(column=1, row=0, padx=15)

        # Создаем выпадающий список (combobox)
        self.system_combobox_input = ttk.Combobox(
            self.frame_calculate,
            textvariable=self.system_var_input,
            values=self.systems,
            state="readonly"  # Запрещаем редактирование
        )
        self.system_combobox_input.grid(column=1, row=1, padx=15)

        # Создаем переменную для хранения выбранной системы
        self.system_var_output = StringVar(self.main_window)
        self.system_var_output.set(self.systems[0])  # Устанавливаем начальное значение
        # Создаем метку для выбора системы счисления
        self.system_label = Label(self.frame_calculate,
                                  text="Выберите систему\nсчисления для вывода:", bg="#F0F8FF")
        self.system_label.grid(column=1, row=5, padx=15)

        # Создаем выпадающий список (combobox)
        self.system_combobox_output = ttk.Combobox(
            self.frame_calculate,
            textvariable=self.system_var_output,
            values=self.systems,
            state="readonly"  # Запрещаем редактирование
        )
        self.system_combobox_output.grid(column=1, row=6, padx=15)

        # Создаём объект класса CalculateNumbers
        self.calculate = calculate.CalculateNumbers(self.master, self.input_entry,
                                                    self.output_entry, self.system_var_input,
                                                    self.system_var_output)

        # Frame для кнопок вычислить, копировать и очистить
        self.frame_buttons = Frame(self.frame_calculate, bg="#D3D3D3",
                                   borderwidth=1, relief="sunken")
        self.frame_buttons.grid(column=0, columnspan=3, row=7,
                                sticky="ew", pady=(50, 0))

        # Создаем объект стиля
        self.style_buttons = ttk.Style()
        # Задаем стили для кнопки
        self.style_buttons.configure("btn.TButton", font=("Calibri", 10),
                                     padding=(10, 3), background="#D3D3D3")

        # Кнопка "Вычислить"
        self.calculate_button = ttk.Button(self.frame_buttons,
                                           text="Вычислить",
                                           style="btn.TButton",
                                           command=self.calculate.calculate_num)
        self.calculate_button.grid(column=0, row=0, pady=10, padx=15)

        # Кнопка "Копировать"
        self.copy_button = ttk.Button(self.frame_buttons,
                                      text="Копировать", style="btn.TButton", command=self.copy_to_clipboard)
        self.copy_button.grid(column=1, row=0, pady=5, padx=15)

        # Кнопка "Очистить"
        self.clear_button = ttk.Button(self.frame_buttons,
                                       text="Очистить", style="btn.TButton", command=self.clear_entry)
        self.clear_button.grid(column=2, row=0, pady=5, padx=15)

        # Кнопка перестановки
        self.swap_button = ttk.Button(self.frame_buttons, text="Переставить",
                                      style="btn.TButton", command=self.swap_values)
        self.swap_button.grid(column=3, row=0, padx=15)

        # Создаем объект стиля
        self.style_buttons_navigate = ttk.Style()
        self.style_buttons_navigate.configure("navigate.TButton", font=("Calibri", 10))
        # Кнопка "Информация об авторе"
        # Загрузка изображения для кнопки "Информация об авторе"
        self.image_author = Image.open("images/author_button.png")
        new_width = int(self.image_author.width / 11)  # Уменьшаем ширину в 4 раза
        new_height = int(self.image_author.height / 11)  # Уменьшаем высоту в 4 раза
        self.image_author_resized = self.image_author.resize((new_width, new_height))

        self.photo_author = ImageTk.PhotoImage(self.image_author_resized)
        self.author_button = ttk.Button(self.frame_btn_navigate, text="Информация\n    об авторе",
                                        image=self.photo_author,
                                        style="navigate.TButton",
                                        compound="top",  # Текст над изображением
                                        command=self.show_author_info)
        self.author_button.image = self.photo_author  # Сохраняем ссылку на объект PhotoImage
        self.author_button.grid(column=0, row=0, padx=25, pady=10)

        # Кнопка "Информация о приложении"
        # Загрузка изображения для кнопки "Информация о приложении"
        self.image_info = Image.open("images/info.png")
        new_width_info = int(self.image_info.width / 20)  # Уменьшаем ширину в 4 раза
        new_height_info = int(self.image_info.height / 20)  # Уменьшаем высоту в 4 раза
        self.image_info_resized = self.image_info.resize((new_width_info, new_height_info))

        self.photo_info = ImageTk.PhotoImage(self.image_info_resized)
        self.button_info = ttk.Button(self.frame_btn_navigate, text=" Информация\nо приложении",
                                      image=self.photo_info,
                                      style="navigate.TButton",
                                      command=self.show_app_info,
                                      compound="top")
        self.button_info.image = self.photo_info
        self.button_info.grid(column=1, row=0, padx=25, pady=10)

        # Кнопка "Помощь"
        # Загрузка изображения для кнопки "Информация о приложении"
        self.image_help = Image.open("images/help.png")
        new_width_info = int(self.image_help.width / 11)  # Уменьшаем ширину в 4 раза
        new_height_info = int(self.image_help.height / 11)  # Уменьшаем высоту в 4 раза
        self.image_help_resized = self.image_help.resize((new_width_info, new_height_info))

        self.photo_help = ImageTk.PhotoImage(self.image_help_resized)
        self.button_help = ttk.Button(self.frame_btn_navigate, text="Помощь",
                                      image=self.photo_help,
                                      style="navigate.TButton",
                                      command=self.show_theory_info,
                                      compound="top")
        self.button_help.image = self.photo_help
        self.button_help.grid(column=2, row=0, padx=25, pady=10)

        # Кнопка "Выход"
        # Загрузка изображения для кнопки "Выход"
        self.image_exit = Image.open("images/exit5.png")
        new_width_exit = int(self.image_exit.width / 14)  # Уменьшаем ширину в 4 раза
        new_height_exit = int(self.image_exit.height / 14)  # Уменьшаем высоту в 4 раза
        self.image_exit_resized = self.image_exit.resize((new_width_exit, new_height_exit))

        self.photo_exit = ImageTk.PhotoImage(self.image_exit_resized)
        self.close_all_button = ttk.Button(self.frame_btn_navigate, text="Выход",
                                           image=self.photo_exit,
                                           style="navigate.TButton",
                                           command=self.close_all_windows,
                                           compound="top")
        self.close_all_button.image = self.photo_exit
        self.close_all_button.grid(column=3, row=0, pady=10, padx=25, sticky="e")

        # Загрузка изображения для всплывающей информации о системах счисления
        self.image_numbers_info = Image.open("images/question.png")
        new_width = 30
        new_height = 30
        self.image_numbers_info = self.image_numbers_info.resize((new_width, new_height))
        self.photo_numbers_info = ImageTk.PhotoImage(self.image_numbers_info)

        # Создаем метку с картинкой
        self.label_image_info = Label(self.frame_calculate,
                                      image=self.photo_numbers_info,
                                      bg="#F0F8FF", borderwidth=0)  # Без рамки по умолчанию
        self.label_image_info.image = self.photo_numbers_info  # Сохраняем ссылку на фото для предотвращения удаления
        self.label_image_info.grid(column=2, row=6, sticky="w", pady=5, padx=5)

        # Добавляем изображение с вопросом и подсказку
        self.add_image_with_tooltip()

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

        self.tooltip = Toplevel(self.main_window)
        self.tooltip.overrideredirect(True)  # Скрываем заголовок окна подсказки
        self.tooltip.geometry(
            "+%s+%s" % (event.x_root + 10, event.y_root + 10))  # Позиционируем подсказку рядом с курсором
        self.tooltip.wm_attributes("-topmost", 1)  # Делаем подсказку самой верхней

        # Добавляем текст в подсказку
        text = ("Система счисления — это способ записи чисел с помощью символов по определённым правилам."
                " Каждая система счисления основана на каком-то основании (или базе), которое определяет"
                " количество символов, используемых для представления чисел. В зависимости"
                " от основания системы, используются разные наборы цифр.")
        text_label = Label(self.tooltip, text=text, wraplength=190, bg="#D3D3D3")
        text_label.pack()

    def hide_tooltip(self, event):
        # Функция для скрытия подсказки

        if self.tooltip:
            self.tooltip.destroy()  # Уничтожаем всплывающую подсказку

    def on_hover(self, event):
        # Функция для изменения визуального состояния при наведении

        self.label_image_info.config(cursor="hand2")  # изменение курсора

    def on_leave(self, event):
        # Функция для возврата к исходному состоянию

        self.label_image_info.config(cursor="")  # курсор по умолчанию
    def swap_values(self):
        """Меняет местами значения в полях ввода."""

        temp = self.input_entry.get()
        self.input_entry.delete(0, END)
        self.input_entry.insert(0, self.output_entry.get())
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, END)
        self.output_entry.insert(0, temp)
        self.output_entry.config(state="readonly")

    def clear_entry(self):
        """Очищает поля ввода и вывода"""

        self.input_entry.delete(0, END)
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, END)
        self.output_entry.config(state="readonly")

    def show_theory_info(self):
        """Отображение окна с теоретическим материалом"""

        theory_window = theoryWindow.TheoryWindow(self.master, self.main_window)

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
