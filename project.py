import customtkinter 
import re
import json
class MyStylebox(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)
        # Tilte for style mode in top
        self.title = customtkinter.CTkLabel(self, text="Style Mode", fg_color="gray30",font=("Verdana",14), corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
        
        # First button
        self.button = customtkinter.CTkButton(self, corner_radius=5, text="Light Mode", font=("Tahoma" , 14) ,command=light_button)
        self.button.grid(row=1, column=0, padx=20, pady=(35, 0), sticky="e")
        
        # Second button
        self.button_2 = customtkinter.CTkButton(self, corner_radius=5, text="Dark Mode", font=("Tahoma" , 14) ,command=dark_button)
        self.button_2.grid(row=2, column=0, padx=20, pady=(20, 5), sticky="e")



class History_list(customtkinter.CTkScrollableFrame):
    def __init__(self, master = None):
        super().__init__(master)
        self.history_lists = []
        self.empty_title = None
        self.rows = 3   # rows start at 3 cuz the 2 before is titles
        # title for HistoryList
        self.title = customtkinter.CTkLabel(self, text="History list", fg_color="gray30",font=("Verdana",14) ,corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="snew")
        if len(self.history_lists) == 0:
            self.empty_history()
        else:
            
            self.history_on()
        # self.load_history()
        self.load_data_HistoryList()

    # if the history list be empty this alert should appear
    def empty_history(self):
        self.grid_columnconfigure(0, weight=2)  # Column for EntryBox ---> makes it fate
        self.empty_title = customtkinter.CTkLabel(self, text="History list is empty right now !!",font=("Helvetica",14), fg_color="gray30", corner_radius=6,height=75)
        self.empty_title.grid(row=2, column=0, rowspan=2, padx=10, pady=(50, 50), sticky="nesw")
    
    # if any item were in history list list two title have to appear
    def history_on(self):

        if self.empty_title is not None:
            self.empty_title.destroy()
            self.empty_title = None 

        self.title = customtkinter.CTkLabel(self, text="Title name", fg_color="gray30", font=("Verdana",14),corner_radius=6)
        self.title.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nw")

        self.title = customtkinter.CTkLabel(self, text="status", fg_color="gray30", font=("Verdana",14),corner_radius=6)
        self.title.grid(row=2, column=1, padx=5, pady=(10, 0), sticky="")

    # to Save any action that happend in entryBox into a csv file
    def save_data_HistoryList(self , data):
            self.name , self.status = data
            with open("history_list_data.csv", "a") as file:
                    file.write(f"{self.name},{self.status}\n")
                    
    # to loud datas in csv file                 
    def load_data_HistoryList(self):
        try:
            with open("history_list_data.csv") as f:
                self.history_on()
                if f :
                    for line in f : 
                        item , status = line.rstrip().split(",")
                        title_item = customtkinter.CTkCheckBox(self, text=item, command=lambda: None)
                        title_item.grid(row=self.rows, column=0, padx=40, pady=(10, 0), sticky="w")
                        if status == "Added":
                            txt = customtkinter.CTkLabel(self, text=status, text_color="#2069A4", font=("Helvetica", 14, "bold"))
                            txt.grid(row=self.rows, column=1, padx=2, pady=(10, 0), sticky="w") 
                        elif status == "Removed":
                            txt = customtkinter.CTkLabel(self, text=status, text_color="#FF0000", font=("Helvetica", 14, "bold"))
                            txt.grid(row=self.rows, column=1, padx=2, pady=(10, 0), sticky="w") 
                        else :
                            txt = customtkinter.CTkLabel(self, text=status, text_color="#4CAF50", font=("Helvetica", 14, "bold"))
                            txt.grid(row=self.rows, column=1, padx=2, pady=(10, 0), sticky="w") 
                        self.rows += 1


        except FileNotFoundError:
            # If the file does not exist, simply ignore
            pass
        
    # To add items that added at the moment to History List from entryBox
    def check_Add(self , item_added):
        # Create a checkbox with the item added
        new_history_item = customtkinter.CTkCheckBox(self, text=f"{item_added}", command=lambda: None)
        new_history_item.grid(row=self.rows  , column=0, padx=7, pady=(10, 0), sticky="w")
        # Create a label for the added text
        txt = customtkinter.CTkLabel(self, text="Added", text_color="#2069A4", font=("Helvetica", 14, "bold"))
        txt.grid(row=self.rows  , column=1, padx=2, pady=(10, 0), sticky="w")
        self.rows += 1
        
        # Append the new checkbox to the history list
        self.history_lists.append(new_history_item)

        self.history_on()

# To add items that removed at the moment to History List from entryBox
    def check_remove(self , item_removed):
    # Create a checkbox with the item removed
        new_history_item = customtkinter.CTkCheckBox(self, text=(f"{item_removed}"), command=lambda: None)
        new_history_item.grid(row=self.rows, column=0, padx=7, pady=(10, 0), sticky="w")
        
        # Append the new checkbox to the history list
        self.history_lists.append(new_history_item)

        # Optionally, add a label for "Removed"
        removed_label = customtkinter.CTkLabel(self, text="Removed", text_color="#FF0000", font=("Helvetica", 14 ,"bold"))
        removed_label.grid(row=self.rows , column=1, padx=2, pady=(10, 0), sticky="w")

        self.rows += 1
        self.history_on()

# To add items that are Done at the moment to History List from entryBox
    def check_Done(self , item_Done):

        new_history_item = customtkinter.CTkCheckBox(self, text=(f"{item_Done}"), command=lambda: None)
        new_history_item.grid(row=self.rows , column=0, padx=7, pady=(10, 0), sticky="w")
        
        # Append the new checkbox to the history list
        self.history_lists.append(new_history_item)

        # Optionally, add a label for "Done"
        Done_label = customtkinter.CTkLabel(self, text="Done", text_color="#4CAF50", font=("Helvetica", 14 ,"bold"))
        Done_label.grid(row=self.rows, column=1, padx=2, pady=(10, 0), sticky="w")

        self.history_on()
        self.rows += 1
class EntryBox(customtkinter.CTkScrollableFrame):
    def __init__(self, History_list , master=None):
        super().__init__(master)
        self.History_list = History_list
        self.rows = 2
        self.items_in_entryBox = []
        self.items_for_historyList = []
        # Load previously saved data
        self.load_data_entryBox()

        
        self.title = customtkinter.CTkLabel(self, text="Add Your Title", fg_color="gray30",font=("Verdana",14), corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew",columnspan=1)
            # entry Box for writing titles
        self.entry = customtkinter.CTkEntry(self, corner_radius=5,width=400, placeholder_text="Type the Title:")
        self.entry.grid(row=1, column=0, padx=30, pady=(35, 0), sticky="new")
            # A button for move title from box to the list 
        self.button = customtkinter.CTkButton(self ,corner_radius=5, text="Add" ,font=("Tahoma" , 14) ,command=self.push_items)
        self.button.grid(row=2, column=1, padx=20, pady=(35, 0), sticky="ew")
            # A button for Items that have complited and are Done
        self.button = customtkinter.CTkButton(self ,corner_radius=5, text="Done" ,font=("Tahoma" , 14) , command=self.done)
        self.button.grid(row=3, column=1, padx=20, pady=(35, 0), sticky="ew")
            # A button if user want to remove a item from list
        self.button = customtkinter.CTkButton(self ,corner_radius=5, text="Remove" ,font=("Tahoma" , 14) , command=self.remove_item)
        self.button.grid(row=4, column=1, padx=20, pady=(35, 0), sticky="ew")


    def save_data_entryBox(self):
        self.data = [{"text": item.cget("text"), "selected": item.get(),"color": item.cget("text_color")} for item in self.items_in_entryBox]
        with open("history_entry_data.json", "w") as f:
            json.dump(self.data, f)
        
    def load_data_entryBox(self):
        try:
            with open("history_entry_data.json", "r") as f:
                content = f.read().strip()  # Read and strip whitespace
                if content:  # Only load if content is not empty
                    self.data = json.loads(content)
                    for entry in self.data:
                        title_item = customtkinter.CTkCheckBox(self, text=entry["text"], font=("Arial", 18, "bold"))
                        title_item.grid(row=self.rows, column=0, padx=40, pady=(10, 0), sticky="w") 

                        if entry["selected"] == 1:
                            title_item.select()  # Automatically select the checkbox if it was selected

                        self.items_in_entryBox.append(title_item)
                        self.rows += 1
                        

                        if entry["color"] == "#4CAF50":
                            title_item.configure(text_color=("#4CAF50"),font=("Helvetica",20,"bold"))
        except FileNotFoundError:
            # If the file does not exist, simply ignore
            pass
        except json.JSONDecodeError:
            # Handle the case where the JSON is invalid
            print("Error: Invalid JSON data in history_data.json. The file will be ignored.")
    def done(self ):
        for i in self.items_in_entryBox:
            if i.get() == 1: # This means that is the items were selected
                i.configure(text_color=("#4CAF50"),font=("Helvetica",20,"bold")) # It change the color of item 
                
                #   To orgnize any action that will happen in EntryBox in a list of dictionary for each item 
                self.History_list.save_data_HistoryList([i._text,"Done"]) 
                
                # To add item name to History_list class to Add it at the moment
                self.History_list.check_Done(i._text)
                
                # this loop will change the color injson file if the item were done
                for item in self.data : 
                    if item["text"] == i.cget("text"):
                        item["color"] = "#4CAF50"
            else:
                None
        self.save_data_entryBox()

    def push_items(self):
        if self.entry.get():
            
            if len(self.items_in_entryBox) == 0:
                self.rows = 2
            if re.match(r"^(?=.*\S)[a-zA-Z0-9\s]+$",self.entry.get()):
                
                title_item = customtkinter.CTkCheckBox(self, text=self.entry.get(), font=("Arial", 18, "bold"))
                title_item.grid(row=self.rows, column=0, padx=40, pady=(10, 0), sticky="w")


                #   This line will add a list in "History_list class ===> save_data_HistoryList function" and pass as "data"
                self.History_list.save_data_HistoryList([title_item._text,"Added"]) 

                # Call the check_event method in History_list with the new item's text
                self.History_list.check_Add(self.entry.get())

                self.rows += 1
                self.entry.delete(0, 'end')
                self.items_in_entryBox.append(title_item)
            else:
                self.show_warning("Please enter a value!")
        else:
             self.show_warning("Please enter a value!")
        # save datas 
        self.save_data_entryBox()
        # to add datas to save_HistoryList methods
        self.History_list.save_data_HistoryList(self.items_for_historyList)
    def remove_item(self):
        items_to_remove = [item for item in self.items_in_entryBox if item.get() == 1]
        
        if not items_to_remove:
            self.rows = 2
            self.show_warning("Please select an item!")
            return
        
        for item in items_to_remove:
            #   To orgnize any action that will happen in EntryBox in a list of dictionary for each item 
            self.History_list.save_data_HistoryList([item._text,"Removed"]) 

            item.grid_forget()  # Remove the checkbox from the grid
            self.History_list.check_remove(item._text) # For add items that removed to history_list
            self.items_in_entryBox.remove(item)  # Remove from the list

        # Update the grid positions of remaining items
        self.update_item_positions()
        
        self.save_data_entryBox()
        # to add datas to save_HistoryList methods
        self.History_list.save_data_HistoryList(self.items_for_historyList)
        
    # this function will call when ever rows be need to update like when ever a item remove    
    def update_item_positions(self):
        for index, item in enumerate(self.items_in_entryBox):
            item.grid(row=index + 2, column=0, padx=40, pady=(10, 0), sticky="w")  # Adjust row index as needed
            
    # This function is for show warning if the user doesn`t enter a value or Removing a item without selecting it
    def show_warning(self, message):
        # Create a new top-level window for the warning
        warning_window = customtkinter.CTkToplevel(self)
        warning_window.title("Warning")
        warning_window.geometry("250x100")
        warning_window.attributes("-topmost", True)

        # Center the warning window
        x = self.winfo_x() + (self.winfo_width() // 2) - 125
        y = self.winfo_y() + (self.winfo_height() // 2) - 50
        warning_window.geometry(f"250x100+{x}+{y}")

        # Warning message label
        warning_label = customtkinter.CTkLabel(warning_window, text=message)
        warning_label.pack(pady=10)

        # Button to close the warning window
        close_button = customtkinter.CTkButton(warning_window, text="Close", command=warning_window.destroy)
        close_button.pack(pady=5)

class Todo(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ToDo List")
        self.geometry("1130x550")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        self.resizable(width=True, height=True)

        # Configure grid weights
        self.grid_columnconfigure(0, weight=1)  # Column for history_list and style_mode
        self.grid_columnconfigure(1, weight=2)  # Column for EntryBox ---> makes it fater

        # Set row weights
        self.grid_rowconfigure(0, weight=1)  # For History_list
        self.grid_rowconfigure(1, weight=1)  # For MyStylebox
        self.grid_rowconfigure(2, weight=1)  # For EntryBox

        EachClass(self)


def main():
    app = Todo()
    app.mainloop()

def light_button():
    return customtkinter.set_appearance_mode("light") # to Make mode light

def dark_button():
    return customtkinter.set_appearance_mode("dark")  # to Make mode dark
    
def EachClass(todo_instance):
    # For History_list
    history_list = History_list(master=todo_instance)
    history_list.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

    # For style_mode
    style_mode = MyStylebox(master=todo_instance)
    style_mode.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="nsw")

    # For entry box
    entry_box = EntryBox(history_list,master=todo_instance)
    entry_box.grid(row=0, column=1, rowspan=2, padx=10, pady=(10, 5), sticky="nsew")  # Full height

if __name__ == "__main__":
    main()