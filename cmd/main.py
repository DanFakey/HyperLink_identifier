# import tkinter as tk
# import helper
# import webbrowser

# def callback(url):
#     webbrowser.open_new(url)

# def process_input():
#     # Получаем входную строку
#     input_text = entry.get("1.0", tk.END)
    
#     result, link_type = helper.openai(input_text)
#     start_idx = input_text.find(result[0])
#     end_idx = start_idx + len(result[0])
    
#     result_label.delete("1.0", tk.END)
#     result_label.insert(tk.END, input_text[:start_idx])

#     # Добавляем ссылку
#     result_label.insert(tk.END, result[0], "link")
    
#     # Добавляем остальной текст
#     result_label.insert(tk.END, input_text[end_idx:])
    
#     # Применяем тег для создания кликабельной ссылки
#     result_label.tag_config("link", foreground="blue", underline=1)
#     result_label.tag_bind("link", "<Button-1>", callback)
    
#     result_label.config(text=f"Результат: {input_text}")
#     result_label_2.config(text=f"Тип ссылки: {link_type}")

#     if link_type == "Ссылка":
#         result_label.bind("<Button-1>", lambda e: callback(str(result[0])))
#     elif link_type == "Телеграм":
#         result = result[0]
#         result = result[1:] 
#         result_label.bind("<Button-1>", lambda e: callback("t.me/"+str(result)))
#     elif link_type == "Почта":
#         result[0] = "mailto:"+result[0]
#         result_label.bind("<Button-1>", lambda e: callback(str(result[0])))
#     elif link_type == "ВК":
#         result_label.bind("<Button-1>", lambda e: callback(str(result[0])))



# # Создаем главное окно
# root = tk.Tk()        
# root.title("Пример UI")

# # Создаем виджет для ввода строки
# entry = tk.Text(root, width=150)
# entry.pack(padx=20, pady=10)

# # Создаем кнопку для запуска логики
# process_button = tk.Button(root, text="Обработать", command=process_input)
# process_button.pack(pady=5)

# # Создаем метку для вывода результата
# result_label = tk.Text(root, width=60, height=10)
# result_label.pack(pady=10)

# result_label_2 = tk.Label(root, text="Тип ссылки: ")
# result_label_2.pack(pady=10)

# # Запускаем главный цикл
# root.mainloop()


# import tkinter as tk
# import helper
# import webbrowser

# def callback(event):
#     # Получаем текст ссылки
#     url = event.widget.get("current linestart", "current lineend")

#     webbrowser.open_new(url)

# def process_input():
#     # Получаем входную строку
#     input_text = entry.get("1.0", tk.END)
    
#     result, lint_type = helper.openai(input_text)
    
#     start_idx = input_text.find(result[0])
#     end_idx = start_idx + len(result[0])
    
#     # Очищаем текстовое поле для результата
#     result_text.delete("1.0", tk.END)
    
#     # Добавляем текст до ссылки
#     result_text.insert(tk.END, input_text[:start_idx])
    
#     # Добавляем ссылку
#     result_text.insert(tk.END, result[0], "link")
    
#     # Добавляем остальной текст
#     result_text.insert(tk.END, input_text[end_idx:])
    
#     # Применяем тег для создания кликабельной ссылки
#     result_text.tag_config("link", foreground="blue", underline=1)
#     result_text.tag_bind("link", "<Button-1>", callback)

# root = tk.Tk()
# root.title("Пример UI")

# # Поле для ввода текста
# entry = tk.Text(root, width=60, height=10)
# entry.pack(padx=20, pady=10)

# # Кнопка для запуска логики
# process_button = tk.Button(root, text="Обработать", command=process_input)
# process_button.pack(pady=5)

# # Поле для вывода результата
# result_text = tk.Text(root, width=60, height=10)
# result_text.pack(padx=20, pady=10)

# # Запускаем главный цикл
# root.mainloop()



import tkinter as tk
import helper
import webbrowser

def callback(result):
    webbrowser.open_new(result)

def process_input():
    # Получаем входную строку
    input_text = entry.get("1.0", tk.END)
    
    result, link_type = helper.openai(input_text)
    
    start_idx = input_text.find(result[0])
    end_idx = start_idx + len(result[0])
    
    # Очищаем текстовое поле для результата
    result_text.delete("1.0", tk.END)
    
    # Добавляем текст до ссылки
    result_text.insert(tk.END, input_text[:start_idx])
    
    # Добавляем ссылку
    result_text.insert(tk.END, result[0], "link")
    
    # Добавляем остальной текст
    result_text.insert(tk.END, input_text[end_idx:])
    
    # Применяем тег для создания кликабельной ссылки
    result_text.tag_config("link", foreground="blue", underline=1)
    result_text.tag_bind("link", "<Button-1>", lambda event, url=result[0]: callback(url))

root = tk.Tk()
root.title("Пример UI")

# Поле для ввода текста
entry = tk.Text(root, width=60, height=10)
entry.pack(padx=20, pady=10)

# Кнопка для запуска логики
process_button = tk.Button(root, text="Обработать", command=process_input)
process_button.pack(pady=5)

# Поле для вывода результата
result_text = tk.Text(root, width=60, height=10)
result_text.pack(padx=20, pady=10)

# Запускаем главный цикл
root.mainloop()