from tkinter import filedialog
import tkinter
import tkinter as tk


class File:
    def __init__(self, root, input_entry, output_entry):
        self.root = root
        self.input_entry = input_entry
        self.output_entry = output_entry

    def open_file(self):
        """Открывает текстовый файл и выводит его содержимое в текстовое поле."""

        # Открываем диалоговое окно для выбора файла
        filepath = tkinter.filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )

        # Если файл выбран
        if filepath:
            try:
                # Открываем файл на чтение
                with open(filepath, "r", encoding='utf-8') as file:
                    # Считываем содержимое файла
                    text = file.read()

                    # Выводим содержимое в текстовое поле
                    self.input_entry.delete(0, tk.END)  # Очищаем текстовое поле
                    self.input_entry.insert(tk.END, text)

            except FileNotFoundError:
                # Обработка ошибки, если файл не найден
                self.root.messagebox.showerror("Ошибка", f"Файл '{filepath}' не найден.")

    def save_file(self):
        """Сохраняет содержимое текстового поля в файл."""

        # Открываем диалоговое окно для выбора файла
        filepath = tkinter.filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )

        # Если файл выбран
        if filepath:
            try:
                # Получаем текст из текстового поля
                text = self.output_entry.get()

                # Сохраняем текст в файл
                with open(filepath, "w", encoding='utf-8') as file:
                    file.write(text)

            except Exception as e:
                # Обработка ошибок при сохранении
                self.root.messagebox.showerror("Ошибка", f"Ошибка при сохранении файла: {e}")
