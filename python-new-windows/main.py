from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Лабораторная работа № 9')
window.config(bg='azure3')
window.resizable(width=False, height=False)

f = ('Times', 14)


def toggle_password():
    if show_password_var.get():
        password.config(show='')
    else:
        password.config(show='*')

def on_close():
    if messagebox.askokcancel('Выход', 'Действительно хотите закрыть приложение?'):
        window.quit()

window.protocol('WM_DELETE_WINDOW', on_close)

left_frame = Frame(window, bd=2, bg='azure3', relief=SOLID, padx=10, pady=10)

Label(left_frame, text="Введите логин", bg='azure3', font=f).grid(row=0, column=0, sticky=W, pady=10)
Label(left_frame, text="Введите пароль", bg='azure3', font=f).grid(row=1, column=0, pady=10)

name = Entry(left_frame, font=f)
password = Entry(left_frame, font=f, show='*')

name.grid(row=0, column=1, pady=10, padx=20)
password.grid(row=1, column=1, pady=10, padx=20)

show_password_var = BooleanVar()
show_password_checkbox = Checkbutton(left_frame, text="Показать пароль", variable=show_password_var, bg='azure3', font=f, command=toggle_password)
show_password_checkbox.grid(row=2, columnspan=2, pady=10, padx=20)

login_btn = Button(left_frame, width=15, text='Войти', font=f, relief=SOLID, cursor='hand2', command=None)
login_btn.grid(row=3, columnspan=2, pady=10)

left_frame.pack()

window.mainloop()
