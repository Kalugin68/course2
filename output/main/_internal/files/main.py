from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Импортируем библиотеку PIL для работы с изображениями
from mainWindow import MainWindow


class FirstWindow:
    def __init__(self):
        self.master = Tk()
        self.master.title("Конвертер чисел и системы счисления")

        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Вычисляем координаты для центрирования окна
        window_width = 600
        window_height = 530
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        # Устанавливаем геометрию окна
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Загружаем изображение для иконки (в формате ICO) через Pillow
        icon_image = Image.open("images/icon.ico")  # Укажите правильный путь к вашему ICO-файлу
        icon_photo = ImageTk.PhotoImage(icon_image)  # type: ignore

        # Устанавливаем иконку окна
        self.master.iconphoto(True, icon_photo)

        # Заголовок
        self.header_label = ttk.Label(self.master, text="Белорусский национальный технический университет",
                                      font=("Arial", 14, "bold"))
        self.header_label.pack(pady=10)

        # Факультет и кафедра
        self.faculty_label = ttk.Label(self.master, text="Факультет информационных технологий и робототехники",
                                       font=("Arial", 12))
        self.faculty_label.pack()
        self.department_label = ttk.Label(self.master,
                                          text="Кафедра программного обеспечения информационных систем и технологий",
                                          font=("Arial", 12))
        self.department_label.pack()

        # Заголовок курсовой работы
        self.title_label = ttk.Label(self.master, text="Курсовой проект", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=20)

        # Название работы
        self.discipline_label = ttk.Label(self.master, text="по дисциплине Языки программирования",
                                          font=("Arial", 14))
        self.discipline_label.pack()
        self.project_label = ttk.Label(self.master, text="Конвертер чисел и системы счисления",
                                       font=("Arial", 20, "bold"))
        self.project_label.pack(pady=10)

        # Рисунок
        self.image = Image.open("images/code.jpg")
        new_width = int(self.image.width / 7)
        new_height = int(self.image.height / 7)
        self.resized_image = self.image.resize((new_width, new_height))
        self.photo = ImageTk.PhotoImage(self.resized_image)

        # Рамка для изображения и информации
        self.frame1 = ttk.Frame(self.master)
        self.frame1.pack()

        # Изображение
        self.image_label = ttk.Label(self.frame1, image=self.photo)
        self.image_label.image = self.photo  # Чтобы картинка не исчезала
        self.image_label.pack(side=LEFT)

        # Автор и преподаватель
        self.author_label = ttk.Label(self.frame1,
                                      text="Выполнил: Студент группы 10701223\nКалугин Александр Андреевич",
                                      font=("Arial", 12))
        self.author_label.pack()
        self.teacher_label = ttk.Label(self.frame1, text="Преподаватель: к.ф.-м.н., доц.\nСидорик Валерий Владимирович",
                                       font=("Arial", 12))
        self.teacher_label.pack(pady=30)

        # Год и место
        self.place_label = ttk.Label(self.master, text="Минск 2024", font=("Arial", 12))
        self.place_label.pack(pady=10)

        # Frame для кнопок навигации
        self.button_frame = Frame(self.master)
        self.button_frame.pack(fill="both", expand=True)

        # Настройка столбцов в button_frame
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        # Кнопка "Далее"
        self.next_button = ttk.Button(self.button_frame, text="Далее", padding=(30, 5),
                                      command=self.next_button_clicked)
        self.next_button.grid(column=0, row=0, sticky="e", padx=20, pady=10)

        # Кнопка "Выход"
        self.exit_button = ttk.Button(self.button_frame, text="Выход", padding=(30, 5), command=self.master.destroy)
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
    first_window = FirstWindow()
    first_window.master.mainloop()


main()
