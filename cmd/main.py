import tkinter as tk
import helper
import webbrowser

def callback(result):
    webbrowser.open_new(result)

def process_input():
    # Получаем входную строку
    input_text = entry.get("1.0", tk.END)
    
    result, link_type = helper.openai(input_text)
    if len(result) == 0:
        result_text.delete("1.0", tk.END)
        return
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
    result_text.tag_config("link", foreground="blue", underline=1)

  
    if link_type == "Ссылка":
        result_text.tag_bind("link", "<Button-1>", lambda event, url=result[0]: callback(url))
    elif link_type == "Телеграм":
        if len(result) == 0:
            result_text.delete("1.0", tk.END)
        else:
            result = result[0]
            result = result[1:]
            result_text.tag_bind("link", "<Button-1>", lambda event, url="t.me/"+result: callback(url))
    elif link_type == "Почта":
        if len(result) == 0:
            result_text.delete("1.0", tk.END)
        else:
            result_text.tag_bind("link", "<Button-1>", lambda event, url="mailto:"+result[0]: callback(url))
    elif link_type == "ВК":
        if len(result) == 0:
            result_text.delete("1.0", tk.END)
        else:
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