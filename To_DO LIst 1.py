import tkinter as tk
import tkinter.messagebox
import json
import os

# create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x350")
root.configure(bg="lightgreen")

# create a list to store tasks
tasks = []


#create functions
def update_listbox():
     clear_listbox()
     for task in tasks:
        btn_listbox.insert(tk.END, task)
   
def clear_listbox():
    btn_listbox.delete(0, tk.END)

def add_task(event):
    task = txt_input.get() 
    #check if the task is not empty
    if task:
        #add the task to the list
        tasks.append(task)
        #save the tasks to a file
        save_tasks()
        #update the listbox
        update_listbox()
        #clear the input field
        txt_input.delete(0, tk.END)
    else:
        tk.messagebox.showwarning("Input Error", "Please enter a task.")


def delete_one():
    # get the selected task index
    task = btn_listbox.get("active")
    #comfirm it is in the list
    if task in tasks:
        # remove the task from the list
        tasks.remove(task)
        #save the tasks to a file
        save_tasks()
        # update the listbox
        update_listbox()
    else:
        tk.messagebox.showinfo("No Selection", "Please select a task to delete.")


def mark_done(event):
    selected_index = btn_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = btn_listbox.get(index)
        if not task.startswith("✔ "):
            # Update the task in the tasks list
            tasks[index] = f"✔ {task}"
            save_tasks()
            update_listbox()
            # Optionally, set color after updating listbox
            btn_listbox.itemconfig(index, fg="blue")

    
def delete_all():
    #since we are changing the list ,we need to be global
    global tasks
    #clear the list 
    tasks = []
    save_tasks()
    #update the listbox
    update_listbox()

def save_tasks():
    #save the tasks to a file
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        
def load_tasks():
    #check if the file exists
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            global tasks
            tasks = json.load(file)
            update_listbox()


# create the widgets
lbl_title = tk.Label(root, text="MY LIST", bg="lightgreen")
lbl_title.pack(pady=10)

txt_input = tk.Entry(root, width=40)
txt_input.pack(side=tk.TOP, padx=10, pady=10)

#add task on pressing enter
txt_input.bind("<Return>", add_task)

btn_listbox = tk.Listbox(root, width=40, height=10)
btn_listbox.pack()

#bind double-click to mark task as done
btn_listbox.bind('<Double-1>', mark_done)

btn_delete_all= tk.Button(root, text="Delete all", bg="lightgreen", command=delete_all)
btn_delete_all.pack(pady=2)

btn_delete_one = tk.Button(root, text="Delete", bg="lightgreen", command=delete_one)
btn_delete_one.pack(pady=2)

# load tasks from file when the program starts
load_tasks()

# start the main loop
root.mainloop()