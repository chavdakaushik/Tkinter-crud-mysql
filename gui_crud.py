from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="demo"
)
mycursor = mydb.cursor()

root = Tk()
var = IntVar()
root.title("Registration")
root.geometry("900x700")

label1 = Label(root, text="First_Name", width=20,
               height=2, bg="cyan").grid(row=0, column=0)
label2 = Label(root, text="Last_Name", width=20,
               height=2, bg="cyan").grid(row=1, column=0)
label3 = Label(root, text="Phone_Number", width=20,
               height=2, bg="cyan").grid(row=2, column=0)
label4 = Label(root, text="Email_id", width=20,
               height=2, bg="cyan").grid(row=3, column=0)
label5 = Label(root, text="Gender", width=20, height=2,
               bg="cyan").grid(row=4, column=0)
label6 = Label(root, text="Address", width=20, height=2,
               bg="cyan").grid(row=5, column=0)

e1 = Entry(root, width=30, borderwidth=3)
e1.grid(row=0, column=1)
e2 = Entry(root, width=30, borderwidth=3)
e2.grid(row=1, column=1)
e3 = Entry(root, width=30, borderwidth=3)
e3.grid(row=2, column=1)
e4 = Entry(root, width=30, borderwidth=3)
e4.grid(row=3, column=1)
e5 = Radiobutton(root, text="Male", variable=var, value=1)
e5.grid(row=4, column=1)
e6 = Radiobutton(root, text="Female", variable=var, value=0)
e6.grid(row=4, column=2)
e7 = Entry(root, width=30, borderwidth=3)
e7.grid(row=5, column=1)


def check(email):
    if(re.search(regex, email)):
        return True
    else:
        return False


def add_data():
    First_Name = e1.get()
    Last_Name = e2.get()
    Phone_Number = e3.get()
    Email_id = e4.get()
    Gender = str(var.get())
    Address = e7.get()

    if(First_Name != "" and Last_Name != "" and Phone_Number != "" and Email_id != "" and Gender != "" and Address != ""):
        if(check(Email_id) and len(Phone_Number) != 10):
            sql_query = "insert into registration (first_name, last_name, phone_number, email_id, gender, address) values (%s, %s, %s, %s, %s, %s)"
            values = (First_Name, Last_Name, Phone_Number,
                      Email_id, Gender, Address)
            mycursor.execute(sql_query, values)
            mydb.commit()
            messagebox.askokcancel("Information", "Data Added")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e7.delete(0, END)
        else:
            messagebox.askokcancel(
                "Information", "Enter Valid Email or Mobile")
    else:
        messagebox.askokcancel("Information", "Some fields left blank")


def show_data():
    class Data(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.create_ui()
            self.load_table()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)

        def create_ui(self):
            tv = Treeview(self)
            tv['columns'] = ['First_Name', 'Last_Name',
                             'Phone_Number', 'Email_id', 'Gender', 'Address']
            tv.heading('#0', text='Action', anchor='center')
            tv.column('#0', anchor='center')
            tv.heading('#1', text='First_Name', anchor='center')
            tv.column('#1', anchor='center')
            tv.heading('#2', text='Last_Name', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='Phone_Number', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='Email_id', anchor='center')
            tv.column('#4', anchor='center')
            tv.heading('#5', text='Gender', anchor='center')
            tv.column('#5', anchor='center')
            tv.heading('#6', text='Address', anchor='center')
            tv.column('#6', anchor='center')
            tv.grid(sticky=(N, S, W, E))
            self.treeview = tv
            tv.bind("<Button-1>", self.on_tree_select)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

        def on_tree_select(self, event):
            curItem = self.treeview.item(self.treeview.focus())

            def update_data(id):
                First_Name = e1.get()
                Last_Name = e2.get()
                Phone_Number = e3.get()
                Email_id = e4.get()
                Gender = str(var.get())
                Address = e7.get()

                sql_query_update = "update registration set first_name='%s', last_name='%s', phone_number='%s',email_id='%s', gender='%s',address='%s' where id='%s'" % (
                    First_Name, Last_Name, Phone_Number, Email_id, Gender, Address, id)
                mycursor.execute(sql_query_update)
                mydb.commit()
                messagebox.askokcancel("Information", "Data Updated")

            def delete_data(id):
                sql_query_delete = "delete from registration where id = '%s'" % (
                    id)
                mycursor.execute(sql_query_delete)
                mydb.commit()
                messagebox.askokcancel("Information", "Data Deleted")

            if curItem['values'] != "":
                root1 = Tk()
                root1.geometry('700x700')

                label1 = Label(root1, text="First_Name", width=20,
                               height=2, bg="cyan").grid(row=0, column=0)
                label2 = Label(root1, text="Last_Name", width=20,
                               height=2, bg="cyan").grid(row=1, column=0)
                label3 = Label(root1, text="Phone_Number", width=20,
                               height=2, bg="cyan").grid(row=2, column=0)
                label4 = Label(root1, text="Email_id", width=20,
                               height=2, bg="cyan").grid(row=3, column=0)
                label5 = Label(root1, text="Gender", width=20,
                               height=2, bg="cyan").grid(row=4, column=0)
                label6 = Label(root1, text="Address", width=20,
                               height=2, bg="cyan").grid(row=5, column=0)

                e1 = Entry(root1, width=30, borderwidth=3)
                e1.grid(row=0, column=1)
                e2 = Entry(root1, width=30, borderwidth=3)
                e2.grid(row=1, column=1)
                e3 = Entry(root1, width=30, borderwidth=3)
                e3.grid(row=2, column=1)
                e4 = Entry(root1, width=30, borderwidth=3)
                e4.grid(row=3, column=1)
                e5 = Radiobutton(root1, text="Male",
                                 variable=var, value="Male")
                e5.grid(row=4, column=1)
                e6 = Radiobutton(root1, text="Female",
                                 variable=var, value="Female")
                e6.grid(row=4, column=2)
                e7 = Entry(root1, width=30, borderwidth=3)
                e7.grid(row=5, column=1)

                lst = curItem['values']
                e1.insert(0, lst[0])
                e2.insert(0, lst[1])
                e3.insert(0, lst[2])
                e4.insert(0, lst[3])
                e7.insert(0, lst[5])

                update_button = Button(root1, text="Update", width=10, height=2, command=lambda: update_data(
                    curItem['text'])).grid(row=7, column=0)
                delete_button = Button(root1, text="Delete", width=10, height=2, command=lambda: delete_data(
                    curItem['text'])).grid(row=7, column=1)

                root1.mainloop()
                # messagebox.askokcancel("Information", curItem['values'])

        def load_table(self):
            sql_query_select = "select * from registration"
            mycursor.execute(sql_query_select)
            result = mycursor.fetchall()
            Id = ""
            First_Name = ""
            Last_Name = ""
            Phone_Number = ""
            Email_id = ""
            Gender = ""
            Address = ""
            for i in result:
                Id = i[0]
                First_Name = i[1]
                Last_Name = i[2]
                Phone_Number = i[3]
                Email_id = i[4]
                Gender = i[5]
                Address = i[6]
                self.treeview.insert("", 'end', text=Id, values=(
                    First_Name, Last_Name, Phone_Number, Email_id, Gender, Address))

    root = Tk()
    root.title("List of records")
    Data(root)


add_button = Button(root, text="Add", width=10, height=2,
                    command=add_data).grid(row=7, column=0)
show_button = Button(root, text="Show record", width=10,
                     height=2, command=show_data).grid(row=7, column=1)

root.mainloop()
