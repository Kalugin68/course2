import customtkinter as ctk
from PIL import Image
from mainWindow import MainWindow
from tkinter import PhotoImage


class SplashScreen:
    def __init__(self):
        ctk.set_appearance_mode("system")  # Устанавливаем темную/светлую тему в зависимости от системы
        ctk.set_default_color_theme("blue")  # Цветовая схема

        self.master = ctk.CTk()
        self.master.title("Конвертер чисел и системы счисления")

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Вычисляем координаты для центрирования окна
        window_width = 550
        window_height = 505
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        # Загружаем иконку в формате PNG
        self.icon = PhotoImage(file="images/converter.png")  # Убедитесь, что файл существует и указан путь
        self.master.iconphoto(True, self.icon)  # Устанавливаем иконку для главного окна
        # Устанавливаем иконку формата .ico
        self.master.iconbitmap("images/icon.ico")  # Укажите путь к вашему файлу .ico
        # Устанавливаем геометрию окна
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Заголовок
        self.header_label = ctk.CTkLabel(self.master, text="Белорусский национальный технический университет",
                                         font=("Arial", 18, "bold"))
        self.header_label.grid(column=0, columnspan=2, row=0, pady=10, padx=40)

        # Факультет и кафедра
        self.faculty_label = ctk.CTkLabel(self.master, text="Факультет информационных технологий и робототехники",
                                          font=("Arial", 12))
        self.faculty_label.grid(column=0, columnspan=2, row=1)
        self.department_label = ctk.CTkLabel(self.master,
                                             text="Кафедра программного обеспечения информационных систем и технологий",
                                             font=("Arial", 12))
        self.department_label.grid(column=0, columnspan=2, row=2)

        # Заголовок курсовой работы
        self.title_label = ctk.CTkLabel(self.master, text="Курсовой проект", font=("Arial", 20, "bold"))
        self.title_label.grid(column=0, columnspan=2, row=3, pady=20)

        # Название работы
        self.discipline_label = ctk.CTkLabel(self.master, text="по дисциплине Языки программирования",
                                             font=("Arial", 14))
        self.discipline_label.grid(column=0, columnspan=2, row=4)
        self.project_label = ctk.CTkLabel(self.master, text="Конвертер чисел и системы счисления",
                                          font=("Arial", 20, "bold"))
        self.project_label.grid(column=0, columnspan=2, row=5, pady=10)

        # Рисунок
        self.image = Image.open("images/code.jpg")

        # Используем CTkImage для отображения изображения
        self.photo = ctk.CTkImage(light_image=self.image, dark_image=self.image,
                                  size=(240, 160))

        # Изображение
        self.image_label = ctk.CTkLabel(self.master, image=self.photo, text="")
        self.image_label.image = self.photo  # Чтобы картинка не исчезала
        self.image_label.grid(column=0, row=6, rowspan=2, padx=(15, 0))

        # Автор и преподаватель
        self.author_label = ctk.CTkLabel(self.master,
                                         text="Выполнил: Студент группы 10701223\nКалугин Александр Андреевич",
                                         font=ctk.CTkFont(size=12))
        self.author_label.grid(column=1, row=6, sticky="w")
        self.teacher_label = ctk.CTkLabel(self.master,
                                          text="Преподаватель: к.ф.-м.н., доц.\nСидорик Валерий Владимирович",
                                          font=ctk.CTkFont(size=12))
        self.teacher_label.grid(column=1, row=7, sticky="w")

        # Год и место
        self.place_label = ctk.CTkLabel(self.master, text="Минск 2024", font=ctk.CTkFont(size=12))
        self.place_label.grid(column=0, columnspan=2, row=8, pady=10)

        # Frame для кнопок навигации
        self.button_frame = ctk.CTkFrame(self.master)
        self.button_frame.grid(column=0, columnspan=2, row=9, sticky="nsew")

        # Настройка столбцов в button_frame
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        # Кнопка "Далее"
        self.next_button = ctk.CTkButton(self.button_frame, text="Далее", width=120, command=self.next_button_clicked)
        self.next_button.grid(column=0, row=0, sticky="e", padx=20, pady=10)

        # Кнопка "Выход"
        self.exit_button = ctk.CTkButton(self.button_frame, text="Выход", width=120, command=self.master.destroy)
        self.exit_button.grid(column=1, row=0, sticky="w", padx=20, pady=10)

        # Запускаем таймер для первого окна
        self.timer_id = self.master.after(60000, self.master.destroy)

    def next_button_clicked(self):
        """Открытие главного окна приложения"""
        main_window = MainWindow(self.master)
        # Отменяем таймер
        self.master.after_cancel(self.timer_id)

        # Скрытие первого окна
        self.master.withdraw()
        main_window.main_window.deiconify()


def main():
    first_window = SplashScreen()
    first_window.master.mainloop()


main()
