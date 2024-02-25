from tkinter import*
from Staff import staffClass
from Company import CompanyClass
from User import UserClass
from Shippers import shipperClass
from Orders import orderClass
from Products import ProductClass
import os
class DashBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Tool Store")
        self.root.geometry("925x600+0+0")
        self.root.configure(bg="#FFDB1C")
        self.root.iconbitmap(r"favicon (1).ico")
        self.root.resizable(False, False)

        self.img = PhotoImage(file="Nintendo-Game-Boy-Color_-Poster-by-Richard-Parry-_-Displate.gif")
        Label(self.root, image=self.img, bg="#FFDB1C").place(x=50, y=35)

        frame = Frame(self.root, width=430, height=490, bg="#FFDB1C", highlightbackground="#FF5F9E", highlightthickness=4)
        frame.place(x=430, y=60)

        self.heading = Label(frame, text="TOOL STORE", fg="#1CD6CE", bg="white", font=("Time New Roman", 30, "bold"),highlightbackground="#08FFC8", highlightthickness=4)
        self.heading.place(x=75, y=25)

        btn_1 = Button(frame, width=26, pady=7, text="STAFF",bg="#FFDB1C", fg="#3B064D", font=("Time New Roman", 15, "bold"), border=2, command=self.staff_button).place(x=50, y=100)
        btn_2 = Button(frame, width=26, pady=7, text="USER", bg="#FFDB1C", fg="#3B064D", font=("Time New Roman", 15, "bold"), border=2, command=self.user_button).place(x=50, y=150)
        btn_4 = Button(frame, width=26, pady=7, text="PRODUCT", bg="#FFDB1C", fg="#3B064D", font=("Time New Roman", 15, "bold"), border=2, command=self.product_button).place(x=50, y=200)
        btn_5 = Button(frame, width=26, pady=7, text="COMPANY", bg="#FFDB1C", fg="#3B064D", font=("Time New Roman", 15, "bold"), border=2, command=self.company_button).place(x=50, y=250)
        btn_6 = Button(frame, width=26, pady=7, text="ORDER", bg="#FFDB1C", fg="#3B064D", font=("Time New Roman", 15, "bold"), border=2, command=self.order_button).place(x=50, y=300)
        btn_7 = Button(frame, width=26, pady=7, text="SHIPPER", bg="#FFDB1C", fg="#3B064D", font=("Time New Roman", 15, "bold"), border=2, command=self.shipper_button).place(x=50, y=350)
        logOutButton = Button(frame, width=26, pady=7, text="LOG OUT", bg="#FFDB1C", fg="#FF5F9E", font=("Time New Roman", 15, "bold"), border=2,command=self.logOutButton).place(x=50, y=400)

    
    def staff_button(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=staffClass(self.new_win)
        self.root.destroy()
        os.system("python Staff.py")

    def user_button(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=UserClass(self.new_win)
        self.root.destroy()
        os.system("python User.py")

    def product_button(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ProductClass(self.new_win)
        self.root.destroy()
        os.system("python Products.py")

    def order_button(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=orderClass(self.new_win)
        self.root.destroy()
        os.system("python Orders.py")

    def company_button(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CompanyClass(self.new_win)
        self.root.destroy()
        os.system("python Company.py")

    def shipper_button(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=shipperClass(self.new_win)
        self.root.destroy()
        os.system("python Shippers.py")

    def logOutButton(self):
        self.root.destroy()
        os.system("python Login.py")


if __name__=="__main__":
    root=Tk()
    obj=DashBoard (root)
    root.mainloop()