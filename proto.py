
import tkinter as tk
from tkinter import ttk, Menu, SUNKEN , LEFT , RIGHT , TOP, BOTTOM
import sqlite3



root = tk.Tk()
root.geometry("1000x700")
def showorder_frame():
    order_frame.tkraise()
def showcheckoutframe():
    checkoutframe.tkraise()
def showsignupframe():
    signup_frame.tkraise()
def showlogin_frame():
    login_frame.tkraise()
def showhome_frame():
    home_frame.tkraise()
def showcollection_frame():
    collection_frame.tkraise()

def showabout_frame():
    about_frame.tkraise()

def showfaq_frame():
    faq_frame.tkraise()

def stock_database():
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hot_choc NUM NOT NULL,
    coffee NUM NOT NULL

    )
    ''')



def admin_database():
    conn = sqlite3.connect('admins.db')  # creates database
    c = conn.cursor()
    c.execute('''
       CREATE TABLE IF NOT EXISTS admins (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           email TEXT NOT NULL,
           password TEXT NOT NULL,
           name TEXT NOT NULL,
           lastname TEXT NOT NULL,
           address TEXT NOT NULL,
           postcode TEXT NOT NULL
       )
   ''')
    conn = sqlite3.connect('admins.db')
    c = conn.cursor()
    c.execute('''
            INSERT INTO admins (email, password, name, lastname, address, postcode)
            VALUES ('herby@gmail.com','H4RVEY2006','harvey','nicholas','16 windsor place','CF417JH')
            ''')
    conn.commit()  # Save changes to the database
    print("Added to database")
    conn.close()


def stockdb():
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO stock (hot_choc, coffee)
        VALUES (10,10)
        ''')
    conn.commit()  # Save changes to the database
    print("Added to database")
    conn.close()




def signup_database():
     conn = sqlite3.connect('signup_database.db') # creates database
     c = conn.cursor()
     c.execute('''
        CREATE TABLE IF NOT EXISTS signup (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            lastname TEXT NOT NULL,
            address TEXT NOT NULL,
            postcode TEXT NOT NULL
        )
    ''')


def validateentry():
    email = login_email_entry.get()
    password = login_password_entry.get()
    name = signup_name1_entry.get()
    lastname = signup_name2_entry.get()
    address = address_entry.get()
    postcode = Postcode_entry.get()
    if email == '' or password == '' or name == '' or lastname == '' or address == '' or postcode == '':
        print("Please fill all fields")
    else:
        signupdb()


def signupdb():
    email = login_email_entry.get()
    password = login_password_entry.get()
    name = signup_name1_entry.get()
    lastname = signup_name2_entry.get()
    address = address_entry.get()
    postcode = Postcode_entry.get()
    conn = sqlite3.connect('signup_database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO signup (email, password, name, lastname, address, postcode)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (email, password, name, lastname, address, postcode))  # Insert values into the bookings table
    conn.commit()  # Save changes to the database
    print("Added to database")
    conn.close()
    showsignupframe()


def login():
    connection = sqlite3.connect('signup_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM signup')
    check = cursor.fetchall()


    for i in check:

        stored_email = i[1]
        stored_password = i[2]



        if stored_email == email_entry.get() and stored_password == password_entry.get():
            showhome_frame()

        else:
            denied = ttk.Label(signup_frame, text='incorrect details. please try again')
            denied.grid()



signup_frame = ttk.Frame(root, padding=0)
login_frame = ttk.Frame(root, padding=0)
home_frame = ttk.Frame(root, padding=0)
order_frame = ttk.Frame(root, padding=0)
collection_frame = ttk.Frame(root, padding=0)
about_frame = ttk.Frame(root, padding=0)
faq_frame = ttk.Frame(root, padding=0)
checkoutframe = ttk.Frame(root, padding=0)




signup_frame.grid(row=0,column=0,sticky="nsew")
login_frame.grid(row=0,column=0, sticky="nsew")
home_frame.grid(row=0,column=0, sticky="nsew")
order_frame.grid(row=0,column=0, sticky="nsew")
collection_frame.grid(row=0,column=0,sticky="nsew")
about_frame.grid(row=0,column=0,sticky="nsew")
faq_frame.grid(row=0,column=0,sticky="nsew")
checkoutframe.grid(row=0,column=0,sticky="nsew")


#placing it on the order frame
hotdrinks_var = tk.StringVar()
colddrinks_var = tk.StringVar()




signup_label = ttk.Label(signup_frame, text="Log in")
email_label = ttk.Label(signup_frame,text="email:")
password_label = ttk.Label(signup_frame,text="Password:")

signup_label.grid(row=0,column=0)
email_label.grid(row=1,column=0)
password_label.grid(row=3,column=0)


email_entry = ttk.Entry(signup_frame)
password_entry = ttk.Entry(signup_frame)

password_entry.grid(row=4,column=0)
email_entry.grid(row=2,column=0)

signup_button = ttk.Button(signup_frame, text="Log in",
command = login)
login_button = ttk.Button(signup_frame, text="or sign up!",
command = showlogin_frame)

signup_button.grid(row=5,column=0)
login_button.grid(row=6,column=0, pady=20)

#Login page,


signup_name1 = ttk.Label (login_frame, text= 'first name: ')
signup_name2 = ttk.Label (login_frame, text= 'Last name: ')
address_label = ttk.Label (login_frame, text='Address: ')
Postcode_label = ttk.Label(login_frame, text='Postcode: ')
login_email_label = ttk.Label(login_frame, text="Email: ")
login_password_label = ttk.Label(login_frame,text="Password: ")


signup_name1.grid(row=0, column = 0 )
signup_name2.grid(row=2, column = 0 )
address_label.grid(row=4 , column= 0)
Postcode_label.grid(row=6,column=0)
login_email_label.grid(row=8,column=0)
login_password_label.grid(row=10, column=0)


signup_name1_entry = ttk.Entry(login_frame)
signup_name2_entry = ttk.Entry(login_frame)
address_entry = ttk.Entry(login_frame)
Postcode_entry = ttk.Entry(login_frame)
login_email_entry = ttk.Entry(login_frame)
login_password_entry = ttk.Entry(login_frame)


signup_name1_entry.grid(row=1 ,column=0 )
signup_name2_entry.grid(row=3 , column=0 )
address_entry.grid(row=5,column=0)
Postcode_entry.grid(row=7,column=0)
login_password_entry.grid(row=11,column=0)
login_email_entry.grid(row=9,column=0)

signup1_button = ttk.Button(login_frame, text="Sign up!",
                command = validateentry)
signup1_button.grid()

#home page

Home_button1 = ttk.Button(home_frame,text="About",
command = showabout_frame)
Home_button2 = ttk.Button(home_frame,text="FAQ", command = showfaq_frame)
Home_button3 = ttk.Button(home_frame,text="Welcome back!")
Home_button4 = ttk.Button(home_frame,text="Welcome back!")
Home_button5 = ttk.Button(home_frame,text="Welcome back!")

Home_button1.grid(row=0,column=0, ipadx=10, ipady=10)
Home_button2.grid(row=0,column=1, ipadx=10, ipady=10)
Home_button3.grid(row=0,column=2, ipadx=10, ipady=10)
Home_button4.grid(row=0,column=3, ipadx=10, ipady=10)
Home_button5.grid(row=0,column=4, ipadx=10, ipady=10)

home_label = ttk.Label(home_frame, text="BUSINESS NAME")
descrip_label = ttk.Label(home_frame, text="SAMPLE TEXT")


descrip_label.grid()
home_label.grid()

order_button = tk.Button(home_frame, text="ORDER", command = showorder_frame)

order_button.grid()


#order frame

delivery_button = tk.Button(order_frame, text='delivery',
                            command = showorder_frame,
                            relief=tk.SUNKEN, borderwidth=3,
                            height=5,width=30


)
collection_button = tk.Button(order_frame, text='collection',
                                command= showcollection_frame,
                                height=5,width=30)

hotdrinks_label = ttk.Label(order_frame, text='HOT DRINKS!!!!')

latte_button = ttk.Button(order_frame, text='latte', command=showcheckoutframe)
cappuccino_button= ttk.Button(order_frame, text='cappuccino', command=showcheckoutframe)
americano_button = ttk.Button(order_frame, text='americano', command=showcheckoutframe)
flatwhite_button = ttk.Button(order_frame, text='flat white', command=showcheckoutframe)


delivery_button.grid()
collection_button.grid()
hotdrinks_label.grid(ipadx=100, ipady=30)
latte_button.grid(ipadx=100, ipady=30)
cappuccino_button.grid(ipadx=100, ipady=30)
americano_button.grid(ipadx=100, ipady=30)
flatwhite_button.grid(ipadx=100, ipady=30)

#duplicating delivery frame for collection


delivery_button = tk.Button(collection_frame, text='delivery',
                            command = showorder_frame,
                            height=5,width=30)
collection_button = tk.Button(collection_frame, text='collection',
                                command= showcollection_frame,
                                relief=tk.SUNKEN, borderwidth=3,
                                height=5,width=30)

delivery_button.pack()
collection_button.pack()





#about us frame
back_button1 = ttk.Button (about_frame, text = "< back", command = showhome_frame)
back_button1.pack(side=LEFT)
about_label1 = ttk.Label (about_frame,text = "[business name] was founded in [...] by the [...] brothers...")
about_label1.pack(side=LEFT)



#FAQ



back_button2 = ttk.Button (faq_frame, text = "< back", command = showhome_frame)
back_button2.grid(column=0,pady=0,padx=0)
FAQ_label1 = ttk.Label (faq_frame, text ='Q: how do I spend my points? ')
FAQ_label1.grid()
FAQ_label2 = ttk.Label (faq_frame, text ='Q: how do I spend my points? ')
FAQ_label2.grid()
FAQ_label3 = ttk.Label (faq_frame, text ='Q: how do I spend my points? ')
FAQ_label3.grid()
FAQ_label4 = ttk.Label (faq_frame, text ='Q: how do I spend my points? ')
FAQ_label4.grid()



checkoutlabel.Label(checkoutframe, text='Check Out')
checkoutbutton.Button(checkoutframe, text='Confirm payment')









admin_database()
stock_database()
stockdb()
signup_database()
showsignupframe()
root.mainloop()