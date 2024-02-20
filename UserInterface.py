import tkinter as tk
import tkinter.font as tkFont
class App:
    def __init__(self, root):
        #setting title
        root.title("Link Manager")
        #setting window size
        width=500
        height=350
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.LinkList_List=tk.Listbox(root)
        self.LinkList_List["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.LinkList_List["font"] = ft
        self.LinkList_List["fg"] = "#333333"
        self.LinkList_List["justify"] = "center"
        self.LinkList_List.place(x=10,y=10,width=142,height=179)
        self.LinkList_List["exportselection"] = "0"
        self.LinkList_List["selectbackground"] = "#393d49"
        self.LinkList_List["selectforeground"] = "#00babd"
        self.LinkList_List["selectmode"] = "single"

        self.LinkList=tk.Listbox(root)
        self.LinkList["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.LinkList["font"] = ft
        self.LinkList["fg"] = "#333333"
        self.LinkList["justify"] = "center"
        self.LinkList["exportselection"] = "0"
        self.LinkList.place(x=160,y=10,width=330,height=179)

        self.addUrl=tk.Button(root)
        self.addUrl["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.addUrl["font"] = ft
        self.addUrl["fg"] = "#000000"
        self.addUrl["justify"] = "center"
        self.addUrl["text"] = "Add"
        self.addUrl.place(x=420,y=200,width=70,height=25)

        self.removeLink=tk.Button(root)
        self.removeLink["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.removeLink["font"] = ft
        self.removeLink["fg"] = "#000000"
        self.removeLink["justify"] = "center"
        self.removeLink["text"] = "Remove"
        self.removeLink.place(x=340,y=230,width=70,height=25)

        self.OpenLink=tk.Button(root)
        self.OpenLink["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.OpenLink["font"] = ft
        self.OpenLink["fg"] = "#000000"
        self.OpenLink["justify"] = "center"
        self.OpenLink["text"] = "Open"
        self.OpenLink.place(x=420,y=230,width=70,height=25)
        self.OpenLink["command"] = self.GButton_670_command

        self.AddLinkList=tk.Button(root)
        self.AddLinkList["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.AddLinkList["font"] = ft
        self.AddLinkList["fg"] = "#000000"
        self.AddLinkList["justify"] = "center"
        self.AddLinkList["text"] = "Add New List"
        self.AddLinkList.place(x=390,y=280,width=100,height=25)
        self.AddLinkList["command"] = self.GButton_556_command

        self.url_entry=tk.Entry(root)
        self.url_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.url_entry["font"] = ft
        self.url_entry["fg"] = "#333333"
        self.url_entry["justify"] = "left"
        self.url_entry["text"] = "Entry"
        self.url_entry.place(x=80,y=200,width=329,height=25)

        self.GLabel_802=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_802["font"] = ft
        self.GLabel_802["fg"] = "#333333"
        self.GLabel_802["justify"] = "left"
        self.GLabel_802["text"] = "Enter Link :"
        self.GLabel_802.place(x=10,y=200,width=70,height=25)

        self.GLabel_327=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_327["font"] = ft
        self.GLabel_327["fg"] = "#333333"
        self.GLabel_327["justify"] = "left"
        self.GLabel_327["text"] = "List Name: "
        self.GLabel_327.place(x=10,y=280,width=70,height=25)

        self.LinkList_Name=tk.Entry(root)
        self.LinkList_Name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.LinkList_Name["font"] = ft
        self.LinkList_Name["fg"] = "#333333"
        self.LinkList_Name["justify"] = "left"
        self.LinkList_Name["text"] = "Entry"
        self.LinkList_Name.place(x=80,y=280,width=300,height=25)

        self.DeleteLinkList=tk.Button(root)
        self.DeleteLinkList["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.DeleteLinkList["font"] = ft
        self.DeleteLinkList["fg"] = "#000000"
        self.DeleteLinkList["justify"] = "center"
        self.DeleteLinkList["text"] = "Delete"
        self.DeleteLinkList.place(x=340,y=310,width=70,height=25)

        self.OpenAllLinks=tk.Button(root)
        self.OpenAllLinks["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.OpenAllLinks["font"] = ft
        self.OpenAllLinks["fg"] = "#000000"
        self.OpenAllLinks["justify"] = "center"
        self.OpenAllLinks["text"] = "Open All"
        self.OpenAllLinks.place(x=420,y=310,width=70,height=25)

        # self.GButton_40=tk.Button(root)
        # self.GButton_40["bg"] = "#f0f0f0"
        # ft = tkFont.Font(family='Times',size=10)
        # self.GButton_40["font"] = ft
        # self.GButton_40["fg"] = "#000000"
        # self.GButton_40["justify"] = "center"
        # self.GButton_40["text"] = "Edit Name"
        # self.GButton_40.place(x=260,y=310,width=70,height=25)
        # self.GButton_40["command"] = self.GButton_40_command
    def GButton_665_command(self):
        print("command")
    def GButton_867_command(self):
        print("command")
    def GButton_670_command(self):
        print("command")
    def GButton_556_command(self):
        print("command")
    def GButton_996_command(self):
        print("command")
    def GButton_441_command(self):
        print("command")
    def GButton_40_command(self):
        print("command")
    def nall(self, master):
        self.master = master
        master.title("Link Manager")
        master.geometry("500x300")

        # Set colors and fonts
        self.bg_color = "lightgray"
        self.text_color = "black"
        self.button_color = "blue"
        self.button_text_color = "white"
        self.list_bg_color = "white"
        self.list_text_color = "black"
        self.font_labels = "Sans Serif"
        self.font_listbox = "FixedSys"
        self.font_buttons = "Sans Serif Bold"

        # Create UI elements
        self.links_list = []
        self.links_listbox = tk.Listbox(master, selectmode=tk.SINGLE, bg=self.list_bg_color, fg=self.list_text_color, font=self.font_listbox)
        self.links_listbox.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW, padx=10, pady=10)

        self.url_entry = tk.Entry(master, bg=self.bg_color, fg=self.text_color, font=self.font_labels)
        self.url_entry.grid(row=1, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add Link", command=self.add_link, bg=self.button_color, fg=self.button_text_color, font=self.font_buttons)
        self.add_button.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)

        self.remove_button = tk.Button(master, text="Remove Link", command=self.remove_link, bg=self.button_color, fg=self.button_text_color, font=self.font_buttons)
        self.remove_button.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

        self.open_button = tk.Button(master, text="Open Link", command=self.open_selected_link, bg=self.button_color, fg=self.button_text_color, font=self.font_buttons)
        self.open_button.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # ... (rest of the code)
    