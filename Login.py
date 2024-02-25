kfrom tkinter import*
import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3 
import os

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x900+0+0")
        self.root.iconbitmap(r"favicon (1).ico")
        self.root.title("Login")
        self.image_bg=ImageTk.PhotoImage(file="login (2).png")
        self.lbl_image_=Label(self.root, image=self.image_bg, bd=0).place(x=0, y=0)
        self.root.resizable(False, False)
    #==================login frame============================
        login_frame=Frame(self.root, bd=0, relief=RIDGE,bg="#2D2727")
        login_frame.place(x=330,y=200,width=320, height=360)

        title=Label(login_frame,text="Log into account", font=("Century Gothic", 20),bg="#2D2727",fg="white")
        title.place(x=10, y=45)
    #====================================================
        self.userID=StringVar()
        self.password=StringVar()

        lbl_user=Label(login_frame,text="User ID",font=("Century Gothic", 12),bg="#2D2727",fg="white")
        lbl_user.place(x=10,y=100)
        txt_user=Entry(login_frame,textvariable=self.userID,width=21,font=("Century Gothic", 10))
        txt_user.place(x=100,y=105)

        lbl_pass=Label(login_frame,text="Password",font=("Century Gothic", 12),bg="#2D2727",fg="white")
        lbl_pass.place(x=10,y=150)
        txt_pass=Entry(login_frame,textvariable=self.password,width=21,font=("Century Gothic", 10),show="*")
        txt_pass.place(x=100,y=155)
    #======================================================
        button1=customtkinter.CTkButton(login_frame, width=220, text='Login', corner_radius=6,command=self.login)
        button1.place(x=50, y=240)

        button2=customtkinter.CTkButton(login_frame, text="Forget password?", font=("Century Gothic", 12),fg_color="#2D2727",command=self.forget_win)
        button2.place(x=156, y=195)
        


    def login(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.userID.get()=="" or self.password.get()=="":
                messagebox.showerror("Error", "Please fill the blank", parent=self.root)

            elif self.userID.get()=="Nguyen Minh Hoang" and self.password.get()=="06122003":
                messagebox.showinfo("Welcome", "Welcome back, Admin !",parent=self.root)
                self.root.destroy()
                os.system("python main.py")
            else:
                cur.execute("SELECT * FROM USER WHERE ID=? AND PASSWORD=?",(self.userID.get(), self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error", "Invalid username/password", parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python main.py")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)   

    def forget_win(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.userID.get()=="":
                messagebox.showerror("Error", "User ID is required!", parent=self.root)
            else:
                cur.execute("SELECT EMAIL FROM USER WHERE ID=?",(self.userID.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error", "Invalid User ID, try again", parent=self.root)
                else:
                    self.forget_window=Toplevel(self.root)
                    self.forget_window.title("Reset password")
                    self.forget_window.geometry("400x400+500+100")
                    self.forget_window.iconbitmap(r"favicon (1).ico")
                    self.imag_bg=ImageTk.PhotoImage(file="forgetpass (1).png")
                    self.lbl_imag_=Label(self.forget_window,image=self.imag_bg, bd=0).place(x=0, y=0)
                    self.forget_window.resizable(False,False)

                    reset_frame=Frame(self.forget_window, bd=0, relief=RIDGE,bg="#2D2727")
                    reset_frame.place(x=70,y=80,width=250, height=250)
                    #====================================================================
                    title=Label(self.forget_window,text="Reset", font=("Century Gothic", 15),bg="#2D2727",fg="white")
                    title.place(x=166, y=90)
                    
                    self.new_pass=StringVar()
                    self.confirm_pass=StringVar() 

                    lbl_newpass=Label(self.forget_window,text="New password", font=("Century Gothic", 10),bg="#2D2727",fg="white")
                    lbl_newpass.place(x=75, y=150)
                    txt_newpass=Entry(self.forget_window,width=14,font=("Century Gothic", 10),textvariable=self.new_pass)
                    txt_newpass.place(x=190,y=150)

                    lbl_confirmpass=Label(self.forget_window,text="Confirm pass", font=("Century Gothic", 10),bg="#2D2727",fg="white")
                    lbl_confirmpass.place(x=75, y=200)
                    txt_newpass=Entry(self.forget_window,width=14,font=("Century Gothic", 10),textvariable=self.confirm_pass)
                    txt_newpass.place(x=190,y=200)
#==========================================================================================
                    btn_reset=customtkinter.CTkButton(self.forget_window, width=150, text='Reset', corner_radius=6,command=self.reset_pass)
                    btn_reset.place(x=120, y=250)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
            
    def reset_pass(self):
        if self.new_pass.get()=="" or self.confirm_pass.get()=="":
            messagebox.showerror("Error", "Password is required!",parent=self.forget_window)
        elif self.new_pass.get()!=self.confirm_pass.get():
            messagebox.showerror("Error", "New password and confirm are not same!, please try again",parent=self.forget_window)
        else:
            conn=sqlite3.connect(database=r'toolStore.db')
            cur=conn.cursor()
            try:
                cur.execute("UPDATE USER SET PASSWORD=? WHERE ID=?",(self.new_pass.get(),self.userID.get()))
                messagebox.showinfo("reset", "Reset sucessfully😎")
                conn.commit()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


root=Tk()
obj=Login(root)
root.mainloop()



#if entry1.get()=='' or  entry2.get()=='':
    #   messagebox.showerror('Error!', 'Fields cannot be empty!')
    # elif entry1.get()=='abc' and entry2.get()=='1234':
    #   app.destroy()
    