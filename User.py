from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox
import sqlite3
from tkinter import ttk, messagebox
import customtkinter
import os
class UserClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Tool Store")
        self.root.geometry("1400x700+0+0")
        root.iconbitmap(r"favicon (1).ico")
    #========================varibles=========================
        self.SEARCH = StringVar()
        self.ID = StringVar()
        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.Address = StringVar()
        self.City = StringVar()
        self.PhoneNumber = StringVar()
        self.Email = StringVar()
        self.Password = StringVar()

    #=======================================title==================================
        title = Label(self.root,bd=20, relief=RIDGE, text="USER", fg="black", bg="white", font=("Time New Roman", 40, "bold"))
        title.pack(side=TOP, fill=X)


    # =======================DataFrame===================
        Dataframe=Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=100,width=1500, height=400)
        
        DataframeLeft=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("Time New Roman", 15, "bold"))
        DataframeLeft.place(x=0,y=5,width=900,height=350)

        DataframeRight=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("Time New Roman", 15, "bold") )
        DataframeRight.place(x=900, y=5,width=460, height=350)
        #=====================buttons frame===================
        showDataFrame=Frame(self.root, bd=20, relief=RIDGE)
        showDataFrame.place(x=0, y=500,width=1400, height=190)

        smallWindow = LabelFrame(DataframeLeft, bd=10, relief=RIDGE, padx=10,font=("Time New Roman", 15, "bold"))
        smallWindow.place(x=610, y=0, width=260, height=330)
    #====================Search======================
        lbl_txtSearch = customtkinter.CTkEntry(master=smallWindow, width=220,height=55,placeholder_text="Enter ID",textvariable=self.SEARCH,font=("Time New Roman", 24, "bold"))
        lbl_txtSearch.grid(row=5, column=0, pady=7)

        searchStaffButton = Button(smallWindow, width=18,height=2, text="SEARCH", bg="white", fg="black", font=("Time New Roman", 15, "bold"),command=self.searchButton)
        searchStaffButton.grid(row=2, column=0, pady=7)
    #===========================content============================
        self.lblref1 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="UserID: ", padx= 2, pady=6)
        self.lblref1.grid(row=1, column=0, sticky=W)
        self.txtref1=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.ID)
        self.txtref1.grid(row=1, column=1)
        
        self.lblref2 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="LastName: ")
        self.lblref2.grid(row=2, column=0, sticky=W)
        self.txtref2=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.LastName)
        self.txtref2.grid(row=2, column=1)

        self.lblref3 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="FirstName: ", padx= 2, pady=6)
        self.lblref3.grid(row=3, column=0, sticky=W)
        self.txtref3=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.FirstName)
        self.txtref3.grid(row=3, column=1)

        self.lblref4 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Address: ", padx= 2, pady=6)
        self.lblref4.grid(row=4, column=0, sticky=W)
        self.txtref4=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.Address)
        self.txtref4.grid(row=4, column=1)

        self.lblref5 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Phone: ", padx= 2, pady=6)
        self.lblref5.grid(row=5, column=0, sticky=W)
        self.txtref5=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.PhoneNumber)
        self.txtref5.grid(row=5, column=1)

        self.lblref6 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="City: ", padx= 2, pady=6)
        self.lblref6.grid(row=6, column=0, sticky=W)
        self.txtref6=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.City)
        self.txtref6.grid(row=6, column=1)

        self.lblref7 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Email: ", padx= 2, pady=6)
        self.lblref7.grid(row=7, column=0, sticky=W)
        self.txtref7=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.Email)
        self.txtref7.grid(row=7, column=1)

        self.lblref8 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Password: ", padx= 2, pady=6)
        self.lblref8.grid(row=8, column=0, sticky=W)
        self.txtref8=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.Password)
        self.txtref8.grid(row=8, column=1)
    #===========================buttons============================
        registerStaffButton = Button(smallWindow, width=18,height=2, text="REGISTER", bg="white", fg="black", font=("Time New Roman", 15, "bold"),command=self.registerButton)
        registerStaffButton.grid(row=0, column=0, pady=7)

        resetStaffButton = Button(smallWindow, width=18,height=2, text="RESET", bg="white", fg="black", font=("Time New Roman", 15, "bold"), command=self.resetButton)
        resetStaffButton.grid(row=1, column=0, pady=7)

        updateStaffButton = Button(DataframeRight, width=34,height=2, text="UPDATE", bg="white", fg="black", font=("Time New Roman", 15, "bold"),command=self.updateButton)
        updateStaffButton.grid(row=0, column=0, pady=7)

        removeStaffButton = Button(DataframeRight, width=34,height=2, text="REMOVE", bg="white", fg="black", font=("Time New Roman", 15, "bold"), command=self.removeButton)
        removeStaffButton.grid(row=1, column=0, pady=7)

        exitStaffButton = Button(DataframeRight, width=34,height=2, text="EXIT", bg="white", fg="black", font=("Time New Roman", 15, "bold"), command=self.exitButton)
        exitStaffButton.grid(row=4, column=0, pady=7)

        viewAllStaffButton = Button(DataframeRight, width=34,height=2, text="VIEW ALL", bg="white", fg="black", font=("Time New Roman", 15, "bold"),command=self.showInfo)
        viewAllStaffButton.grid(row=3, column=0, pady=7)

    #=========================================ScrollBar======================================
        scroll_x = ttk.Scrollbar(showDataFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(showDataFrame, orient=VERTICAL)
        self.tree=ttk.Treeview(showDataFrame, column=("No", 
        "UserID", "LastName", "FirstName", "Address", "Phone", "City", "Email", "Password")
        , xscrollcommand=scroll_y.set, yscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.tree.xview)
        scroll_y=ttk.Scrollbar(command=self.tree.yview)

        self.tree.heading("No", text="No.", )
        self.tree.heading("UserID", text="User ID")
        self.tree.heading("LastName", text="Last Name")
        self.tree.heading("FirstName", text="First Name")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("City", text="City")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Password", text="Password")


        self.tree["show"] = "headings"

        self.tree.column("No", width=100)
        self.tree.column("UserID", width=100)
        self.tree.column("LastName", width=100)
        self.tree.column("FirstName", width=100)
        self.tree.column("Address", width=100)
        self.tree.column("Phone", width=100)
        self.tree.column("City",  width=100)
        self.tree.column("Email", width=100)
        self.tree.column("Password", width=100)
        self.tree.pack(fill=BOTH, expand=1)

        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.showInfo()
#======================================================================
    def registerButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.ID.get()=="":
                messagebox.showerror("Error", "User ID must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM USER WHERE ID=?",(self.ID.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","ID already assigned")
                else:
                    cur.execute("INSERT INTO USER  (ID, LAST_NAME ,FIRST_NAME ,ADDRESS , PHONE , CITY , EMAIL , PASSWORD  ) values(?,?,?,?,?,?,?,?)",(
                                self.ID.get(),
                                self.FirstName.get(),
                                self.LastName.get(),
                                self.Address.get(),
                                self.City.get(),
                                self.PhoneNumber.get(),
                                self.Email.get(),
                                self.Password.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Store Successfully", parent=self.root)
                    self.showInfo()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def showInfo(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM USER")
            rows=cur.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:    
                self.tree.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def OnDoubleClick(self,ev):
        x=self.tree.focus()
        content=self.tree.item(x)
        row=content['values']
        print(row)
        self.ID.set(row[1])
        self.FirstName.set(row[2])
        self.LastName.set(row[3])
        self.Address.set(row[4])
        self.City.set(row[5])
        self.PhoneNumber.set(row[6])
        self.Email.set(row[7])
        self.Password.set(row[8])

    def exitButton(self):
        self.exitButton = tkinter.messagebox.askyesno("User Information","Confirm if you want to exit")
        if self.exitButton > 0:
            self.root.destroy()
            os.system("python main.py")

        return
    def resetButton(self):
        self.txtref1.delete(0,END)
        self.txtref2.delete(0,END)
        self.txtref3.delete(0,END)
        self.txtref4.delete(0,END)
        self.txtref5.delete(0,END)
        self.txtref6.delete(0,END)
        self.txtref7.delete(0,END)
        self.txtref8.delete(0,END)

    def updateButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.ID.get()=="":
                messagebox.showerror("Error", "User ID must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM USER WHERE ID=?",(self.ID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID")
                else:
                    cur.execute("UPDATE USER SET LAST_NAME=?,FIRST_NAME=?,ADDRESS=?, PHONE=?, CITY=?, EMAIL=?, PASSWORD=? WHERE ID = ?",(
                                self.LastName.get(),
                                self.FirstName.get(),
                                self.Address.get(),
                                self.City.get(),
                                self.PhoneNumber.get(),
                                self.Email.get(),
                                self.Password.get(),
                                self.ID.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Update Successfully", parent=self.root)
                    self.showInfo()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    
    def removeButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.ID.get()=="":
                messagebox.showerror("Error", "user ID must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM USER WHERE ID=?",(self.ID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID")
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to remove?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM USER WHERE ID=?", (self.ID.get(),))
                        conn.commit()
                        messagebox.showinfo("Remove", "Remove Successfully",parent=self.root)
                        self.showInfo() 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def searchButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM USER WHERE ID LIKE ?", ('%' + str(self.SEARCH.get()) + '%',))
            rows=cur.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:    
                self.tree.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=UserClass(root)
    root.mainloop()

