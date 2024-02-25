from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox
import sqlite3
from tkinter import ttk, messagebox
import customtkinter
import os
class ProductClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Tool Store")
        self.root.geometry("1400x700+0+0")
        root.iconbitmap(r"favicon (1).ico")

    #================================Variables============================================
        self.SEARCH = StringVar()
        self.release_date = StringVar()
        self.productID = StringVar()
        self.brand = StringVar()
        self.size = StringVar()
        self.color = StringVar()
        self.material = StringVar()
        self.companyID=StringVar()
        self.selling_price = StringVar()
        self.product_name = StringVar()
        self.account_bank = StringVar()



        title = Label(self.root,bd=20, relief=RIDGE, text="PRODUCTS", fg="black", bg="white", font=("Time New Roman", 40, "bold"))
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
    #=========================Search===================================
        lbl_txtSearch = customtkinter.CTkEntry(master=smallWindow, width=220,height=55,placeholder_text="Enter ID",textvariable=self.SEARCH,font=("Time New Roman", 24, "bold"))
        lbl_txtSearch.grid(row=5, column=0, pady=7)

        searchStaffButton = Button(smallWindow, width=18,height=2, text="SEARCH", bg="white", fg="black", font=("Time New Roman", 15, "bold"),command=self.searchButton)
        searchStaffButton.grid(row=2, column=0, pady=7)

    # =========================DataFrameLeft======================
        self.lblref1 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Product ID: ")
        self.lblref1.grid(row=1, column=0, sticky=W)
        self.txtref1=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40, textvariable=self.productID)
        self.txtref1.grid(row=1, column=1)

        self.lblref2 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Release Date: ", padx= 2, pady=6)
        self.lblref2.grid(row=2, column=0, sticky=W)
        self.txtref2=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.release_date)
        self.txtref2.grid(row=2, column=1)
        
        self.lblref3 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Brand: ", padx= 2, pady=6)
        self.lblref3.grid(row=3, column=0, sticky=W)
        self.txtref3=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.brand)
        self.txtref3.grid(row=3, column=1)

        self.lblref4 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Size: ", padx= 2, pady=6)
        self.lblref4.grid(row=4, column=0, sticky=W)
        self.txtref4=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.size)
        self.txtref4.grid(row=4, column=1)

        self.lblref5 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Color: ", padx= 2, pady=6)
        self.lblref5.grid(row=5, column=0, sticky=W)
        self.txtref5=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.color)
        self.txtref5.grid(row=5, column=1)

        self.lblref6 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Material: ", padx= 2, pady=6)
        self.lblref6.grid(row=6, column=0, sticky=W)
        self.txtref6=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.material)
        self.txtref6.grid(row=6, column=1)

        self.lblref7 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Selling Price: ", padx= 2, pady=6)
        self.lblref7.grid(row=7, column=0, sticky=W)
        self.txtref7=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.selling_price)
        self.txtref7.grid(row=7, column=1)

        self.lblref8 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Product Name: ", padx= 2, pady=6)
        self.lblref8.grid(row=8, column=0, sticky=W)
        self.txtref8=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.product_name)
        self.txtref8.grid(row=8, column=1)

        self.lblref9 = Label(DataframeLeft, font=("Time New Roman", 15, "bold"), text="Company ID: ", padx= 2, pady=6)
        self.lblref9.grid(row=9, column=0, sticky=W)
        self.txtref9=Entry(DataframeLeft,font=("Time New Roman", 15, "bold"), width=40,textvariable=self.companyID)
        self.txtref9.grid(row=9, column=1)

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
                        #======================Table=======================
    #=========================================ScrollBar======================================
        scroll_x = ttk.Scrollbar(showDataFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(showDataFrame, orient=VERTICAL)
        self.staff_table=ttk.Treeview(showDataFrame, column=("No", 
         "ProductID","ReleaseDate","Brand", "Size", "Color", "Material", "SellingPrice", "ProductName", "CompanyID")
        , xscrollcommand=scroll_y.set, yscrollcommand=scroll_x.set)

        self.staff_table.pack(fill=BOTH, expand=1)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.staff_table.xview)
        scroll_y=ttk.Scrollbar(command=self.staff_table.yview)

        self.staff_table.heading("No", text="No.", )
        self.staff_table.heading("ProductID", text="Product ID")
        self.staff_table.heading("ReleaseDate", text="Release Date")
        self.staff_table.heading("Brand", text="Brand")
        self.staff_table.heading("Size", text="Size")
        self.staff_table.heading("Color", text="Color")
        self.staff_table.heading("Material", text="Material")
        self.staff_table.heading("SellingPrice", text="Selling Price")
        self.staff_table.heading("ProductName", text="Product Name")
        self.staff_table.heading("CompanyID", text="Company ID")
        


        self.staff_table["show"] = "headings"

        self.staff_table.column("No", width=100)
        self.staff_table.column("ProductID", width=100)
        self.staff_table.column("ReleaseDate", width=100)
        self.staff_table.column("Brand", width=100)
        self.staff_table.column("Size", width=100)
        self.staff_table.column("Color", width=100)
        self.staff_table.column("Material",  width=100)
        self.staff_table.column("SellingPrice", width=100)
        self.staff_table.column("ProductName", width=100)
        self.staff_table.column("CompanyID", width=100)

        self.staff_table.bind("<Double-1>", self.OnDoubleClick)
        self.showInfo()

    def registerButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            if self.productID.get()=="":
                messagebox.showerror("Error", " productID must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM PRODUCTS WHERE PRODUCT_ID=?",(self.productID.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Status already assigned")
                else:
                    cur.execute("INSERT INTO PRODUCTS (PRODUCT_ID , RELEASE_DATE, BRAND , SIZE , COLOR , MATERIAL , SELLING_PRICE , PRODUCT_NAME , COMPANY_ID ) values(?,?,?,?,?,?,?,?,?)",(
                                self.productID.get(),
                                self.release_date.get(),
                                self.brand.get(),
                                self.size.get(),
                                self.color.get(),
                                self.material.get(),
                                self.selling_price.get(),
                                self.product_name.get(),
                                self.companyID.get()
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
            cur.execute("select * from PRODUCTS")
            rows=cur.fetchall()
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:    
                self.staff_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
  
    def OnDoubleClick(self,ev):
        x=self.staff_table.focus()
        content=self.staff_table.item(x)
        row=content['values']
        print(row)
        self.productID.set(row[1])
        self.release_date.set(row[2])
        self.brand.set(row[3])
        self.size.set(row[4])
        self.color.set(row[5])
        self.material.set(row[6])
        self.selling_price.set(row[7])
        self.product_name.set(row[8])
        self.account_bank.set(row[9])
    
    def exitButton(self):
        self.exitButton = tkinter.messagebox.askyesno("products Information","Confirm if you want to exit")
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
            if self.productID.get()=="":
                messagebox.showerror("Error", "Product ID must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM PRODUCTS WHERE PRODUCT_ID=?",(self.productID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID")
                else:
                    cur.execute("UPDATE PRODUCTS SET RELEASE_DATE=? , BRAND=? , SIZE=? , COLOR=? , MATERIAL=? , SELLING_PRICE=? , PRODUCT_NAME=? , COMPANY_ID=? WHERE PRODUCT_ID = ?",(
                                self.release_date.get(),
                                self.brand.get(),
                                self.size.get(),
                                self.color.get(),
                                self.material.get(),
                                self.selling_price.get(),
                                self.product_name.get(),
                                self.companyID.get(),
                                self.productID.get()
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
            if self.productID.get()=="":
                messagebox.showerror("Error", "Product ID must be required",parent=self.root)
            else:
                cur.execute("Select * from PRODUCTS where PRODUCT_ID=?",(self.productID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Shipper ID")
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to remove?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM PRODUCTS WHERE PRODUCT_ID=?", (self.productID.get(),))
                        conn.commit()
                        messagebox.showinfo("Remove", "Remove Successfully",parent=self.root)
                        self.showInfo() 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def searchButton(self):
        conn=sqlite3.connect(database=r'toolStore.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM PRODUCTS WHERE PRODUCT_ID LIKE ?", ('%' + str(self.SEARCH.get()) + '%',))
            rows=cur.fetchall()
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:    
                self.staff_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)




if __name__=="__main__":
  root=Tk()
  obj=ProductClass(root)
  root.mainloop()