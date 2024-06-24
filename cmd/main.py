import tkinter as tk
import helper
import webbrowser

def callback(url):
    webbrowser.open_new(url)

def process_input():
    # Получаем входную строку
    input_text = entry.get()
    
    result, link_type = helper.openai(input_text)
    
    result_label.config(text=f"Результат: {input_text}")
    result_label_2.config(text=f"Тип ссылки: {link_type}")

    print(str(result[0]))
    result_label.bind("<Результат>", lambda e: callback(str(result[0])))

# Создаем главное окно
root = tk.Tk()
root.title("Пример UI")

# Создаем виджет для ввода строки
entry = tk.Entry(root, width=150)
entry.pack(padx=20, pady=10)

# Создаем кнопку для запуска логики
process_button = tk.Button(root, text="Обработать", command=process_input)
process_button.pack(pady=5)

# Создаем метку для вывода результата
result_label = tk.Label(root, text="Результат: ")
result_label.pack(pady=10)

result_label_2 = tk.Label(root, text="Тип ссылки: ")
result_label_2.pack(pady=10)

# Запускаем главный цикл
root.mainloop()
