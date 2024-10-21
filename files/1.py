import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Создаем главное окно
root = tk.Tk()
root.title("Пример всплывающей подсказки")
root.geometry("150x150")

# Загружаем картинку с вопросом
image = Image.open("images/question.png")

# Уменьшаем размер картинки
new_width = 30  # Новая ширина
new_height = 30  # Новая высота
image = image.resize((new_width, new_height))
photo = ImageTk.PhotoImage(image)

# Создаем метку с картинкой
image_label = tk.Label(root, image=photo, borderwidth=0)  # Без рамки по умолчанию
image_label.image = photo  # Сохраняем ссылку на фото для предотвращения удаления
image_label.pack()

# Переменная для хранения ссылки на всплывающую подсказку
tooltip = None


# Функция для создания всплывающей подсказки
def show_tooltip(event):
    global tooltip
    if tooltip:
        tooltip.destroy()  # Уничтожаем предыдущую подсказку, если она есть

    tooltip = tk.Toplevel(root)
    tooltip.overrideredirect(True)  # Скрываем заголовок окна подсказки
    tooltip.geometry("+%s+%s" % (event.x_root + 10, event.y_root + 10))  # Позиционируем подсказку рядом с курсором
    tooltip.wm_attributes("-topmost", 1)  # Делаем подсказку самой верхней

    # Добавляем текст в подсказку
    text = "Это картинка с вопросом! \n\nНажмите на изображение для получения дополнительной информации."
    text_label = tk.Label(tooltip, text=text, wraplength=200)
    text_label.pack()


# Функция для скрытия подсказки
def hide_tooltip(event):
    global tooltip
    if tooltip:
        tooltip.destroy()  # Уничтожаем всплывающую подсказку


# Функция для изменения визуального состояния при наведении
def on_hover(event):
    image_label.config(cursor="hand2")  # Рамка и изменение курсора


# Функция для возврата к исходному состоянию
def on_leave(event):
    image_label.config(cursor="")  # Убираем рамку и курсор по умолчанию


# Привязываем функции к событиям клика на картинку и наведения курсора
image_label.bind("<Enter>", on_hover)  # Изменение при наведении
image_label.bind("<Leave>", on_leave)  # Возвращение к исходному состоянию
image_label.bind("<Button-1>", show_tooltip)  # Показать всплывающую подсказку при нажатии
image_label.bind("<ButtonRelease-1>", hide_tooltip)  # Скрыть подсказку при отпускании

# Запускаем главное окно
root.mainloop()
