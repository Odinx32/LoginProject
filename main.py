from tkinter import *
from global_variables import *
import modules
####################################
def login_window():
    global login_window_exists
    if login_window_exists is None:
        login_window_exists = True
        root = Tk()
        root.title("login")
        root.config(bg="#d17b75")
        root.geometry("400x500+0+0")
        root.resizable(False,False)

        user_label = Label(root,text="Username",width=10,bg="#d17b75")
        user_label.place(x=100,y=100)
        password_label = Label(root,text="Password",width=10,bg="#d17b75")
        password_label.place(x=100,y=150)

        user_entry = Entry(root,width=20)
        user_entry.place(x=200,y=100)
        password_entry = Entry(root,width=20)
        password_entry.place(x=200,y=150)

        login_button = Button(root,text='Login')
        login_button.place(x=115,y=200)
        signup_button = Button(root,text="Signup",command=signup_window)
        signup_button.place(x=115,y=250)


        root.mainloop()

def signup_window():
    global signup_window_exists
    if signup_window_exists is None:
        root = Tk()
        root.title("Signup")
        root.geometry("400x500+0+0")
        root.resizable(False,False)
        root.config(bg="#d17b75")

        firstname_label = Label(root,text="Firstname",width=10,bg="#d17b75")
        firstname_label.place(x=100,y=100)
        lastname_label = Label(root,text="Lastname",width=10,bg="#d17b75")
        lastname_label.place(x=100,y=150)
        email_label = Label(root,text="Email",width=10,bg="#d17b75")
        email_label.place(x=90,y=200)
        phone_label = Label(root,text="Phone",width=10,bg="#d17b75")
        phone_label.place(x=90,y=250)

        firstname_entry = Entry(root,width=20)
        firstname_entry.place(x=200,y=100)
        lastname_entry = Entry(root,width=20)
        lastname_entry.place(x=200,y=150)
        email_entry = Entry(root,width=20)
        email_entry.place(x=200,y=200)
        phone_entry = Entry(root,width=20)
        phone_entry.place(x=200,y=250)

        signup_button = Button(root,text="Signup",command=login_window)
        signup_button.place(x=112,y=300)

        signup_window_exists = True
        def close_signup_window():
            global signup_window_exists
            signup_window_exists = None
            root.destroy()

        root.protocol('WM_DELETE_WINDOW',close_signup_window)
        root.mainloop()

login_window()