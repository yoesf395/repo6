import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
import json
import Register

admin_data = {
    "mail": "admin@gmail.com",
    "password": "admin123"
}

def open_register_page():
        root.destroy()
        Register.RegistrationPage()

def on_enter_user(e):
    user.delete(0, 'end')

def on_leave_user(e):
    name = user.get()
    if not name:
        user.insert(0, 'Username')

def on_enter_password(e):
    password.delete(0, 'end')

def on_leave_password(e):
    name = password.get()
    if not name:
        password.insert(0, 'Password')

def toggle_password_visibility():
    current_password = password.get()
    if password.cget("show") == "":
        password.config(show="*")
    else:
        password.config(show="")
    password.delete(0, 'end')
    password.insert(0, current_password)

def login():
    username = user.get()
    user_password = password.get()

    if not username or not user_password:
        messagebox.showerror("Login Failed", "Please enter both username and password.")
        return

    try:
        with open('user_data.json', 'r') as json_file:
            data = json.load(json_file)
            if not isinstance(data, list):
                raise TypeError("The data is not a list")
    except FileNotFoundError:
        messagebox.showerror("Login Failed", "User data file not found.")
        return
    except Exception as e:
        messagebox.showerror("Login Failed", f"An error occurred: {str(e)}")
        return

    is_admin = False

    for user_data in data:
        if username == admin_data["mail"] and user_password == admin_data["password"]:
            is_admin = True
            break

    if is_admin:
        messagebox.showinfo("Login", "Login Successful as an Admin")
    else:
        for user_data in data:
            if username == user_data["username"] and user_password == user_data["password"]:
                messagebox.showinfo("Login", "Login Successful as a Normal User")
                break
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    clear_fields()

def clear_fields():
    user.delete(0, 'end')
    password.delete(0, 'end')

root = tk.Tk()
root.title("Login Page")
root.geometry('900x500+300+200')
root.configure(bg='#131313')
root.resizable(False, False)
bg_image = tk.PhotoImage(file="login001.png")
bg_label = tk.Label(root, image=bg_image, bg='#131313')
bg_label.place(x=420, y=10)

frame = Frame(root, width=350, height=350, bg="#131313")
frame.place(x=50, y=55)

heading = Label(frame, text='Sign in', fg='white', bg='#131313', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg='white', borderwidth=0, bg="#131313", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_user)
user.bind('<FocusOut>', on_leave_user)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

password = Entry(frame, width=25, fg='white', borderwidth=0, bg="#131313", font=('Microsoft YaHei UI Light', 11), show="*")
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter_password)
password.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

show_password_button = Button(frame, width=14, text="Show Password", border=0, bg='#131313', cursor='hand2', fg='#57a1f8', command=toggle_password_visibility)
show_password_button.place(x=26, y=180)

login_button = Button(frame,font=('Microsoft YaHei UI Light', 11), width=30, pady=10, text='Login', bg='#FF5B31', fg='white', border=0, command=login)
login_button.place(x=35, y=215)
label = Label(frame, width=39, pady=7, text="Don't have an account?", fg='white', bg='#131313', font=('Microsoft YaHei UI Light', 9))
label.place(x=20, y=269)
register_button = Button(frame, width=6, text='Register', border=0, bg='#131313', cursor='hand2', fg='#FF5B31', command=open_register_page)
register_button.place(x=225, y=276)
root.mainloop()
if __name__ == "__main__": 
    login()