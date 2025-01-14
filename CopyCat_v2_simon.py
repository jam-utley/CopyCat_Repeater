# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:16:29 2025

@author: utley
"""

import tkinter as tk
import csv
import time

#with open('buttonRecord.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows([['Button Color', 'Timestamp', 'Time to hit the button']])

def on_button_click():
    button_time_A = time.perf_counter()      #Measures time in nanoseconds
#    button_time_B = button_time_A
    
    print("Click Acknowledged")
    print(button_time_A)

def elapsed_time():
    """Calculates the time elapsed between presses of buttons"""
    import pandas as pd
    elapsedTime = []                #WAIT: For some reason, this code is running first so it is being read as empty because there is NOTHING in it
    data = pd.read_csv('buttonRecord.csv', sep = ',')
    print(data)
    for i in range(len(data)):
        if i == 0:      #If it is the first go through, just appends 0 because there is nothing to compare it to before it.
            elapsedTime.append(0)
        else:
            elapsedTime.append(data[i]-data[i-1])
    print(elapsedTime)
    data['Elapsed Time'] = elapsedTime
    print('calculations of elapsed time complete')

class SimonSays (tk.Tk):        #This is the main page
    def __init__(self):
        super().__init__()
        self.title("Simon Says")    #Setting up title and size of the window
        self.geometry("900x300")
        
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
    
    def show_page(self, page_class):            #The show_page function
        """Show a frame for the given page class."""
        page = self.pages[page_class]
        page.tkraise()

class PageOne(tk.Frame):        #Main page
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Add widgets to the page
        label = tk.Label(self, text="Welcome to Simon Says. Press \"Begin\" to begin recording and then I will repeat your inputs.", font=("Arial", 16), anchor = "center")
        label.pack(pady=20)    #pady= gives distance between objects in tkinter
        
        # Button to go to Page Two
        button = tk.Button(self, text="Begin", command=lambda: controller.show_page(PageTwo), anchor = 'center')
        button.pack(expand = True)

class PageTwo(tk.Frame):        #Button Page
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
         # Add widgets to the page
        label = tk.Label(self, text="Type a pattern into the buttons below", font=("Arial", 16))
        label.pack(pady=20)

        buttonBlue = tk.Button(self, text="Blue", command=lambda: (recordPress("Blue"), controller.show_page(PageTwo)))   #Records Blue Button being pressed and refreshes the page so it can be pressed again
        buttonBlue.pack(pady = 20)
        buttonStop = tk.Button(self, text ="End Recording", command=lambda: controller.show_page(PageThree))   #Moves to Page three
        buttonStop.pack()

class PageThree(tk.Frame):      #Repeats your responses back to you at the same rate as you pressed them
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        if __name__ == "__main__":
            elapsed_time()
        label = tk.Label(self, text = "Your responses were: \n", font =("Arial", 16))
        label.pack(pady = 20)
        label =tk.Label(self, text = 123)
        label.pack(pady = 20)

class PageFinal:
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text = "Thank you for playing. See you next time!", font =("Arial", 16))
        label.pack(pady = 20)

def recordPress(buttonColor):
    """Records which button is pressed and the time stamp of the press."""
    import time
    import csv
    import pandas as pd
#    data = {'Color':[buttonColor], 'Timestamp':[time.perf_counter()]}
#    dFrame = pd.DataFrame(data)
#    dFrame.to_csv('buttonRecord.csv', header = True)
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