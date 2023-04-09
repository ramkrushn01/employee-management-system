from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Employee Management System')

        # Variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designition = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()



        lbl_title = Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        # logo
        # img_logo = Image.open('Image/maingrp.png')
        # img_logo = img_logo.resize((50,50),Image.ANTIALIAS)
        # self.photo_logo = ImageTk.PhotoImage(img_logo)

        # self.logo = Label(self.root,image=self.photo_logo)
        # self.logo.place(x=270,y=0,width=50,height=50)

        # IMG FRAME
        img_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1st
        # img1 = Image.open('Image/office01.png')
        # img1 = img1.resize((540,160),Image.ANTIALIAS)
        # self.photo1 = ImageTk.PhotoImage(img1)

        # self.img_1 = Label(img_frame,image=self.photo1)
        # self.img_1.place(x=0,y=0,width=540,height=160)

        # 2st
        # img2 = Image.open('Image/office02.png')
        # img2 = img2.resize((540,160),Image.ANTIALIAS)
        # self.photo2 = ImageTk.PhotoImage(img2)

        # self.img_2 = Label(img_frame,image=self.photo2)
        # self.img_2.place(x=540,y=0,width=540,height=160)

        # 3rd
        # img3 = Image.open('Image/office03.jpg')
        # img3 = img3.resize((540,160),Image.ANTIALIAS)
        # self.photo3 = ImageTk.PhotoImage(img3)

        # self.img_3 = Label(img_frame,image=self.photo3)
        # self.img_3.place(x=1080,y=0,width=540,height=160)


        # main Frame 
        Main_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)

        # upper frame 
        upper_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels and Entry fields 
        lbl_dep = Label(upper_frame,text='Department',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        # dep
        combo_dep = ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=20,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Enginner','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Name 
        lbl_Name = Label(upper_frame,text='Name:',font=('arial',11,'bold'),bg='white')
        lbl_Name.grid(row=0,column=2,padx=2,pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        # lbl_designition 
        lbl_Designition = Label(upper_frame,font=('arial',11,'bold'),text='Designition:',bg='white')
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition = ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=('arial',11,'bold'))
        txt_Designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # Email 
        lbl_email = Label(upper_frame,font=('arial',11,'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email = ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',11,'bold'))
        txt_email.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        # Address
        lbl_Address = Label(upper_frame,font=('arial',11,'bold'),text='Address:',bg='white')
        lbl_Address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_Address = ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_Address.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # Married 
        lbl_merried_status = Label(upper_frame,font=('arial',11,'bold'),text='Married Status:',bg='white')
        lbl_merried_status.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_married = ttk.Combobox(upper_frame,textvariable=self.var_married,state='readonly',font=('arial',11,'bold'),width=18)
        com_txt_married['value'] = ('Marrid','Unmarried')
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #  1:01:00
        # Dob 
        lbl_dob = Label(upper_frame,font=('arial',11,'bold'),text='DOB:',bg='white')
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob = ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=3,column=1,sticky=W,padx=2,pady=7)


        # DOJ 
        lbl_doj = Label(upper_frame,font=('arial',11,'bold'),text='DOJ:',bg='white')
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj = ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',11,'bold'))
        txt_doj.grid(row=3,column=3,sticky=W,padx=2,pady=7)
        

        # ID_Proof
        com_txt_proof = ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state='readonly',font=('arial',11,'bold'),width=22)
        com_txt_proof['value'] = ('Select ID Proof','PAN CARD','ADHAR CARD','DRIVING LICENCE')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_proof = ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=('arial',11,'bold'))
        txt_proof.grid(row=4,column=1,sticky=W,padx=2,pady=7)

        # gender 
        lbl_gender = Label(upper_frame,font=('arial',11,'bold'),text='Gender',bg='white')
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        com_txt_gender = ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',11,'bold'),state='readonly',width=20)
        com_txt_gender['value'] = ('Male','Female','Other')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        # phone
        lbl_phone = Label(upper_frame,font=('arial',11,'bold'),text='Phone No:',bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone = ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        # Country
        lbl_country = Label(upper_frame,font=('arial',11,'bold'),text='Country:',bg='white')
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country = ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        # CTC
        lbl_ctc = Label(upper_frame,font=('arial',11,'bold'),text='Salary(CTC)',bg='white')
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc = ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
        txt_ctc.grid(row=2,column=5,sticky=W,padx=2,pady=7)


        # mask image
        
        # imgmask = Image.open('Image/mask.jpg')
        # imgmask = imgmask.resize((220,220),Image.ANTIALIAS)
        # self.photomask = ImageTk.PhotoImage(imgmask)

        # self.img_mask = Label(upper_frame,image=self.photomask)
        # self.img_mask.place(x=1000,y=0,width=220,height=220)
        
        # Button Frame 
        button_frame = Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1290,y=10,width=170,height=210)

        # 1btn
        btn_add = Button(button_frame,text='Save',font=('arial',15,'bold'),width=13,bg='blue',fg='white',command=self.add_data)
        btn_add.grid(row=0,column=0,sticky=W,padx=1,pady=5)

        # 2btn
        btn_update = Button(button_frame,text='Update',font=('arial',15,'bold'),width=13,bg='blue',fg='white',command=self.update_data)
        btn_update.grid(row=1,column=0,sticky=W,padx=1,pady=5)

        #3btn
        btn_delete = Button(button_frame,text='Delete',font=('arial',15,'bold'),width=13,bg='blue',fg='white',command=self.delete_data)
        btn_delete.grid(row=2,column=0,sticky=W,padx=1,pady=5)

        # 4btn
        btn_clear = Button(button_frame,text='Clear',font=('arial',15,'bold'),width=13,bg='blue',fg='white',command=self.reset_data)
        btn_clear.grid(row=3,column=0,sticky=W,padx=1,pady=5)

        
        


        # down frame 
        down_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        #  Search frame
        search_frame = LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by = Label(search_frame,font=('Arial',11,'bold'),text='Search by:',fg='white',bg='red')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # search 
        self.var_com_search  = StringVar()
        com_txt_search = ttk.Combobox(search_frame,textvariable=self.var_com_search,state='readonly',font=('arial',12,'bold'),width=22)
        com_txt_search['value']=('Select Option','Phone','id_proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('Arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn__search = Button(search_frame,text='Search',font=('Arial',11,'bold'),width=14,bg='blue',fg='white',command=self.search_data)
        btn__search.grid(row=0,column=3,padx=5)

        btn_ShowAll = Button(search_frame,text='Show All',font=('Arial',11,'bold'),width=14,bg='blue',fg='white',command=self.fectch_data)
        btn_ShowAll.grid(row=0,column=4,padx=5)

        # stayhome = Label(search_frame,text='Manoj Bhosale',font=('monospace',10,'bold'),bg='white',fg='red')
        # stayhome.place(x=780,y=0,width=600,height=30)

        # =================== Employee table =======================
        # Table Frame
        table_frame = Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame,columns=('dep','name','degi','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        emp_details = ['dep','name','degi','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','salary']
        emp_details_value = ['Department','Name','Degignition','Email','Address','Married Status','DOB','DOJ','ID Type','ID Proof','Genter','Phone','country','Salary']
        
        # for i in range(len(emp_details_value)):
        #     self.employee_table.heading(emp_details[i],text=emp_details_value[i])

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Degignition')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show'] = 'headings'
        for i in emp_details:
            self.employee_table.column(i,width=100)

        self.employee_table.pack(fill=BOTH,expand=True)
        self.employee_table.bind('<ButtonRelease>',self.get_cursor)

        self.fectch_data()


    # ***************Function Declaration*****************

    def add_data(self):
        if self.var_dep.get()=='' or self.var_email.get()=='':
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost',port=3306,user='root',password='ramkrushn@123,./',database='mydata')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_dep.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_designition.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_married.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_doj.get(),
                                                                                                            self.var_idproofcomb.get(),
                                                                                                            self.var_idproof.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_country.get(),
                                                                                                            self.var_salary.get(),
                                                                                                            ))
                conn.commit()
                self.fectch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
    
    # Fetch data
    def fectch_data(self):        
        conn = mysql.connector.connect(host='localhost',port=3306,user='root',password='ramkrushn@123,./',database='mydata')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from  employee1')
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert('',END,values=i)
            conn.commit()

        conn.close()
    
    # Get Cursor
    def get_cursor(self,event=''):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
    
    def update_data(self):
        if self.var_dep.get()=='' or self.var_email.get()=='':
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                update=messagebox.askyesno('update','Are You Sure Update This Employee Data')
                if update>0:
                    conn = mysql.connector.connect(host='localhost',port=3306,user='root',password='ramkrushn@123,./',database='mydata')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,Id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where Id_proof=%s',(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_designition.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_married.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_doj.get(),
                                                                                                            self.var_idproofcomb.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_country.get(),
                                                                                                            self.var_salary.get(),
                                                                                                            self.var_idproof.get()

                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fectch_data()
                conn.close()
                messagebox.showinfo('Success','Employee Successfuly Updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
    # Delete 
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                Delete = messagebox.askyesno('Delete','Are You Sure Delete this Employee',parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host='localhost',port=3306,user='root',password='ramkrushn@123,./',database='mydata')
                    my_cursor = conn.cursor()
                    sql = 'delete from employee1 where id_proof=%s'
                    value = (self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fectch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Successfuly Delected',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)

    # Reset
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_name.set('')
        self.var_designition.set('')
        self.var_email.set('')
        self.var_address.set('')
        self.var_married.set('Married')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_idproofcomb.set('Select ID proof')
        self.var_gender.set('Male')
        self.var_phone.set('')
        self.var_country.set('')
        self.var_salary.set('')
        self.var_idproof.set('')


    # Search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search == '':
            messagebox.showerror('Error','Please Select Option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost',port=3306,user='root',password='ramkrushn@123,./',database='mydata')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

                




if __name__=='__main__':
    root = Tk()
    obj = Employee(root)
    root.mainloop()

