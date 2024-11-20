from tkinter import *
from tkinter import ttk

root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("300x300")  # устанавливаем размеры окна

label = Label(text="Hello")  # создаем текстовую метку
label.pack()  # размещаем метку в окне
btn=ttk.Button()
btn.pack()
# устанавливаем параметр text
btn["text"]="Send"
# получаем значение параметра text
btnText = btn["text"]
print(btnText)

root.mainloop()