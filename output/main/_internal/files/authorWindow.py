from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class AuthorWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window

        self.author_window = Toplevel()
        self.author_window.title("Конвертер чисел и системы счисления")

        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Вычисляем координаты для центрирования окна
        window_width = 400
        window_height = 620
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        # Устанавливаем геометрию окна
        self.author_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Считывание и форматирование изображения
        self.image_author = Image.open("images/author.jpg")
        new_width = int(self.image_author.width / 3)  # Уменьшаем ширину в 4 раза
        new_height = int(self.image_author.height / 3)  # Уменьшаем высоту в 4 раза
        self.image_author_resized = self.image_author.resize((new_width, new_height))
        self.photo_author = ImageTk.PhotoImage(self.image_author_resized)

        # Создание изображения
        self.image_label = ttk.Label(self.author_window, image=self.photo_author)
        self.image_label.image = self.photo_author  # Чтобы картинка не исчезала
        self.image_label.pack(pady=10)

        # Информация об авторе
        self.label_author = ttk.Label(self.author_window, text="Автор", font=("Arial", 14))
        self.label_author.pack()
        self.label_groop = ttk.Label(self.author_window, text="Студент группы 10701223", font=("Arial", 14))
        self.label_groop.pack()
        self.label_name = ttk.Label(self.author_window, text="Калугин Александр Андреевич", font=("Arial", 14))
        self.label_name.pack()
        self.label_mail = ttk.Label(self.author_window, text="sashakalugin74@gmail.com", font=("Arial", 14))
        self.label_mail.pack()

        # Создаем объект стиля
        self.style = ttk.Style()
        # Задаем стили для кнопки
        self.style.configure("Author.TButton", font=("Calibri", 10), padding=(15, 3))

        # Кнопка назад
        self.back_button = ttk.Button(self.author_window, text="Назад",
                                      command=self.back_button_clicked, style="Author.TButton")
        self.back_button.pack(pady=15, padx=15)

    def back_button_clicked(self):
        """Возвращение назад к главнмоу окну"""

        self.author_window.withdraw()
        self.main_window.deiconify()
