## Modules
from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
import os
from PIL import Image,ImageTk
import time
import mysql.connector

## CURRENT BALANCE    
current_balance=0.00
global user_display_father_name
global user_display_account_number

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data={'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        ## INITIALIZING PAGES IN CONTAINER
        for F in (StartPage, MenuPage, WithdrawPage,DepositPage,BalancePage,InfoPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

## START PAGE 
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        self.controller.title('Pegasus')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='abc.png'))

        heading=tk.Label(self,text='Pegasus ATM',font=('Bahnschrift Light',50,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#3d3d5c').pack()

        password_label=tk.Label(self,text=(f'Welcome {user_display_name} to Pegasus Banking'),font=('BatmanForeverAlternate',17,'bold'),bg='#3d3d5c',fg='white').pack(pady=10)

        def next_page():
            controller.show_frame('MenuPage')

        entry_button = tk.Button(self,text='Enter',font=('Bahnschrift Light',12),command=next_page,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)

        def Quit():
            self.controller.destroy()

        def popup():
            response=messagebox.askyesno('Exit','Do you want to Quit?')

            if response == 1:
                return Quit()
            else:
                return

        quit1 = tk.Button(self,text='Quit',font=('Bahnschrift Light',12),command=popup,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)


        dualtone_label=tk.Label(self, text='',font=('Bahnschrift Light',13),fg='white',bg='#33334d',anchor='n')
        dualtone_label.pack(fill='both',expand='True')

        def changescreen():
            self.controller.destroy()
            main_screen()

        def popup2():
            response=messagebox.askyesno('Exit','Do you want to use another account?')

            if response == 1:
                return changescreen()
            else:
                return

        register_login_screen = tk.Button(dualtone_label,text='Use another account',font=('Bahnschrift Light',12),command=popup2,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10,padx=10,side='bottom',anchor='e')

        ## BOTTOM FRAME 
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3).pack(fill='x',side='bottom')

        visa_photo= tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        mastercard_photo= tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        american_express_photo= tk.PhotoImage(file='american_express.png')
        american_express_label=tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image=american_express_photo

        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)


        time_label=tk.Label(bottom_frame,font=('Bahnschrift Light',12))
        time_label.pack(side='right')
        tick()

        credits=tk.Label(bottom_frame,text='@ Created and Developed by Akshay Kumar & Sakshi ',font=('Bahnschrift Light',15)).pack()

## MENU PAGE 
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='Pegasus ATM',font=('Bahnschrift Light',50,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Main Menu',font=('Bahnschrift Light',25,'bold'),fg='white',bg='#3d3d5c')
        main_menu_label.pack(pady=5)
        slection_label=tk.Label(self,text='Please make a selection',font=('Bahnschrift Light',17),fg='white',bg='#3d3d5c')
        slection_label.pack(fill='x',pady=5)

        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand='True')

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button=tk.Button(button_frame,text='Withdraw',font=('Bahnschrift Light',13),command=withdraw,relief='raised',borderwidth=3,width=30,height=4)
        withdraw_button.grid(row=0,column=0,pady=7)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button=tk.Button(button_frame,text='Deposit',font=('Bahnschrift Light',13),command=deposit,relief='raised',borderwidth=3,width=30,height=4)
        deposit_button.grid(row=1,column=0,pady=5)
        def balance():
            controller.show_frame('BalancePage')

        balance_button=tk.Button(button_frame,text='Balance',font=('Bahnschrift Light',13),command=balance,relief='raised',borderwidth=3,width=30,height=4)
        balance_button.grid(row=0,column=1,pady=7,padx=794)

        def info():
            controller.show_frame('InfoPage')

        info_button=tk.Button(button_frame,text='Personal Info',font=('Bahnschrift Light',13),command=info,relief='raised',borderwidth=3,width=30,height=4)
        info_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')


        exit_button=tk.Button(button_frame,text='Exit',font=('Bahnschrift Light',13),command=exit,relief='raised',borderwidth=3,width=30,height=4)
        exit_button.grid(row=1,column=1,pady=5)

## WITHDRAW PAGE
class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='Pegasus ATM',font=('Bahnschrift Light',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)
        choose_amount_label=tk.Label(self,text='Choose the amount you want to withdraw',font=('Bahnschrift Light',13),fg='white',bg='#3d3d5c')
        choose_amount_label.pack()
        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand='True')

        def withdraw(amount):
            global current_balance
            if amount>current_balance:
                messagebox.showwarning('WARNING','Not sufficient funds!')
                other_amount_entry.delete(0,END)
            else:

                current_balance -= amount
                messagebox.showinfo('TRANSACTION','Done Successfully!')
                other_amount_entry.delete(0,END)
                controller.shared_data['Balance'].set(current_balance)
                mydb=mysql.connector.connect(host="localhost",user="root",password='Akshay9058@')
                mycursor=mydb.cursor()
                mycursor.execute("use Pegasus")
                mycursor.execute(f"update Pegasusbank set balance ={current_balance} where card_number = {cardnumber1} ")
                mydb.commit()

                controller.show_frame('MenuPage')
 

        twenty_button=tk.Button(button_frame,text='₹20',font=('Bahnschrift Light',12),command=lambda:withdraw(20),relief='raised',borderwidth=3,width=30,height=4)
        twenty_button.grid(row=0,column=0,pady=5)

        fourty_button=tk.Button(button_frame,text='₹40',font=('Bahnschrift Light',12),command=lambda:withdraw(40),relief='raised',borderwidth=3,width=30,height=4)
        fourty_button.grid(row=1,column=0,pady=5)

        sixty_button=tk.Button(button_frame,text='₹60',font=('Bahnschrift Light',12),command=lambda:withdraw(60),relief='raised',borderwidth=3,width=30,height=4)
        sixty_button.grid(row=2,column=0,pady=5)

        eighty_button=tk.Button(button_frame,text='₹80',font=('Bahnschrift Light',12),command=lambda:withdraw(80),relief='raised',borderwidth=3,width=30,height=4)
        eighty_button.grid(row=3,column=0,pady=5)

        one_hundred_button=tk.Button(button_frame,text='₹100',font=('Bahnschrift Light',12),command=lambda:withdraw(100),relief='raised',borderwidth=3,width=30,height=4)
        one_hundred_button.grid(row=0,column=1,pady=5,padx=794)

        two_hundred_button=tk.Button(button_frame,text='₹200',font=('Bahnschrift Light',12),command=lambda:withdraw(200),relief='raised',borderwidth=3,width=30,height=4)
        two_hundred_button.grid(row=1,column=1,pady=5)

        three_hundred_button=tk.Button(button_frame,text='₹300',font=('Bahnschrift Light',12),command=lambda:withdraw(300),relief='raised',borderwidth=3,width=30,height=4)
        three_hundred_button.grid(row=2,column=1,pady=5)

        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,font=('Bahnschrift Light',12),textvariable=cash,width=28,justify='right')
        other_amount_entry.grid(row=3,column=1,pady=4,ipady=30)

        other_amount_heading=tk.Button(button_frame,text='Other amount in dollars',font=('Bahnschrift Light',13),borderwidth=0,relief='sunken',activeforeground='white',activebackground='#33334d',bg='#33334d',fg='white')
        other_amount_heading.grid(row=4,column=1)

        def other_amount(_):
            global current_balance
            try:
                val=int(cash.get())

                if int(cash.get())>current_balance:
                    messagebox.showwarning('WARNING','Not sufficient funds!')
                    other_amount_entry.delete(0,END)
                elif int(cash.get())<0:
                    messagebox.showwarning('WARNING','Invalid Input!')
                    other_amount_entry.delete(0,END)
                else:

                    current_balance -= int(cash.get())
                    controller.shared_data['Balance'].set(current_balance)
                    cash.set('')
                    messagebox.showinfo('TRANSACTION','Done Successfully!')
                    controller.show_frame('MenuPage')
                    mydb=mysql.connector.connect(host="localhost",user="root",password='Akshay9058@')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Pegasus")
                    mycursor.execute(f"update Pegasusbank set balance ={current_balance} where card_number = {cardnumber1} ")
                    mydb.commit()
            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')

        other_amount_entry.bind('<Return>',other_amount)

## DEPOSIT PAGE 
class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='Pegasus ATM',font=('Bahnschrift Light',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#3d3d5c').pack()

        enter_amount_label=tk.Label(self,text='Enter the amount you want to deposit',font=('Bahnschrift Light',13),bg='#3d3d5c',fg='white').pack(pady=10)

        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('Bahnschrift Light',12),width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            try:
                val=int(cash.get())
                if int(val)<0:
                    messagebox.showwarning('WARNING','Improper Amount Entered!')
                    cash.set('')
                else:
                    current_balance += int(val)
                    messagebox.showinfo('DEPOSITION','Done Successfully!')
                    controller.shared_data['Balance'].set(current_balance)
                    controller.show_frame('MenuPage')
                    cash.set('')
                    mydb=mysql.connector.connect(host="localhost",user="root",password='Akshay9058@')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Pegasus")
                    mycursor.execute(f"update Pegasusbank set balance ={current_balance} where card_number = {cardnumber1} ")
                    mydb.commit()

            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')


        enter_button=tk.Button(self,text='Enter',font=('Bahnschrift Light',13),command=deposit_cash,relief='raised',borderwidth=3,width=23,height=3)
        enter_button.pack(pady=10)

        two_tone_label=tk.Label(self,bg='#33334d')
        two_tone_label.pack(fill='both',expand=True)

## BALANCE PAGE
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='Pegasus ATM',font=('Bahnschrift Light',50,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(current_balance)

        balance_label = tk.Label(self, text='Balance', font=('Bahnschrift Light',35),fg='white', bg='#3d3d5c', anchor='w')
        balance_label.pack()

        upperframe=tk.Frame(self,bg='#33334d')
        upperframe.pack(fill='both',expand='True')

        balance_label = tk.Label(upperframe, textvariable=self.balance_var, font=('Bahnschrift Light',25),fg='white', bg='#33334d', anchor='w')
        balance_label.place(relx=0.5,rely=0.5,anchor=CENTER)

        button_frame=tk.Label(self,bg='#33334d')
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Menu',font=('Bahnschrift Light',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)

        def exit():
            controller.show_frame('StartPage')

        exit_button=tk.Button(button_frame,text='Exit',command=exit,font=('Bahnschrift Light',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=5)

    def on_balance_changed(self, *args):
        self.balance_var.set('Current Balance: ₹'+str(self.controller.shared_data['Balance'].get()))

class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='Pegasus ATM',font=('Bahnschrift Light',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Personal Info',font=('Bahnschrift Light',13),fg='white',bg='#3d3d5c')
        main_menu_label.pack(pady=5)

        upperframe=tk.Frame(self,bg='#33334d')
        upperframe.pack(fill='both',expand='True')

        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both')

        mydb=mysql.connector.connect(host="localhost",user="root",password='Akshay9058@')
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists Pegasus")
        mycursor.execute("use Pegasus")
        mycursor.execute(f"select password from Pegasusbank where card_number = {cardnumber1} ")
        pass_code=mycursor.fetchone()
        pass_code_read=''
        for i in pass_code:
            pass_code_read+=i
        mycursor.execute(f"select father_name from Pegasusbank where card_number={cardnumber1}")
        values=mycursor.fetchall()
        user_father_name=[]
        for i in values:
            user_father_name.append(i[0])
        user_display_father_name=str(user_father_name[0])
        mycursor.execute(f"select account_number from Pegasusbank where card_number={cardnumber1}")
        values=mycursor.fetchall()
        user_account_number=[]
        for i in values:
            user_account_number.append(i[0])
        user_display_account_number=str(user_account_number[0])
        name_info = tk.Label(upperframe, text=f'Name     : {user_display_name}', font=('Bahnschrift Light',16),fg='white', bg='#33334d')
        name_info.pack(pady=5)

        name_info = tk.Label(upperframe, text=f'Father Name     : {user_display_father_name}', font=('Bahnschrift Light',16),fg='white', bg='#33334d')
        name_info.pack(pady=5)

        account_number_info = tk.Label(upperframe, text=f'Account Number     : {user_display_account_number}', font=('Bahnschrift Light',16),fg='white', bg='#33334d')
        account_number_info.pack(pady=5)

        account_number_info = tk.Label(upperframe, text=f'Card Number     : {cardnumber1}', font=('Bahnschrift Light',16),fg='white', bg='#33334d')
        account_number_info.pack(pady=5)

        pin_info = tk.Label(upperframe, text=f'Pin     : {pass_code_read}', font=('Bahnschrift Light',16),fg='white', bg='#33334d')
        pin_info.pack(pady=5)

        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Menu',command=exit,font=('Bahnschrift Light',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=20,padx=10)

## CLASS  DEFINE FUNCTION
def abcd():

        app = SampleApp()
        app.mainloop()

def password_not_recognised():
  messagebox.showwarning('WARNING',('Invalid Password!'))

## ABOUT SCREEN
def about():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("About")
  screen3.geometry("380x90+750+230")
  screen3.state('zoomed')
  screen3.configure(bg='white')
  screen3.iconphoto(False,tk.PhotoImage(file='abc.png'))
  photo = PhotoImage(file="ABOUT_SECTION.png") 
  photo1= photo.subsample(2,2)
  label = Label(screen3,image=photo1,bg='white')
  label.image = photo1
  label.pack(pady=5)
  Label(screen3,text = "Pegasus, this is an ATM Management System, that is based\n on Python Programming Language. We use MySQL to Create Database.\nIt is developed by Akshay Kumar & Sakshi as a Mini Project in Partial fulfillment\n for the award of the degree of Bachelor of Technology in Computer Science and Engineering.\nSchool of Engineering and Technology\nHemwati Nandan Bahuguna Garhwal University\nSrinagar Garhwal, Uttarakhand.",fg='white', bg = "grey", width = "300",height = "7", font = ("Bahnschrift Light", 13)).pack(side=BOTTOM)

##WARNING_SCREEN
def user_not_found():
  messagebox.showwarning('WARNING',('No AccountID Found !'))

## REGISTER USER SCREEN 
def register_user():
  global name_info
  global password_info
  global father_name_info
  global card_number_info
  global Account_number_info

  name_info = name.get()
  password_info = password.get()
  father_name_info     = father_name.get()
  card_number_info = card_number.get() 
  Account_number_info = Account_number.get()

  ## MYSQL DATABASE 
  global mycursor
  mydb=mysql.connector.connect(host="localhost",user="root",password='Akshay9058@')
  mycursor=mydb.cursor()
  mycursor.execute("create database if not exists Pegasus")
  mycursor.execute("use Pegasus")
  mycursor.execute("create table if not exists Pegasusbank(account_number int(20) ,card_number int(20) primary key,name varchar(30),father_name varchar(30),password char(20),balance char(30))")
  mydb.commit()

  mycursor.execute('select card_number from Pegasusbank')
  values=mycursor.fetchall()

  b=[]
  for i in values:
      b.append(i[0])
  if Account_number_info in b:
    messagebox.showwarning('WARNING',('AccountID already exists!'))
    password_entry.delete(0,END)
    name_entry.delete(0,END)
    card_number_entry.delete(0,END)
    father_name_entry.delete(0,END)
  elif card_number_info=='' :
        messagebox.showwarning('WARNING',('No Card Number Given!'))
        password_entry.delete(0,END)
        name_entry.delete(0,END)
        father_name_entry.delete(0,END)
  elif name_info=='' :
        messagebox.showwarning('WARNING',('No Name Given!'))
        password_entry.delete(0,END)
        father_name_entry.delete(0,END)
  elif father_name_info=='' :
        messagebox.showwarning('WARNING',('No Name Given!'))
        password_entry.delete(0,END)
  elif password_info=='' :
        messagebox.showwarning('WARNING',('No Password Given!'))
  else:
        balance_inti='0.00'
        password_entry.delete(0,END)
        name_entry.delete(0,END)
        card_number_entry.delete(0,END)
        father_name_entry.delete(0,END)
        screen1.destroy()
        mycursor.execute("insert into Pegasusbank values('"+Account_number_info+"','"+card_number_info+"','"+name_info+"','"+father_name_info+"','"+password_info+"','"+balance_inti+"')")
        mydb.commit()
        messagebox.showinfo('Registration',('Done Successfully!'))

## LOGIN VERIFY SCREEN 
def login_verify():
  global current_balance
  global cardnumber1
  global name_display
  global user_display_name
  cardnumber1 = card_number_verify.get()
  password1 = password_verify.get()

  mydb=mysql.connector.connect(host="localhost",user="root",password='Akshay9058@')
  mycursor=mydb.cursor()
  mycursor.execute("use Pegasus")
  mycursor.execute("select card_number from Pegasusbank ")
  values=mycursor.fetchall()
  user_acc=[]
  for i in values:
    user_acc.append(i[0])
        
  if str(cardnumber1)=='':
        messagebox.showwarning('WARNING',('No Accound ID Given!'))
        password_entry1.delete(0,END)
  elif str(cardnumber1).isspace():
        messagebox.showwarning('WARNING',('No Accound ID Given!'))
        card_number_entry1.delete(0, END)
        password_entry1.delete(0,END)
  elif cardnumber1.isalnum():
      if cardnumber1.isdigit():

          if int(cardnumber1) in user_acc:

              mycursor.execute(f"select password from Pegasusbank where card_number = {cardnumber1} ")
              values=mycursor.fetchall()
              mydb.commit()
              user_pass=[]
              for i in values:
                  user_pass.append(i[0])

              user_pass_1=str(user_pass[0])

              if password1=='':
                  messagebox.showwarning('WARNING',('No Password Given!'))
                  card_number_entry1.delete(0, END)
                  password_entry1.delete(0,END)
              elif password1 == str(user_pass_1) :
                  mycursor.execute(f"select name from Pegasusbank where card_number={cardnumber1}")
                  values=mycursor.fetchall()
                  user_name=[]
                  for i in values:
                    user_name.append(i[0])
                  user_display_name=str(user_name[0])
                  mydb=mysql.connector.connect(host="localhost",user="root",password='Akshay9058@')
                  mycursor=mydb.cursor()
                  mycursor.execute("use Pegasus")
                  mycursor.execute(f'select balance from Pegasusbank where card_number ={cardnumber1}')
                  values=mycursor.fetchall()
                  user_balance=[]
                  for i in values:
                    user_balance.append(i[0])
                  user_balance_1=float(user_balance[0])
                  current_balance=user_balance_1

                  screen2.destroy()
                  screen.destroy()

                  abcd()
 
              elif password1!= str(user_pass_1):
                  password_not_recognised()
          else:
              user_not_found()
      else:
          user_not_found()

  else:
        user_not_found()

## REGISTER DISPLAY SCREEN
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("380x470+750+230")
  screen1.state('zoomed')
  screen1.configure(bg='white')
  screen1.iconphoto(False,tk.PhotoImage(file='abc.png'))

  photo = PhotoImage(file="login_person.png")
  label = Label(screen1,image=photo,bg='white')
  label.image = photo
  label.pack(pady=5)

  global password
  global name
  global father_name
  global card_number
  global Account_number

  global password_entry
  global name_entry
  global father_name_entry
  global card_number_entry
  global Account_number_entry

  username      = StringVar()
  password      = StringVar()
  name          = StringVar()
  father_name   = StringVar()
  card_number   = StringVar()
  Account_number = StringVar() 
  
  Label(screen1, text = "Please Enter Details Below To Register",bg='white',font = ("Bahnschrift Light", 15,'bold')).pack()

  Label(screen1,text = "",bg='white',).pack()
  Label(screen1, text = "Name",font = ("Bahnschrift Light", 12),bg='white').pack()
  name_entry = Entry(screen1,bg='ghostwhite',font = ("Bahnschrift Light",12), textvariable = name)
  name_entry.pack()
  
  Label(screen1,text = "",bg='white',).pack()
  Label(screen1, text = "Father's Name",font = ("Bahnschrift Light", 12),bg='white').pack()
  father_name_entry = Entry(screen1,bg='ghostwhite',font = ("Bahnschrift Light",12), textvariable = father_name)
  father_name_entry.pack()
  
  Label(screen1,text = "",bg='white',).pack()
  Label(screen1, text = "Enter Card No.",font = ("Bahnschrift Light", 12),bg='white').pack()
  card_number_entry = Entry(screen1,bg='ghostwhite',font = ("Bahnschrift Light",12), textvariable = card_number)
  card_number_entry.pack()
  
  Label(screen1,text = "",bg='white',).pack()
  Label(screen1, text = "Enter Account No.",font = ("Bahnschrift Light", 12),bg='white').pack()
  Account_number_entry = Entry(screen1,bg='ghostwhite',font = ("Bahnschrift Light",12), textvariable = Account_number)
  Account_number_entry.pack()
  
  Label(screen1,text = "",bg='white',).pack()

  Label(screen1, text = "Pin",font = ("Bahnschrift Light", 12),bg='white').pack()
  password_entry =  Entry(screen1,bg='ghostwhite',font = ("Bahnschrift Light",12), textvariable = password)
  password_entry.config(fg='black',show='●')
  password_entry.pack()

  Label(screen1, text = "",bg='white').pack()

  img1 = PhotoImage(file="REGISTER.png")
  photoimage1 = img1.subsample(2, 2)
  img1Btn = Button(screen1,command = register_user,image=photoimage1,bg='white',activebackground='white',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()

  img1 = PhotoImage(file="EXIT.png")
  photoimage1 = img1.subsample(2, 2)
  img1Btn = Button(screen1,command = quit,image=photoimage1,bg='white',activebackground='white',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack(side=LEFT)

## LOGIN DISPLAY SCREEN
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("380x470+750+230")
  screen2.state('zoomed')
  screen2.configure(bg='white')
  screen2.iconphoto(False,tk.PhotoImage(file='abc.png'))

  photo = PhotoImage(file="login_person.png")
  label = Label(screen2,image=photo,bg='white')
  label.image = photo
  label.pack(pady=5)
  
  Label(text = "",bg='white',).pack()
  Label(screen2, text = "Please Enter Details Below To Login",bg='white',font = ("Bahnschrift Light", 15,'bold')).pack()
  Label(screen2, text = "",bg='white').pack()

  global card_number_verify
  global password_verify

  card_number_verify = StringVar()
  password_verify = StringVar()

  global card_number_entry1
  global password_entry1

  Label(screen2, text = "Enter Your Card Number",bg='white',font = ("Bahnschrift Light", 12)).pack()
  card_number_entry1 = Entry(screen2,bg='ghostwhite',font = ("Bahnschrift Light",12) ,textvariable = card_number_verify)
  card_number_entry1.pack()

  Label(screen2, text = "",bg='white').pack()
  Label(screen2, text = "Enter Your Pin",bg='white',font = ("Bahnschrift Light", 12)).pack()
  password_entry1 = Entry(screen2,bg='ghostwhite',font = ("Bahnschrift Light",12), textvariable = password_verify)
  password_entry1.config(fg='black',show='●')
  password_entry1.pack()
  Label(screen2, text = "",bg='white').pack()

  img1 = PhotoImage(file ="LOGIN.png")
  photoimage1 = img1.subsample(2, 2)
  img1Btn = Button(screen2,command = login_verify,image=photoimage1,bg='white',activebackground='white',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()

  img1 = PhotoImage(file="EXIT.png")
  photoimage1 = img1.subsample(2, 2)
  img1Btn = Button(screen2,command = quit,image=photoimage1,bg='white',activebackground='white',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack(side=LEFT)

##REGISTER/LOGIN SCREEN 
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("530x530+450+120")
  screen.state('zoomed')
  screen.title("Pegasus")
  screen.configure(bg='white')
  screen.iconphoto(False,tk.PhotoImage(file='abc.png'))

  Label(text = " ATM Managment System®",fg='white', bg = "grey", width = "300", height = "1", font = ("Bahnschrift Light", 15)).pack(side=BOTTOM)
  Label(text = "",bg='white').pack()

  img = ImageTk.PhotoImage(Image.open("p.png"))
  panel = Label(screen, image = img,bg='white')
  panel.pack() 

  Label(text = "",bg='white',).pack()
  photo1 = PhotoImage(file="LOGIN.png")
  photoimage1 = photo1.subsample(1, 1)
  Button(command = login,bg='white',activebackground='white',relief=FLAT,image = photoimage1).pack(pady=5)
  Label(text = "",bg='white',).pack()

  photo2 = PhotoImage(file="REGISTER.png")
  photoimage2 = photo2.subsample(1, 1)
  Button(command = register,bg='white',activebackground='white',relief=FLAT,image = photoimage2).pack(pady=5)
  Label(text = "",bg='white').pack()

  photo3 = PhotoImage(file="ABOUT.png")
  photoimage3 = photo3.subsample(2, 2)
  Button(command = about,bg='white',activebackground='white',relief=FLAT,image = photoimage3).pack(side=RIGHT)
  photo4 = PhotoImage(file="EXIT.png")
  photoimage4 = photo4.subsample(2, 2)
  Button(command = quit,bg='white',activebackground='white',relief=FLAT,image = photoimage4).pack(side=LEFT)
  
  screen.mainloop()

## SPLASH SCREEN
splash_root = Tk()
splash_root.geometry("3000x2000")
# splash_root.attributes('-fullscreen',True)
splash_root.state('zoomed')
splash_root.title("Initialisation Screen")
splash_root.configure(bg='white')
splash_root.iconphoto(False,tk.PhotoImage(file='abc.png'))
Label(text = "",bg='white').pack()
Label(text = "",bg='white').pack()
img = ImageTk.PhotoImage(Image.open("p.png"))
panel = Label(image = img,bg='white')
panel.pack() 
Label(text = "Welcome to the Pegasus, this is an ATM Management System, that is based\n on Python Programming Language. We use MySQL to Create Database. It is\n developed by Akshay Kumar & Sakshi as a Mini Project in Partial fulfillment\n for the award of the degree of Bachelor of Technology in Computer Science\n and Engineering, Hemwati Nandan Bahuguna Garhwal University, Srinagar\n Garhwal Uttarakhand.",fg='white', bg = "grey", width = "300",height = "7", font = ("Bahnschrift Light", 15,'bold')).pack(side=BOTTOM)
Label(text = "",bg='white').pack()

# main window function
def main():
	splash_root.destroy()
	main_screen()

splash_root.after(5000,main)

mainloop()

