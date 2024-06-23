import tkinter as tk
import helper


def process_input():
    # Получаем входную строку
    input_text = entry.get()
    
    result = helper.openai(input_text)
    
    result_label.config(text=f"Результат: {result}")

# Создаем главное окно
root = tk.Tk()
root.title("Пример UI")

# Создаем виджет для ввода строки
entry = tk.Entry(root, width=40)
entry.pack(padx=20, pady=10)

# Создаем кнопку для запуска логики
process_button = tk.Button(root, text="Обработать", command=process_input)
process_button.pack(pady=5)

# Создаем метку для вывода результата
result_label = tk.Label(root, text="Результат: ")
result_label.pack(pady=10)

# Запускаем главный цикл
root.mainloop()
