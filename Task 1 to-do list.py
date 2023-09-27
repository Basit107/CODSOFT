import pickle
from tkinter import *
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-do List")


def add_task():
    todo = entry_task.get()
    if todo != "":
        app_box.insert(tkinter.END, todo)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="NOTE !!", message="Please write something first.")

def delete_task():
    try:
        index_todo = app_box.curselection()[0]
        app_box.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Warning !!", message="Please choose a task to delete.")

def load_task():
    try:
        todo_list = pickle.load(open("tasks.dat", "rb"))
        app_box.delete(0, tkinter.END)
        for todo in todo_list:
            app_box.insert(tkinter.END, todo)
    except:
        tkinter.messagebox.showwarning(title="Warning !!", message="Task not Found.")

def save_tasks():
    todo_list = app_box.get(0, app_box.size())
    pickle.dump(todo_list, open("tasks.dat", "wb"))


list_frame = tkinter.Frame(root)
list_frame.pack()

app_box = tkinter.Listbox(list_frame, font=("Arial",14), height=10, width=43)
app_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

app_box.config(yscrollcommand=scroller.set)
scroller.config(command=app_box.yview)

entry_task = tkinter.Entry(root, font=("arial",12), width=40)
entry_task.pack(padx=0, pady=9)

add_task_button = tkinter.Button(root, text="Add Task", font=("arial", 13, "bold"), fg='white', background="#36F51C", width=48, command=add_task)
add_task_button.pack()


delete_task_button = tkinter.Button(root, text="Delete Task", font=("arial", 13, "bold"), fg='white', background="#F14020", width=48, command=delete_task)
delete_task_button.pack()

load_task_button = tkinter.Button(root, text="Load Tasks", font=("arial", 13, "bold"), fg='white', background="#7A7E79", width=48, command=load_task)
load_task_button.pack()

save_task_button = tkinter.Button(root, text="Save Tasks", font=("arial", 13, "bold"), fg='white', background="#E4F516", width=48, command=save_tasks)
save_task_button.pack()

root.mainloop()


