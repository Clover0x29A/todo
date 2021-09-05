from tkinter import *



class TodoItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TodoList:

    def __init__(self, root):
        
        self.todo_file = 'todo_list.txt'

        self.index = (-1,)
        self.todo_items =  []
        self.read_todo_list()

        root.title("To Do List App")

        # frame of the todo list app
        frame = Frame(root, borderwidth=2, relief="groove")
        frame.grid(row=1, column=1, sticky=(NS, EW))
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        # label of the todo list created
        list_label = Label(frame, text="Todo List",font=(26) )
        list_label.grid(row=1, column=1, sticky=(S,))
        
        
 
        self.todo_names = StringVar(value=list(map(lambda x: x.name, self.todo_items)))
        
        # list of created todo items by name
        # because I used a text widget, if I selected text in it that would throw an error
        # based off of how curselection works so I added exportselection=False to stop the
        # error
        item_list = Listbox(frame, listvariable=self.todo_names, height=5,width=25, font=(28), exportselection=False)
        item_list.grid(row=2, rowspan=4, column=1, sticky=(EW, NS))
        item_list.bind("<<ListboxSelect>>", lambda s: self.select_item(item_list.curselection()))

        # task label
        task_label = Label(frame, text="Task name:", font=(18), padx=4)
        task_label.grid(row=1, column=3, sticky=(S,))
       
        # Task name entry box
        self.name_text = StringVar()
        entry = Entry(frame, textvariable=self.name_text, font=(28))
        entry.grid(row=2, column=3, sticky=(S, EW))
        
        # textbox for editing description
        description_label = Label(frame, text="description", font=(18))
        description_label.grid(row=3, column=3, sticky=(S,))
        
        self.description = Text(frame, width=18, height=5, font=(28), wrap="word")
        self.description.grid(column=3, row=4, sticky=(EW,))

        # buttons
        # add item
        # delete item
        # save list
        button = Button(frame, text="Add Item", command=self.add_item_button)
        button.grid(row=6, column=3, sticky=(S, EW))

        button = Button(frame, text="Delete Item", command=self.del_item_button)
        button.grid(row=7, column=3, sticky=(S, EW))

        button = Button(frame, text="Save List", command=self.save_button)
        button.grid(row=6, column=1, sticky=(S, EW))

        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=5)
        
    # button actions when clicked
    def add_item_button(self):
        if self.name_text.get() != "":
            if self.index[0]>= 0 and self.index[0] < len(self.todo_items):
                if self.todo_items[self.index[0]].name == self.name_text.get():
                    self.todo_items[self.index[0]].description = self.description.get(1.0, END)
                else:
                    self.update_todo_list()
            else:
                self.update_todo_list()
    # this function goes with add_item_button    
    def update_todo_list(self):
        self.todo_items.append(TodoItem(self.name_text.get(), self.description.get(1.0, END)))
        self.todo_names.set(value=list(map(lambda x: x.name, self.todo_items)))

    def select_item(self, index):
        self.description.delete(1.0, END)
        self.description.insert(1.0,self.todo_items[index[0]].description)
        self.name_text.set(self.todo_items[index[0]].name)
        self.index = index

    def save_button(self):
        self.write_in_todo()

    def del_item_button(self):
        if self.index != None:
            if self.index[0] >= 0 and self.index[0] < len(self.todo_items):
                self.todo_items.pop(self.index[0])
                self.todo_names.set(value=list(map(lambda x: x.name, self.todo_items)))
    
    # this overwrites todo_list.txt
    # with the current list in program
    # file is made as "name","description"
    def write_in_todo(self):
        file = open(self.todo_file, "w")
        for x in self.todo_items:
            # x.description[:-1] removes hidden char
            full_line = '"' + x.name + '","' + x.description[:-1] + '"'
            print(full_line)
            print(len(full_line))
            file.writelines(full_line)
            file.writelines('\n')
        file.close()
    
    # open text file on start and create list from it
    # reads in a line at a time and creates name and
    # description from them
    def read_todo_list(self):
        file = open(self.todo_file, "r")
        for x in file:
            index_comma = x.index('","', 0, len(x))
            if index_comma != -1:
                name = x[1:index_comma]
                index_comma += 3
                description = x[index_comma:-2]
                self.todo_items.append(TodoItem(name, description))        
        file.close()
        

# Start of Program
root = Tk()
TodoList(root)

root.mainloop()