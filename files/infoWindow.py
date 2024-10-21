from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class InfoWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window

        self.info_window = Toplevel()
        self.master.title("Конвертер чисел и системы счисления")

        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Вычисляем координаты для центрирования окна
        window_width = 1000
        window_height = 500
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        # Устанавливаем геометрию окна
        self.info_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Название темы
        self.label_theme = ttk.Label(self.info_window, text="Конвертер чисел и системы счисления",
                                     font=("Arial", 18))
        self.label_theme.place(x=150, y=20)

        # Frame для изображения
        self.frame_image = Frame(self.info_window, borderwidth=2, relief="sunken")
        self.frame_image.place(x=20, y=60, height=380)

        # Frame для текста
        self.frame_text = Frame(self.info_window, borderwidth=2, relief="sunken")
        self.frame_text.place(x=450, y=60, width=530, height=380)

        # Считывание и форматирование изображения
        self.info_image = Image.open("images/adfs.png")
        new_width = int(self.info_image.width / 2)  # Уменьшаем ширину в 4 раза
        new_height = int(self.info_image.height / 2)  # Уменьшаем высоту в 4 раза
        self.info_image_resized = self.info_image.resize((new_width, new_height))
        self.photo_info = ImageTk.PhotoImage(self.info_image_resized)

        # Создание изображения
        self.image_label = ttk.Label(self.frame_image, image=self.photo_info)
        self.image_label.image = self.photo_info  # Чтобы картинка не исчезала
        self.image_label.pack(pady=10)

        # Информация о функционале приложения
        self.label_info = Label(self.frame_text, font=("Calibri", 18),
                                text="Программа позволяет")
        self.label_info.grid(row=0, column=0)
        self.label_info2 = Label(self.frame_text, font=("Calibri", 18),
                                 justify="left",
                                 text="1.Выбирать систему счисления для ввода/вывода\n числа")
        self.label_info2.grid(row=1, column=0, sticky="w")
        self.label_info3 = Label(self.frame_text, font=("Calibri", 18),
                                 justify="left",
                                 text="2.Выполнять перевод числа между системами\n счисления")
        self.label_info3.grid(row=2, column=0, sticky="w")
        self.label_info4 = Label(self.frame_text, font=("Calibri", 18),
                                 text="3.Сохранять результат перевода в файл")
        self.label_info4.grid(row=3, column=0, sticky="w")
        self.label_info5 = Label(self.frame_text, font=("Calibri", 18),
                                 justify="left",
                                 text="4.Считывать данные из файла в поле ввода числа")
        self.label_info5.grid(row=4, column=0, sticky="w")
        self.label_info6 = Label(self.frame_text, font=("Calibri", 18),
                                 justify="left",
                                 text="5.Копировать результат перевода числа в буфер\n обмена")
        self.label_info6.grid(row=5, column=0, sticky="w")
        self.label_info7 = Label(self.frame_text, font=("Calibri", 18),
                                 text="6.Очищать поля ввода и вывода")
        self.label_info7.grid(row=6, column=0, sticky="w")
        self.label_info8 = Label(self.frame_text, font=("Calibri", 18),
                                 text="7.Менять местами числа из полей ввода и вывода")
        self.label_info8.grid(row=7, column=0, sticky="w")

        # Создаем объект стиля
        self.style_buttons = ttk.Style()
        # Задаем стили для кнопки
        self.style_buttons.configure("back.TButton", font=("Calibri", 10), padding=(15, 3))

        # Кнопка возвращения назад к главному окну
        self.back_button = ttk.Button(self.info_window, text="Назад", style="back.TButton",
                                      command=self.clicked_back_button)
        self.back_button.place(x=830, y=450)

    def clicked_back_button(self):
        """Возвращение назад к главнмоу окну"""

        self.info_window.withdraw()
        self.main_window.deiconify()
