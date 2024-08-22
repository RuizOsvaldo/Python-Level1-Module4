"""
Log Search using a Id-Name Dictionary
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

# TODO: Create a dictionary of integers for the keys and strings for the values.
#  Create a GUI app with three buttons. Look at 'log_search_example.png' in this
#  folder for an example of what your program should look like.
#
#  Button 1: Add Entry
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      After an ID is entered, use another input dialog to ask the user
#      to enter a name. Add this information as a new entry to your
#      dictionary.

#  Button 2: Search by ID
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      If that ID exists, display that name to the user.
#      Otherwise, tell the user that that entry does not exist.
#
# Button 3: View List
#      When this button is clicked, display the entire list in a message
#      dialog in the following format:
#      ID: 123  Name: Harry Howard
#      ID: 245  Name: Polly Powers
#      ID: 433  Name: Oliver Ortega
#      etc...
#
# When this is complete, add a fourth button to your window.
# Button 4: Remove Entry
#      When this button is clicked, prompt the user to enter an ID using
#      an input dialog.
#      If this ID exists in the dictionary, remove it. Otherwise, notify the
#      user that the ID is not in the list.
#

#Creating LogSearch class and inheriting tk module
class LogSearch(tk.Tk):
    
    #Constructor for class
    def __init__(self):
        super().__init__()

        self.title("Log Search")
        self.geometry("500x300")

        #Dictionary for the entries.
        self.entries = {}

        #Initializing buttons for GUI.
        add_button = tk.Button(self, text="Add Entry", command=self.add_entry)
        search_button = tk.Button(self, text="Search Entry", command=self.search_entry)
        view_button = tk.Button(self, text="View List", command=self.view_list)
        remove_button = tk.Button(self, text="Remove Entry", command=self.remove_entry)

        #Packing Buttons to frame.
        add_button.pack(pady=10)
        search_button.pack(pady=10)
        view_button.pack(pady=10)
        remove_button.pack(pady=10)


    #Add Entry function
    def add_entry(self):
        id_number = simpledialog.askinteger("ID Number", "Enter an ID number")

        #Assuring ID_number input is a number before asking for a name.
        if id_number is not None:
            if id_number in self.entries:
                    messagebox.showerror("ID Number Error", "ID already exists. Enter a new ID")
                    return
            
            name = simpledialog.askstring("Name", "Enter a name.")

            #Checking to see if name is not empty and is a string.
            if name is not None and name.isalpha():
                 self.entries[id_number] = name
                 messagebox.showinfo("Add Entry", f"Entry added: ID {id_number}, Name {name}")

    #Search Entry Function
    def search_entry(self):
        id_number = simpledialog.askinteger("ID Number", "Enter an ID number")
    
        #Assuring ID_number input is a number before asking for a name.
        if id_number is not None:
            if id_number not in self.entries:
                messagebox.showerror("ID Number Error", "ID doesn't exist. Enter a new ID.")
                return
            else:
                 messagebox.showinfo("Search Entry", f" Entry located: ID {id_number}, Name {self.entries[id_number]}")

    #View List Function
    def view_list(self):
        #Checking to see if entries is empty
        if not self.entries:
            messagebox.showerror("Empty List", "There are no entries.")
            return
        
        #Adding entries to string variable and printing
        entry_list = "\n".join([f"ID {id}, Name {name}" for id, name in self.entries.items()])
        messagebox.showinfo("List of Entries", entry_list)

    #remove_entry function
    def remove_entry(self):
        if not self.entries:
            messagebox.showerror("Empty List", "There is nothing to remove, there are no entries.")
            return
        
        id_number = simpledialog.askinteger("ID Number", "Enter an ID number to remove.")

        #Assuring ID_number input is a number before asking for a name.
        if id_number is not None and id_number not in self.entries:
            messagebox.showerror("ID Number Error", "ID does not exist or not valid. Enter a new ID")
            return
        else:
            del self.entries[id_number]
            messagebox.showinfo("Entry Removed", f"ID {id_number} has been removed.")
 
if __name__ == "__main__":
    app = LogSearch()
    app.mainloop()
        