import tkinter as tk
from tkinter import ttk, Menu, SUNKEN , LEFT , RIGHT , TOP, BOTTOM

root = tk.Tk()
root.geometry("1000x700")
def showorder_frame():
    order_frame.tkraise()
def showsignupframe():
    signup_frame.tkraise()
def showlogin_frame():
    login_frame.tkraise()
def showhome_frame():
    validation = email_entry.get()
    if len(validation) >5:
        print("yipee")
        home_frame.tkraise()
    else:
        print("invalid")
        showsignupframe()
        error_login.grid()
def showcollection_frame():
    collection_frame.tkraise()







signup_frame = ttk.Frame(root, padding=10)
login_frame = ttk.Frame(root, padding=10)
home_frame = ttk.Frame(root, padding=10)
order_frame = ttk.Frame(root, padding=10)
collection_frame = ttk.Frame(root, padding=10)


signup_frame.grid(row=0,column=0,sticky="nsew")
login_frame.grid(row=0,column=0, sticky="nsew")
home_frame.grid(row=0,column=0, sticky="nsew")
order_frame.grid(row=0,column=0, sticky="nsew")
collection_frame.grid(row=0,column=0,sticky="nsew")


#placing it on the order frame
hotdrinks_var = tk.StringVar()
colddrinks_var = tk.StringVar()

signup_label = ttk.Label(signup_frame, text="Sign up!")
email_label = ttk.Label(signup_frame,text="email:")
password_label = ttk.Label(signup_frame,text="Password:")

signup_label.grid(row=0,column=0)
email_label.grid(row=1,column=0)
password_label.grid(row=3,column=0)
test = ttk.Button(signup_frame)
test.grid()
email_entry = ttk.Entry(signup_frame)
password_entry = ttk.Entry(signup_frame)

password_entry.grid(row=4,column=0)
email_entry.grid(row=2,column=0)

signup_button = ttk.Button(signup_frame, text="Sign up!", command = showhome_frame)
login_button = ttk.Button(signup_frame, text="or Log in", command = showlogin_frame)

signup_button.grid(row=5,column=0)
login_button.grid(row=6,column=0, pady=20)

#Login page,
login_email_label = ttk.Label(login_frame, text="Email:")
login_password_label = ttk.Label(login_frame,text="Password:")
login_email_label.grid(row=0,column=0)
login_password_label.grid(row=3,column=0)

login_email_entry = ttk.Entry(login_frame)
login_password_entry = ttk.Entry(login_frame)

login_password_entry.grid(row=4,column=0)
login_email_entry.grid(row=1,column=0)
error_login = ttk.Label(text="error: please enter a valid email " )
error_login.grid_forget()

Log_button = ttk.Button(login_frame, text="Welcome back!",
                command = showhome_frame)
Log_button.grid()


#home page

Home_button1 = ttk.Button(home_frame,text="Welcome back!")
Home_button2 = ttk.Button(home_frame,text="Welcome back!")
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

delivery_button.pack(padx=100,side=RIGHT)
collection_button.pack(side=RIGHT)

combo_order = ttk.Combobox(order_frame, text="Hot drinks",
                            state="readonly",
                            textvariable=hotdrinks_var,

)
combo_order["values"] = ("Hot Drinks!",
"coffee                                      £3.50",
"hot chocolate                         £3.50",
"americano                              £3.50",
"latte                                         £3.50",
"capuchino                              £3.50",
"pumpkin spice latte              £3.50")

combo_order.pack(side=BOTTOM, padx=200)
combo_order.current(0)




combo_order = ttk.Combobox(order_frame, text="Hot drinks",
                            state="readonly",
                            textvariable=colddrinks_var,

)

#adding the values
combo_order["values"] = ("Hot Drinks!",
"coffee                                      £3.50",
"hot chocolate                         £3.50",
"americano                              £3.50",
"latte                                         £3.50",
"capuchino                              £3.50",
"pumpkin spice latte              £3.50")

combo_order.pack(side=BOTTOM)
combo_order.current(0)


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




combo_order = ttk.Combobox(collection_frame, text="Hot drinks",
                            state="readonly",
                            textvariable=hotdrinks_var,

)
combo_order["values"] = ("Hot Drinks!",
"coffee                                      £3.50",
"hot chocolate                         £3.50",
"americano                              £3.50",
"latte                                         £3.50",
"capuchino                              £3.50",
"pumpkin spice latte              £3.50")

combo_order.pack()
combo_order.current(0)




combo_order = ttk.Combobox(collection_frame, text="Hot drinks",
                            state="readonly",
                            textvariable=colddrinks_var,

)

#adding the values
combo_order["values"] = ("cold Drinks!",
"coffee                                      £3.50",
"hot chocolate                         £3.50",
"americano                              £3.50",
"latte                                         £3.50",
"capuchino                              £3.50",
"pumpkin spice latte              £3.50")

combo_order.pack()
combo_order.current(0)










showsignupframe()
root.mainloop()



showsignupframe()
root.mainloop()
