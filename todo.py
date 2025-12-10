import tkinter as tk
from tkinter import messagebox

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                listbox.insert(tk.END, task.strip())
    except:
        pass

# Add task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task")

# Delete task
def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

# Save tasks to file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# GUI Setup 
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=28, height=15)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=26)
entry.pack(pady=5)

add_btn = tk.Button(root, text="Add Task", width=10, command=add_task)
add_btn.pack(pady=2)

del_btn = tk.Button(root, text="Delete Task", width=10, command=delete_task)
del_btn.pack(pady=2)

# Load tasks on start
load_tasks()

root.mainloop()