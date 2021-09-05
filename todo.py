import tkinter as tk
from tkinter import *
from tkinter import font


class TodoItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TodoList:

    def __init__(self, root):
        
        root.title("To Do List App")

        #frame of the todo list app
        frame = Frame(root, borderwidth=2, relief="groove")
        frame.grid(row=1, column=1, sticky=(NS, EW))
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        #label of the todo list created
        list_label = Label(frame, text="Todo List",font=(26) )
        list_label.grid(row=1, column=1, sticky=(S,))
        #list of todo item (name, description)
        self.todo_items = [
            TodoItem("Read", "read a book!"),
            TodoItem("Watch a Movie", "Pick out and watch a movie")
        ]
        self.todo_names = StringVar(value=list(map(lambda x: x.name, self.todo_items)))
        
        #list of created todo items by name
        item_list = Listbox(frame, listvariable=self.todo_names, height=5,width=25, font=(28), exportselection=False)
        item_list.grid(row=2, rowspan=4, column=1, sticky=(EW, NS))
        item_list.bind("<<ListboxSelect>>", lambda s: self.select_item(item_list.curselection()))

        #task label
        task_label = Label(frame, text="Task name:", font=(18), padx=4)
        task_label.grid(row=1, column=3, sticky=(S,))
       
        #Task name entry box
        self.name_text = StringVar()
        entry = Entry(frame, textvariable=self.name_text, font=(28))
        entry.grid(row=2, column=3, sticky=(S, EW))
        
        #textbox for editing description
        description_label = Label(frame, text="description", font=(18))
        description_label.grid(row=3, column=3, sticky=(S,))
        
        self.description = Text(frame, width=18, height=5, font=(28), wrap="word")
        self.description.grid(column=3, row=4, sticky=(EW,))

        #button
        button = Button(frame, text="Add Item", command=self.add_item_button)
        button.grid(row=6, column=3, sticky=(S, EW))

        button = Button(frame, text="Save List", command=self.save_button)
        button.grid(row=6, column=1, sticky=(S, EW))

        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=5)
        

    def add_item_button(self):
        if self.name_text.get() != "":
            if self.index != None:
                if self.name_text.get() == self.todo_items[self.index[0]].name:
                    self.todo_items[self.index[0]].description = self.description.get(1.0, END)
            else:
                self.todo_items.append(TodoItem(self.name_text.get(), self.description.get(1.0, END)))
                self.todo_names.set(value=list(map(lambda x: x.name, self.todo_items)))

    def select_item(self, index):
        self.description.delete(1.0, END)
        self.description.insert(1.0,self.todo_items[index[0]].description)
        self.name_text.set(self.todo_items[index[0]].name)
        self.index = index

    def save_button(self):
        pass

        





root = Tk()
TodoList(root)

root.mainloop()