from tkinter import *

window = Tk()
window.title("Login Me")
window.geometry("450x300")
window.config(background="blue")

user_name = Label(window, text="Username").place(x=40,y=60)
user_password = Label(window, text="Password").place(x=40, y=100)
submit_button = Button(window, text="Submit").place(x=40, y=130)
user_name_input_area = Entry(window, width=30).place(x=110, y=60)
user_password_entry_area = Entry(window, show='.', width=30).place(x=110, y=100)

window.mainloop()
