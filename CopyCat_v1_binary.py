# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:27:07 2025

@author: utley
"""

def copycat_binary_record():
    """
    Takes input of either a zero or a one, writes it to a dedicated file
    """
    first_time_counter = 0
    num_in = int(input("Enter a 0 or a 1. Press 2 to stop."))
    num_in_list = []
    again = 0       #Variable that when above zeero will stop the encoding process.
    while again <1:
        num_in_list = list(num_in_list)
        while num_in > 2 or num_in<0:     #Error checking
            num_in = int(input("Please enter a valid selection."))
        while num_in < 2:
            num_in_list.append(num_in)       #Appends the input into a list
            num_in = int(input("Enter a 0 or a 1. Press 2 to stop."))   #Gets a new input
        if first_time_counter > 0:
            print("eek")
            with open("cc_binary_record.txt", 'r') as f:
                for line in f:  #Reads the last line and stores it in a variable for slicing
                    pass
                lastline = line
                (left,sep,right) = lastline.partition(':')   #partitions the string to find the version number
                session_num = left[-1]             #Finds the previous session number and records it
                session_num = int(session_num)
            with open("cc_binary_record.txt", 'w') as f:
                num_in_list = str(num_in_list)
                session_num += 1
                f.write("Session v")   #Records session version
                session_num = str(session_num)
                f.write(session_num)   #Version number
                f.write(":")           #Adds a colon afte the version number
                f.write(num_in_list)   #Writes the binary list to the file
        else:
            with open("cc_binary_record.txt", 'w') as f:  #For the first time through the file
                num_in_list = str(num_in_list)
                f.write("Session v1: ")   #Records session version
                f.write(num_in_list)   #Writes the binary list to the file
                f.write('\n')
            first_time_counter += 1
        endit = input("Do you wish to encode another session? Y/N ")
        if endit.lower() == 'n':    #Adds an exit criterium for the loop
            again = 1  
        else:
            num_in = int(input("Enter a 0 or a 1. Press 2 to stop."))
    print("Encoding complete.")

def copycat_binary_read(ver_num):
    """
    Reads the binary file at a specified line number corresponding to the session recorded.
    """

    return(None)

copycat_binary_record()