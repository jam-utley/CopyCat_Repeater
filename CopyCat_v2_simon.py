# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:16:29 2025

@author: utley
"""

import tkinter as tk
import csv
import time

with open('buttonRecord.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([['Button Color', 'Timestamp']])

def on_button_click():
    button_time_A = time.perf_counter()      #Measures time in nanoseconds
#    button_time_B = button_time_A
    
    print("Click Acknowledged")
    print(button_time_A)

def elapsed_time(timeA, timeB):
    return(timeB-timeA)

class SimonSays (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simon Says")
        self.geometry("800x300")
        
        # Create a container for all pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        # Dictionary to hold pages
        self.pages = {}
        
        # Initialize pages
        for Page in (PageOne, PageTwo, PageThree):
            page = Page(parent=self.container, controller=self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")
        
        # Show the first page
        self.show_page(PageOne)
    
    def show_page(self, page_class):
        """Show a frame for the given page class."""
        page = self.pages[page_class]
        page.tkraise()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Add widgets to the page
        label = tk.Label(self, text="Welcome to Simon Says. Press \"Begin\" to begin recording and then I will repeat your inputs.", font=("Arial", 16))
        label.pack(pady=20)
        
        # Button to go to Page Two
        button = tk.Button(self, text="Begin", command=lambda: controller.show_page(PageTwo))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
         # Add widgets to the page
        label = tk.Label(self, text="Type a pattern into the buttons below", font=("Arial", 16))
        label.pack(pady=20)

        buttonBlue = tk.Button(self, text="Blue", command=lambda: (recordPress("Blue"), controller.show_page(PageTwo)))   #Records Blue Button being pressed
        buttonBlue.pack()
        buttonStop = tk.Button(self, text ="End Recording", command=lambda: controller.show_page(PageThree))
        buttonStop.pack()

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text = "Thank you for playing. See you next time!", font =("Arial", 16))
        label.pack(pady = 20)

def recordPress(buttonColor):
    """Records which button is pressed and the time stamp of the press."""
    import time
    import csv
    with open("buttonRecord.csv", 'a', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow([buttonColor, time.perf_counter()])
    
        

if __name__ == "__main__":
    app = SimonSays()
    app.mainloop()
    

#Steps for CopyCat v2 code
#Record button presses and time elapsed between presses in dictionary
#dictionary format --   button_pressed:time_elapsed
#So need button code and time tracking code to write to probably a csv file.