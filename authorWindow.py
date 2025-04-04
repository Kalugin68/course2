from PIL import Image
import customtkinter as ctk


class AuthorWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window

        self.author_window = ctk.CTkToplevel()
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
        self.photo_author = ctk.CTkImage(light_image=self.image_author, dark_image=self.image_author,
                                         size=(320, 426))

        # Создание изображения
        self.image_label = ctk.CTkLabel(self.author_window, image=self.photo_author, text="")
        self.image_label.image = self.photo_author  # Чтобы картинка не исчезала
        self.image_label.pack(pady=10)

        # Информация об авторе
        self.label_author = ctk.CTkLabel(self.author_window, text="Автор", font=("Calibri", 18))
        self.label_author.pack()
        self.label_groop = ctk.CTkLabel(self.author_window, text="Студент группы 10701223", font=("Calibri", 18))
        self.label_groop.pack()
        self.label_name = ctk.CTkLabel(self.author_window, text="Калугин Александр Андреевич", font=("Calibri", 18))
        self.label_name.pack()
        self.label_mail = ctk.CTkLabel(self.author_window, text="sashakalugin74@gmail.com", font=("Calibri", 18))
        self.label_mail.pack()

        # Кнопка назад
        self.back_button = ctk.CTkButton(self.author_window, text="Назад",
                                         command=self.back_button_clicked)
        self.back_button.pack(pady=15, padx=15)

    def back_button_clicked(self):
        """Возвращение назад к главнмоу окну"""

        self.author_window.withdraw()
        self.main_window.deiconify()
