import json
import tkinter as tk
from collections import defaultdict
import os
import os.path as pt
dict_obj = {"name": "John", "age": 30}
class Save:
    def __init__(self,filename:str):
        self.FILE_NAME = filename
        self.PATH_PREFIX = "C:\\ProgramData\\"
        self.FOLDER_NAME = "LinkManager"
        self.PATH = pt.join(self.PATH_PREFIX,self.FOLDER_NAME)
        self.PATH_FILE = pt.join(self.PATH,self.FILE_NAME) +".json"
        print(self.PATH_FILE)
        if pt.exists(self.PATH) == False:
            try:
                os.mkdir(self.PATH)
            except OSError:
                print ("Creation of the directory %s failed" % self.PATH)
                tk.messagebox.showerror("Error", "Failed To Create File")
                
            if pt.isfile(self.PATH_FILE) == False:
                with open(self.PATH_FILE, "w") as my_dict_file:
                    pass
       
                
    # Read the JSON file and parse into a dictionary object
    def ReadData(self) -> dict:
        try:
            with open(self.PATH_FILE, "r") as dataFile:
                read_dict_obj = json.load(dataFile)
                print("Data Retrived")
                return read_dict_obj
        except:
            return defaultdict(list)
        
        
    # Write the dictionary object to a JSON file
    def WriteData(self,data):     
        with open(self.PATH_FILE, "w") as my_dict_file:
            json.dump(data, my_dict_file)
            print("Data Saved")


