from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox
import sqlite3
from tkinter import ttk, messagebox
import customtkinter
import os
class staffClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Tool Store")
        self.root.iconbitmap(r"favicon (1).ico")
#========================varibles=========================
        self.SEARCH = StringVar()
        self.gender = StringVar()
        self.ID = StringVar()
        self.Name = StringVar()
        self.DoB = StringVar()
        self.StartDate = StringVar()
        self.EndDate = StringVar()   
        self.PhoneNumber = StringVar()
        self.Email = StringVar()
        self.Salary = StringVar()
        #=======================Title======================
        title = Label(self.root,bd=20, relief=RIDGE, text="STAFF", fg="black", bg="white", font=("Time New Roman", 40, "bold"))
        title.pack(side=TOP, fill=X)

         # =======================DataFrame===================
        Dataframe=Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=100,width=1500, height=400)

        DataframeLeft=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("Time New Roman", 15, "bold"))
        DataframeLeft.place(x=0,y=5,width=900,height=350)

        DataframeRight=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("Time New Roman", 15, "bold") )
        DataframeRight.place(x=900, y=5,width=460, height=350)

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
        self.lblref1=Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="ID: ")
        self.lblref1.grid(row=1, column=0, sticky=W)
        self.txtref1=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.ID)
        self.txtref1.grid(row=1, column=1)

        self.lblref2=Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Name: ", padx= 2, pady=6)
        self.lblref2.grid(row=2, column=0, sticky=W)
        self.txtref2=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.Name)
        self.txtref2.grid(row=2, column=1)

        self.lblref3 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Date of birth: ", padx= 2, pady=6)
        self.lblref3.grid(row=3, column=0, sticky=W)
        self.txtref3=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.DoB)
        self.txtref3.grid(row=3, column=1)

        self.lblref4 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Start date: ", padx= 2, pady=6)
        self.lblref4.grid(row=4, column=0, sticky=W)
        self.txtref4=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.StartDate)
        self.txtref4.grid(row=4, column=1)

        self.lblref5 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="End date: ", padx= 2, pady=6)
        self.lblref5.grid(row=5, column=0, sticky=W)
        self.txtref5=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.EndDate)
        self.txtref5.grid(row=5, column=1)

        self.lblref6 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Phone number: ", padx= 2, pady=6)
        self.lblref6.grid(row=6, column=0, sticky=W)
        self.txtref6=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.PhoneNumber)
        self.txtref6.grid(row=6, column=1)

        self.lblref7 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Email: ", padx= 2, pady=6)
        self.lblref7.grid(row=7, column=0, sticky=W)
        self.txtref7=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.Email)
        self.txtref7.grid(row=7, column=1)

        self.lblref8 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Salary: ", padx= 2, pady=6)
        self.lblref8.grid(row=8, column=0, sticky=W)
        self.txtref8=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.Salary)
        self.txtref8.grid(row=8, column=1)

        self.lblref9 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Gender: ", padx= 2, pady=6)
        self.lblref9.grid(row=9, column=0, sticky=W)
        self.txtref9=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.gender)
        self.txtref9.grid(row=9, column=1)
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
# =========================================ScrollBar======================================
        scroll_x = ttk.Scrollbar(showDataFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(showDataFrame, orient=VERTICAL)

        self.tree=ttk.Treeview(showDataFrame, column=("No", "ID", "Name","Gender" ,"DateOfBirth", "StartDate", "EndDate", "PhoneNumber", "Email", "Salary")
    , xscrollcommand=scroll_y.set, yscrollcommand=scroll_x.set, selectmode="extended")
        self.tree.pack(fill=BOTH,expand=1)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.tree.xview)
        scroll_y=ttk.Scrollbar(command=self.tree.yview)

        self.tree.heading("No", text="No")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Name", text="Name")
        self.tree.heading("DateOfBirth", text="Date of birth")
        self.tree.heading("StartDate", text="Start date")
        self.tree.heading("EndDate", text="End date")
        self.tree.heading("PhoneNumber", text="Phone number")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Salary", text="Salary")

        self.tree["show"] = "headings"

        self.tree.column("No", width=50)
        self.tree.column("ID", width=100)
        self.tree.column("Gender", width=100)
        self.tree.column("Name", width=100)
        self.tree.column("DateOfBirth", width=100)
        self.tree.column("StartDate", width=100)
        self.tree.column("EndDate", width=100)
        self.tree.column("PhoneNumber", width=100)
        self.tree.column("Email", width=100)
        self.tree.column("Salary", width=100)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.showInfo()
#======================================================================
    def registerButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.ID.get()=="":
                messagebox.showerror("Error", "Staff ID must be required",parent=self.root)
            else:
                cur.execute("Select * from staff where ID=?",(self.ID.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","ID already assigned")
                else:
                    cur.execute("insert into staff (ID, NAME ,GENDER ,DOB, START_DATE , END_DATE , PHONE_NUMBER , EMAIL , SALARY ) values(?,?,?,?,?,?,?,?,?)",(
                                self.ID.get(),
                                self.Name.get(),
                                self.gender.get(),
                                self.DoB.get(),
                                self.StartDate.get(),
                                self.EndDate.get(),
                                self.PhoneNumber.get(),
                                self.Email.get(),
                                self.Salary.get()
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
            cur.execute("select * from staff")
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
        self.Name.set(row[2])
        self.gender.set(row[3])
        self.DoB.set(row[4])
        self.StartDate.set(row[5])
        self.EndDate.set(row[6])
        self.PhoneNumber.set(row[7])
        self.Email.set(row[8])
        self.Salary.set(row[9])

    def exitButton(self):
        self.exitButton = tkinter.messagebox.askyesno("Staff Information","Confirm if you want to exit")
        if self.exitButton > 0:
            self.root.destroy()
            os.system("python main.py")

    def resetButton(self):
        self.txtref1.delete(0,END)
        self.txtref2.delete(0,END)
        self.txtref3.delete(0,END)
        self.txtref4.delete(0,END)
        self.txtref5.delete(0,END)
        self.txtref6.delete(0,END)
        self.txtref7.delete(0,END)
        self.txtref8.delete(0,END)
        self.txtref9.delete(0,END)

    def updateButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.ID.get()=="":
                messagebox.showerror("Error", "Staff ID must be required",parent=self.root)
            else:
                cur.execute("Select * from staff where ID=?",(self.ID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID")
                else:
                    cur.execute("UPDATE staff SET NAME=?,GENDER=?,DOB=?,START_DATE=?,END_DATE=?,PHONE_NUMBER=?,EMAIL=?,SALARY=? WHERE ID = ?",(
                                self.Name.get(),
                                self.gender.get(),
                                self.DoB.get(),
                                self.StartDate.get(),
                                self.EndDate.get(),
                                self.PhoneNumber.get(),
                                self.Email.get(),
                                self.Salary.get(),
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
                messagebox.showerror("Error", "Staff ID must be required",parent=self.root)
            else:
                cur.execute("Select * from staff where ID=?",(self.ID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID")
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to remove?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM staff WHERE ID=?", (self.ID.get(),))
                        conn.commit()
                        messagebox.showinfo("Remove", "Remove Successfully",parent=self.root)
                        self.showInfo() 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def searchButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM STAFF WHERE ID LIKE ?", ('%' + str(self.SEARCH.get()) + '%',))
            rows=cur.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:    
                self.tree.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=staffClass(root)
    root.mainloop()