import random
import tkinter as tk

window = tk.Tk()
window.title('Генератор паролей')
window.geometry('400x400')

def set_error():
    result_label['fg'] = 'red'
    result_label['text'] = ('Введено неверное колличество символов.')

def clear_error():
    result_label['text'] = ''

def show_password(password):
    result_label['fg'] = 'green'
    result_label['text'] = f'Ваш пароль: {password}'
def password_generate():
    clear_error()
    password = ''
    quantity_chars = quantity_chars_entry.get()

    if quantity_chars.isdigit():
        quantity_chars = int(quantity_chars)

        for i in range(quantity_chars):
            char = random.randint(1, 9)
            password += str(char)

        show_password(password)
    else:
        set_error()


main_label = tk.Label(window, text='Определите сложность пароля.')
main_label.place(x=10, y=10)
quantity_chars_label = tk.Label(window, text='Введите колличество символов: ')
quantity_chars_label.place(x=10, y=50)
result_label = tk.Label(window)
result_label.place(x=10, y=90)

quantity_chars_entry = tk.Entry(window, width=3)
quantity_chars_entry.place(x=200, y=50)
generate_btn = tk.Button(window, text='Сгенерировать пароль', width=30, command=password_generate)
generate_btn.place(x=10, y=360)

window.mainloop()
