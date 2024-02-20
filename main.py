import tkinter as tk
from tkinter import messagebox 
import webbrowser
import validators
import tkinter.font as tkFont
import UserInterface
from collections import defaultdict
import SaveData

class LinkManager:
    
    def __init__(self,root) :
        self.SaveData = SaveData.Save("LinkManager")
      
        self.links_list = defaultdict(list) 
        self.links_list = (self.SaveData.ReadData())
        self._init_ui(root)
        print(self.links_list)
        self.LoadLinkLists()
        
    # initialise ui elements
    def _init_ui(self,root):
        self.ui = UserInterface.App(root)
        self.ui.addUrl["command"] = self.add_link
        self.ui.removeLink["command"] = self.remove_link
        self.ui.OpenLink["command"] = self.open_selected_link
        self.ui.AddLinkList["command"] = self.AddLinkList
        self.ui.DeleteLinkList["command"] = self.DeleteLinkList
        self.ui.OpenAllLinks["command"] = self.OpenAllLinks
        self.ui.LinkList_List.bind('<<ListboxSelect>>',self.OnLinkChange)
        
    # adds link to the linklist of the current selected list   
    def add_link(self):
        listname,index = self.GetActiveList()
        new_link = self.ui.url_entry.get()
        self.ui.url_entry.delete(0, tk.END) 
        # Error handling for Selected List
        if listname == "null":
            tk.messagebox.showerror("Error", "Select a List First. If No list then Creat one.")
            
        # Error handling for invalid URLs
        if not new_link  :
            return  
        elif  not validators.url(new_link):
            tk.messagebox.showerror("Error", "Invalid URL. Please enter a valid link.")
            return
        
        # Remove duplicates and handle empty input
        if new_link not in self.links_list:
            self.links_list[listname].append(new_link)
            self.ui.LinkList.insert(tk.END, new_link)
            
        # Writes Data to file
        self.SaveData_Write()
        
    # remove links from the selected list
    def remove_link(self):
        
        selected_index = self.ui.LinkList.curselection()
        selected_list,index = self.GetActiveList()
        #checks if list is selected
        if selected_index:
            print(selected_index[0],self.links_list)
            del self.links_list[selected_list][selected_index[0]] #delete selected link
            self.ui.LinkList.delete(selected_index[0]) 
        # Writes Data to file
        self.SaveData_Write()
    # Opens selected link in default browser
    def open_selected_link(self):
        selected_index = self.ui.LinkList.curselection()
        if selected_index:
            selected_link = self.ui.LinkList.get(selected_index)
            webbrowser.open(str(selected_link))
    # Returns selected list (list_name,list_index)
    def GetActiveList(self):
        selection =  self.ui.LinkList_List.curselection()
        if (selection == None or selection == ()):
            return "null",-1
        else:
            print("get",selection)
            print("get",self.ui.LinkList_List.get(selection))
            return self.ui.LinkList_List.get(selection),selection
        
    # Adds New List
    def AddLinkList(self):
        new_list = self.ui.LinkList_Name.get()
        self.ui.url_entry.delete(0, tk.END)  # Clear entry after adding
        print("List before Added",self.links_list)

        # Enhanced behavior: Remove duplicates and handle empty input
        if new_list not in self.links_list and new_list != "null":
            self.links_list[new_list] = []
            self.ui.LinkList_List.insert(tk.END, new_list)
        print("List Added",self.links_list)
        # Writes Data to file
        self.SaveData_Write()
        
    # Deletes Selected List
    def DeleteLinkList(self):
        selected_index = self.ui.LinkList_List.curselection()
        if selected_index:
            # selected_link = self.links_list[selected_index[0]]
            listname,index =  self.GetActiveList()
            print(listname,index)
            if listname != None and listname in self.links_list.keys():
                del self.links_list[listname]
                self.ui.LinkList_List.delete(index)
        # Writes Data to file
        self.SaveData_Write()
                
    # Called when the selected list is changed 
    # displays the links in the selected list
    def OnLinkChange(self,event):
        print("call",str(event))
        self.ui.LinkList.delete(0,tk.END)
        selected,index = self.GetActiveList()
        if self.links_list != None and self.links_list:
            for link in self.links_list[selected]:
                self.ui.LinkList.insert(tk.END,link) 
            print("onlinkchanged",self.links_list)
            
    # Opens all the links in selected list in default browser
    def OpenAllLinks(self):
        selected,index = self.GetActiveList()
        if self.links_list != None and self.links_list:
            for link in self.links_list[selected]:
                webbrowser.open(str(link))
            print("Opening All Link",str(link))
            
    # Displays the Lists
    def LoadLinkLists(self):
        for ListName in self.links_list:
            self.ui.LinkList_List.insert(tk.END,ListName)
        self.ui.LinkList_List.selection_set(0)
        self.OnLinkChange(None)
    
    # Writes Data to file
    def SaveData_Write(self):
        self.SaveData.WriteData(self.links_list)
        
root = tk.Tk()
link_manager = LinkManager(root)

root.mainloop()

