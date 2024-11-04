from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
import mainWindow
class InfoWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window

        self.info_window = ctk.CTkToplevel()
        self.info_window.title("Конвертер чисел и системы счисления")

        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Вычисляем координаты для центрирования окна
        window_width = 870
        window_height = 500
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        # Устанавливаем геометрию окна
        self.info_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Название темы
        self.label_theme = ctk.CTkLabel(self.info_window, text="Конвертер чисел и системы счисления",
                                        font=("Calibri", 24, "bold"))
        self.label_theme.place(x=150, y=20)

        # Frame для текста
        self.frame_text = ctk.CTkFrame(self.info_window)
        self.frame_text.place(x=450, y=60)

        # Считывание и форматирование изображения
        self.info_image = Image.open("images/adfs.png")
        # Закругляем углы
        self.rounded_image = mainWindow.MainWindow.round_image(self=main_window, image_main=self.info_image, radius=30)
        self.photo_info = ctk.CTkImage(light_image=self.rounded_image, dark_image=self.rounded_image,
                                       size=(424, 350))

        # Создание изображения
        self.image_label = ctk.CTkLabel(self.info_window, image=self.photo_info, text="")
        self.image_label.image = self.photo_info  # Чтобы картинка не исчезала
        self.image_label.place(x=20, y=60)

        # Информация о функционале приложения
        self.label_info = ctk.CTkLabel(self.frame_text, font=("Calibri", 22, "bold"),
                                       text="Программа позволяет")
        self.label_info.grid(row=0, column=0, pady=10)
        self.label_info2 = ctk.CTkLabel(self.frame_text, font=("Calibri", 20),
                                        justify="left",
                                        text="1.Выбирать систему счисления для\nввода/вывода числа")
        self.label_info2.grid(row=1, column=0, sticky="w")
        self.label_info3 = ctk.CTkLabel(self.frame_text, font=("Calibri", 20),
                                        justify="left",
                                        text="2.Выполнять перевод числа между системами\nсчисления")
        self.label_info3.grid(row=2, column=0, sticky="w")
        self.label_info4 = ctk.CTkLabel(self.frame_text, font=("Calibri", 20),
                                        justify="left",
                                        text="3.Сохранять результат перевода в файл")
        self.label_info4.grid(row=3, column=0, sticky="w")
        self.label_info5 = ctk.CTkLabel(self.frame_text, font=("Calibri", 20),
                                        justify="left",
                                        text="4.Считывать данные из файла в поле\nввода числа")
        self.label_info5.grid(row=4, column=0, sticky="w")
        self.label_info6 = ctk.CTkLabel(self.frame_text, font=("Calibri", 20),
                                        justify="left",
                                        text="5.Копировать результат перевода числа в\nбуфер обмена")
        self.label_info6.grid(row=5, column=0, sticky="w")
        self.label_info7 = ctk.CTkLabel(self.frame_text, font=("Calibri", 20),
                                        justify="left",
                                        text="6.Очищать поля ввода и вывода")
        self.label_info7.grid(row=6, column=0, sticky="w")
        self.label_info8 = ctk.CTkLabel(self.frame_text, font=("Calibri", 20),
                                        justify="left",
                                        text="7.Менять местами числа из полей ввода \nи вывода")
        self.label_info8.grid(row=7, column=0, sticky="w")

        # Кнопка возвращения назад к главному окну
        self.back_button = ctk.CTkButton(self.info_window, text="Назад",
                                      command=self.clicked_back_button)
        self.back_button.place(x=660, y=450)

    def clicked_back_button(self):
        """Возвращение назад к главнмоу окну"""

        self.info_window.withdraw()
        self.main_window.deiconify()
