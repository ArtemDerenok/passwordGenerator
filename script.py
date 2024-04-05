import random
import tkinter as tk
import string

window = tk.Tk()
window.title('Генератор паролей')
window.geometry('300x250')


def set_error():
    quantity_nums = quantity_nums_entry.get()
    quantity_letters = quantity_letters_entry.get()

    if quantity_nums.isdigit() is not True or quantity_letters.isdigit() is not True:
        result_label['fg'] = 'red'
        result_label['text'] = ('Введено неверное колличество символов.')


def clear_error():
    result_label['text'] = ''


def show_password(password):
    result_label['fg'] = 'green'
    result_label['text'] = f'Ваш пароль: {password}'


is_valid_entry1 = False
is_valid_entry2 = False


def password_generate():
    clear_error()
    quantity_nums = quantity_nums_entry.get()
    quantity_letters = quantity_letters_entry.get()
    quantity_nums = int(quantity_nums)
    quantity_letters = int(quantity_letters)
    list1 = random.choices(string.digits, k=quantity_nums)
    list2 = random.choices(string.ascii_lowercase, k=quantity_letters)
    result_list = list1 + list2
    random.shuffle(result_list)
    password = ''.join(result_list)

    show_password(password)


def on_btn():
    global is_valid_entry1
    global is_valid_entry2

    if is_valid_entry1 is True and is_valid_entry2 is True:
        generate_btn['state'] = tk.NORMAL
    else:
        generate_btn['state'] = tk.DISABLED


def is_valid_num_entry(newval):
    global is_valid_entry1

    if newval.isdigit():
        is_valid_entry1 = True
        on_btn()
        return True
    else:
        set_error()
        return False


def is_valid_letter_entry(newval):
    global is_valid_entry2

    if newval.isdigit():
        is_valid_entry2 = True
        on_btn()
        return True
    else:
        set_error()
        return False


check1 = (window.register(is_valid_num_entry), "%P")
check2 = (window.register(is_valid_letter_entry), '%P')

main_label = tk.Label(window, text='Определите сложность пароля.')
main_label.place(x=10, y=10)
quantity_nums_label = tk.Label(window, text='Введите колличество цифр: ')
quantity_nums_label.place(x=10, y=50)
quantity_letters_label = tk.Label(window, text='Введите колличество букв: ')
quantity_letters_label.place(x=10, y=70)
result_label = tk.Label(window, wraplength=250)
result_label.place(x=10, y=90)

quantity_nums_entry = tk.Entry(window, width=3, validate='key', validatecommand=check1)
quantity_nums_entry.place(x=170, y=50)
quantity_letters_entry = tk.Entry(window, width=3, validate='key', validatecommand=check2)
quantity_letters_entry.place(x=165, y=70)
generate_btn = tk.Button(window, text='Сгенерировать пароль', width=30, command=password_generate, state=tk.DISABLED)
generate_btn.place(x=10, y=210)

window.mainloop()
