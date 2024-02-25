from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox
import sqlite3
from tkinter import ttk, messagebox
import customtkinter
import os
class orderClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Tool Store")
        self.root.iconbitmap(r"favicon (1).ico")
#========================varibles=========================
        self.SEARCH = StringVar()
        self.orderID = StringVar()
        self.status = StringVar()
        self.ProductID = StringVar()
        self.ShipperID = StringVar()
        self.UserID = StringVar()
        self.StaffID = StringVar()
        self.Quantity = StringVar()   
        self.OrderDate = StringVar()
        self.AccountBank = StringVar()
    
        #=======================Title======================
        title = Label(root,bd=20, relief=RIDGE, text="ORDER", fg="black", bg="white", font=("Time New Roman", 40, "bold"))
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

#============SEARCH=======================

        lbl_txtSearch = customtkinter.CTkEntry(master=smallWindow, width=220,height=55,placeholder_text="Enter ID",textvariable=self.SEARCH,font=("Time New Roman", 24, "bold"))
        lbl_txtSearch.grid(row=5, column=0, pady=7)

        searchStaffButton = Button(smallWindow, width=18,height=2, text="SEARCH", bg="white", fg="black", font=("Time New Roman", 15, "bold"),command=self.searchButton)
        searchStaffButton.grid(row=2, column=0, pady=7)
#===========================content============================
        self.lblref0=Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Order ID: ")
        self.lblref0.grid(row=1, column=0, sticky=W)
        self.txtref0=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.orderID)
        self.txtref0.grid(row=1, column=1)

        self.lblref1=Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="status: ")
        self.lblref1.grid(row=2,column=0, sticky=W)
        self.txtref1=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.status)
        self.txtref1.grid(row=2, column=1)

        self.lblref2=Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Product ID: ", padx= 2, pady=6)
        self.lblref2.grid(row=3, column=0, sticky=W)
        self.txtref2=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.ProductID)
        self.txtref2.grid(row=3, column=1)

        self.lblref3 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Shipper ID: ", padx= 2, pady=6)
        self.lblref3.grid(row=4, column=0, sticky=W)
        self.txtref3=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.ShipperID)
        self.txtref3.grid(row=4, column=1)

        self.lblref4 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="User ID: ", padx= 2, pady=6)
        self.lblref4.grid(row=5, column=0, sticky=W)
        self.txtref4=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.UserID)
        self.txtref4.grid(row=5, column=1)

        self.lblref5 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Staff ID: ", padx= 2, pady=6)
        self.lblref5.grid(row=6, column=0, sticky=W)
        self.txtref5=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.StaffID)
        self.txtref5.grid(row=6, column=1)

        self.lblref6 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Quantity: ", padx= 2, pady=6)
        self.lblref6.grid(row=7, column=0, sticky=W)
        self.txtref6=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.Quantity)
        self.txtref6.grid(row=7, column=1)

        self.lblref7 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Order Date: ", padx= 2, pady=6)
        self.lblref7.grid(row=8, column=0, sticky=W)
        self.txtref7=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.OrderDate)
        self.txtref7.grid(row=8, column=1)

        self.lblref8 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Account Bank: ", padx= 2, pady=6)
        self.lblref8.grid(row=9, column=0, sticky=W)
        self.txtref8=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.AccountBank)
        self.txtref8.grid(row=9, column=1)

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

        self.tree=ttk.Treeview(showDataFrame, column=("No","orderID", "status", "ProductID","ShipperID","UserID","StaffID","Quantity","OrderDate","AccountBank")
    , xscrollcommand=scroll_y.set, yscrollcommand=scroll_x.set, selectmode="extended")
        self.tree.pack(fill=BOTH,expand=1)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.tree.xview)
        scroll_y=ttk.Scrollbar(command=self.tree.yview)

        self.tree.heading("No", text="No")
        self.tree.heading("orderID", text="order ID")
        self.tree.heading("status", text="status")
        self.tree.heading("ProductID", text="Product ID")
        self.tree.heading("ShipperID", text="Shipper ID")
        self.tree.heading("UserID", text="User ID")
        self.tree.heading("StaffID", text="Staff ID")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("OrderDate", text="Order Date")
        self.tree.heading("AccountBank", text="Account Bank")

        self.tree["show"] = "headings"

        self.tree.column("No", width=50)
        self.tree.column("orderID", width=50)
        self.tree.column("status", width=100)
        self.tree.column("ProductID", width=100)
        self.tree.column("ShipperID", width=100)
        self.tree.column("UserID", width=100)
        self.tree.column("StaffID", width=100)
        self.tree.column("Quantity", width=100)
        self.tree.column("OrderDate", width=100)
        self.tree.column("AccountBank", width=100)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.showInfo()
#======================================================================
    def registerButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.orderID.get()=="":
                messagebox.showerror("Error", "Order orderID must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM ORDERS WHERE ORDER_ID=?",(self.orderID.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Status already assigned")
                else:
                    cur.execute("INSERT INTO ORDERS (ORDER_ID , STATUS ,PRODUCT_ID ,SHIPPER_ID , USER_ID , STAFF_ID , QUANTITY , ORDER_DATE ,ACCOUNT_BANK ) values(?,?,?,?,?,?,?,?,?)",(
                                self.orderID.get(),
                                self.status.get(),
                                self.ProductID.get(),
                                self.ShipperID.get(),
                                self.UserID.get(),
                                self.StaffID.get(),
                                self.Quantity.get(),
                                self.OrderDate.get(),
                                self.AccountBank.get()
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
            cur.execute("SELECT * FROM ORDERS ")
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
        self.orderID.set(row[1])
        self.status.set(row[2])
        self.ProductID.set(row[3])
        self.ShipperID.set(row[4])
        self.UserID.set(row[5])
        self.StaffID.set(row[6])
        self.Quantity.set(row[7])
        self.OrderDate.set(row[8])
        self.AccountBank.set(row[9])
        

    def exitButton(self):
        self.exitButton = tkinter.messagebox.askyesno("Order Information","Confirm if you want to exit")
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
        self.txtref0.delete(0,END)
        
        

    def updateButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.orderID.get()=="":
                messagebox.showerror("Error", "orderID must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM ORDERS WHERE ORDER_ID=?",(self.orderID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid OrderID")
                else:
                    cur.execute("UPDATE ORDERS SET STATUS=?,PRODUCT_ID=?,SHIPPER_ID=?,USER_ID=?,STAFF_ID=?,QUANTITY=?,ORDER_DATE=?,ACCOUNT_BANK=? WHERE ORDER_ID=? ",(
                                self.status.get(),
                                self.ProductID.get(),
                                self.ShipperID.get(),
                                self.UserID.get(),
                                self.StaffID.get(),
                                self.Quantity.get(),
                                self.OrderDate.get(),
                                self.AccountBank.get(),
                                self.orderID.get()
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
            if self.orderID.get()=="":
                messagebox.showerror("Error", "Order ID must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM ORDERS WHERE ORDER_ID=?",(self.orderID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Order ID")
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to remove?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM ORDERS WHERE ORDER_ID=?", (self.orderID.get(),))
                        conn.commit()
                        messagebox.showinfo("Remove", "Remove Successfully",parent=self.root)
                        self.showInfo() 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def searchButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM ORDERS WHERE ORDER_ID LIKE ?", ('%' + str(self.SEARCH.get()) + '%',))
            rows=cur.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:    
                self.tree.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=orderClass(root)
    root.mainloop()