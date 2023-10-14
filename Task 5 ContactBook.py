import csv, tkinter
from tkinter import *
from tkinter import messagebox


# Create a main Window
root = tkinter.Tk()
root.title("Contact Book")
theme = "#F9FBFF"
font_name = "Candara"
button_color = "#2C89D6"
entry_widget_colr = "#F0F0F0" 
entry_fg = "#000000"

root.config(bg=theme)

app_width = 500
app_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (app_width/2))
y = int((screen_height/2) - (app_height/2))

root.geometry(f"{app_width}x{app_height}+{x-34}+{y-15}")



header = [""]
search_term = ""
contact_list = []
results = []


def add_to_listbox(): # All Contacts are inserted inside the Contact List_box through this function
    global contact_list

    contact_listbox.delete(0, END)
    contact_list.sort(key=lambda name: name[0])
    for i, (name, contact_num, e_mail, address) in enumerate(contact_list, start=1):
        contact_listbox.insert(END, f"  {i}      |         {name}         |           {contact_num}")


def search_listbox(event):
    global results, search_term

    search_term = search_entry.get()
    results = []
    contact_listbox.delete(0, tkinter.END)  # Clear the Listbox
    for index, (name, contact_num, e_mail, address) in enumerate(contact_list):
        if search_term.lower() in name.lower():
            contact_listbox.select_clear(0, tkinter.END)  # Clear previous selections
            results.append(index)

        elif search_term in contact_num:
            results.append(index)
    
    for c, (name, contact_num, e_mail, address) in enumerate(contact_list):
        if c in results:
            contact_listbox.insert(tkinter.END, f"  {c+1}         |         {name}              |          {contact_num}")


def ReadCSVFile():
    global header, contact_list

    with open("ContactDetails.csv", "r") as csvfile:
        global header
        csv_reader = csv.reader(csvfile,delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            contact_list.append(row)
    add_to_listbox()		


def WriteInCSVFile(phonelist):
    with open('ContactDetails.csv','w',newline='') as csv_file:
        writeobj = csv.writer(csv_file,delimiter=',')
        writeobj.writerow(header)
        for row in phonelist:
            writeobj.writerow(row)


def edit_contact(): # Saves the Changes done in the selected contact Information
    global contact_list

    if window3_name_ent.get() and window3_num_ent.get() and window3_email_ent.get() and window3_address_ent.get():
        if results:
            index_to_view = int(ind[0])
            original_index = results[index_to_view]
            contact_list[original_index] = [window3_name_ent.get(), window3_num_ent.get(),
                                    window3_email_ent.get(), window3_address_ent.get()]

        else:
            contact_list[ind[0]] = [window3_name_ent.get(), window3_num_ent.get(),
                                window3_email_ent.get(), window3_address_ent.get()]
        
        add_to_listbox()
        WriteInCSVFile(contact_list)
        messagebox.showinfo("Confirmation", "Succesfully Update Contact")
        window3.destroy()


def save_contact(): #Saves the contact information that the user has added
    global contact_list

    name = name_entry.get()
    contact_num = number_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    try:
        int(contact_num)
        if name != "" and contact_num != "" and email != "" and address != "":
            contact_list.append([name, contact_num, email, address])
            WriteInCSVFile(contact_list)
            add_to_listbox()

            add_contact_button.config(state=NORMAL)
            window2.destroy()
        
        else:
            tkinter.messagebox.showwarning(title="NOTE !!", message="Please Enter The required Fields.")

    except ValueError:
        tkinter.messagebox.showwarning(title="ATTENTION!!", message="Please Enter contact number.")


def add_contact_window():# creates a new window for user to add contact Information
    global window2, name_entry, number_entry, email_entry, address_entry

    window2 = tkinter.Tk()
    window2.title("Add Contact")
    window2.config(bg=theme)

    app_width = 400
    app_height = 450

    x = int((screen_width/2) - (app_width/2))
    y = int((screen_height/2) - (app_height/2))

    window2.geometry(f"{app_width}x{app_height}+{x+6}+{y-23}")

    name_label = tkinter.Label(window2, text="Enter Name: ", font=(font_name, 14), bg=theme)
    name_label.pack(pady=16)
    name_entry = tkinter.Entry(window2, font=(font_name, 13), width=34, fg=entry_fg, bg=entry_widget_colr)
    name_entry.pack()

    number_label = tkinter.Label(window2, text="Enter Phone Number: ", font=(font_name, 14), bg=theme)
    number_label.pack(pady=16)
    number_entry = tkinter.Entry(window2, font=(font_name, 13), width=34, fg=entry_fg, bg=entry_widget_colr)
    number_entry.pack()

    email_label = tkinter.Label(window2, text="Enter Email: ", font=(font_name, 14), bg=theme)
    email_label.pack(pady=16)
    email_entry = tkinter.Entry(window2, font=(font_name, 13), width=34, fg=entry_fg, bg=entry_widget_colr)
    email_entry.pack()

    address_label = tkinter.Label(window2, text="Enter Address: ", font=(font_name, 14), bg=theme)
    address_label.pack(pady=16)
    address_entry = tkinter.Entry(window2, font=(font_name, 13), width=34, fg=entry_fg, bg=entry_widget_colr)
    address_entry.pack()
    
    save_contact_button = tkinter.Button(window2, text="Save Contact", font=(font_name, 13, "bold"), 
                                         fg='white', background=button_color, justify=LEFT, command=save_contact)
    save_contact_button.pack(side=BOTTOM, padx=15, pady=26)
    
    window2.mainloop()


def view_contact(): # Creates a window to view Full details of selected contact
    global window3, window3_name_ent, window3_num_ent, window3_email_ent, window3_address_ent, contact_list, ind
    
    try:
        ind = contact_listbox.curselection()
        if results != []:
            index_to_view = int(ind[0])
            original_index = results[index_to_view]
            name, num, email, address = contact_list[original_index]
        else:
            index_to_view = int(ind[0])
            name, num, email, address = contact_list[index_to_view]

        window3 = tkinter.Tk()
        window3.title(name)
        window3.config(bg=theme)

        app_width = 400
        app_height = 450

        x = int((screen_width/2) - (app_width/2))
        y = int((screen_height/2) - (app_height/2))

        window3.geometry(f"{app_width}x{app_height}+{x+6}+{y-23}")

        name_label = tkinter.Label(window3, text="Name: ", font=(font_name, 14), bg=theme)
        name_label.pack(pady=16)
        window3_name_ent = tkinter.Entry(window3, font=(font_name, 13), width=34, fg=entry_fg, bg=entry_widget_colr)
        window3_name_ent.pack()

        number_label = tkinter.Label(window3, text="Contact Number: ", font=(font_name, 14), bg=theme)
        number_label.pack(pady=16)
        window3_num_ent = tkinter.Entry(window3, font=(font_name, 13), width=34, fg=entry_fg, bg=entry_widget_colr)
        window3_num_ent.pack()

        email_label = tkinter.Label(window3, text="Email: ", font=(font_name, 14), bg=theme)
        email_label.pack(pady=16)
        window3_email_ent = tkinter.Entry(window3, font=(font_name, 13), width=34, fg=entry_fg, bg=entry_widget_colr)
        window3_email_ent.pack()

        address_label = tkinter.Label(window3, text="Address: ", font=(font_name, 14), bg=theme)
        address_label.pack(pady=16)
        window3_address_ent = tkinter.Entry(window3, font=(font_name, 13), width=34, fg=entry_fg, bg=entry_widget_colr)
        window3_address_ent.pack()

        edit_contact_button = tkinter.Button(window3, text="Edit Contact", font=(font_name, 13, "bold"), 
                                            fg='white', background=button_color, justify=LEFT, command=edit_contact)
        edit_contact_button.pack(side=BOTTOM, padx=15, pady=26)

        window3_name_ent.insert(0, name)
        window3_num_ent.insert(0, num)
        window3_email_ent.insert(0, email)
        window3_address_ent.insert(0, address)

        window3.mainloop()
    except:
        messagebox.showerror("Error", "Please Select a Contact to view.")


def delete_contact(): # Deletes the selected contact information from the file
    filtered_indices = [index for index, (name, email, num, address) in enumerate(contact_list) 
                        if search_term in name.lower() or search_term in num]
    selected_index = contact_listbox.curselection()
    if filtered_indices:
        if len(selected_index)!=0:
            result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
            if result==True:
                index_to_delete = int(selected_index[0])  # Convert the selected index to an integer
                original_index = filtered_indices[index_to_delete]
                deleted_item = contact_list[original_index]
                contact_listbox.delete(selected_index) 
                del contact_list[original_index]
                filtered_indices.pop(index_to_delete)
                WriteInCSVFile(contact_list)
                add_to_listbox()
        else:
            messagebox.showerror("Error", 'Please select the Contact')
    else:
        if len(selected_index)!=0:
            result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
            if result==True:
                index_to_delete = int(selected_index[0])
                contact_listbox.delete(selected_index)
                del contact_list[selected_index[0]]
                WriteInCSVFile(contact_list)
                add_to_listbox()



# The Code for the main window that displays all the contacts
search_label = tkinter.Label(root, text="Search:", font=("Arial", 13, "bold"), bg=theme)
search_label.pack(pady=4)

search_entry = tkinter.Entry(root, font=("Arial", 13), fg=entry_fg, bg=entry_widget_colr)
search_entry.pack(side=tkinter.TOP, padx=5, pady=9)
search_entry.bind('<KeyRelease>', search_listbox)


list_frame = tkinter.Frame(root)
scroller = tkinter.Scrollbar(list_frame, orient=VERTICAL)
contact_listbox = tkinter.Listbox(list_frame, yscrollcommand=scroller.set, font=("Arial Bold",14), 
                                  height=13, width=55, justify=LEFT, fg="#2C89D6", bg="black", borderwidth=1, relief=GROOVE)

scroller.config(command=contact_listbox.yview)

scroller.pack(side=tkinter.RIGHT, fill=Y)
contact_listbox.pack()
list_frame.pack(side=tkinter.TOP, padx=15, pady=16)

add_contact_button = tkinter.Button(root, text="Add Contact", font=(font_name, 13, "bold"), fg='white', 
                                    background=button_color, command=add_contact_window)
add_contact_button.pack(side=LEFT, padx=15)

delete_contact_button = tkinter.Button(root, text="Delete Contact", font=(font_name, 13, "bold"), fg='white', 
                                       background="#F5311E", command=delete_contact)
delete_contact_button.pack(side=LEFT, padx=40)

view_contact_button = tkinter.Button(root, text="View Contact", font=(font_name, 13, "bold"), fg='white', 
                                     background=button_color, command=view_contact)
view_contact_button.pack(side=RIGHT, padx=15)



ReadCSVFile()

root.mainloop()