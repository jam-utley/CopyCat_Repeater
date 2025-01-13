# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:04:55 2025

@author: utley
"""

def copycat_binary_record():
    """
    Takes input of either a zero or a one, writes it to a dedicated file
    """
    with open('cc_binary_record.txt', 'w') as f:    #Opens and closes the file, clearing it.
        pass
    first_time_counter = 0
    num_in = int(input("Enter a 0 or a 1. Press 2 to stop."))
    num_in_list = []
    playagain = 0       #Variable that when above zero will stop the recording process.
    f = open('cc_binary_record.txt', 'r+')
    while playagain <1:
        num_in_list = list(num_in_list)
        while num_in > 2 or num_in<0:     #Error checking
            num_in = int(input("Please enter a valid selection."))
        num_in_list.clear()
        while num_in < 2:            
            num_in_list.append(num_in)       #Appends the input into a list
            num_in = int(input("Enter a 0 or a 1. Press 2 to stop."))   #Gets a new input
        if first_time_counter > 0:
            first_time_counter +=1
            num_in_list = str(num_in_list)
            f.write(f"Session {first_time_counter}: {num_in_list}")   #Writes the binary list to the file
            f.write('\n')
        else:   #If it's the first time, it records:
           
            num_in_list = str(num_in_list)
            f.write(f"Session 1: {num_in_list}")   #Writes the binary list to the file
            f.write('\n')
            first_time_counter += 1
        endit = input("Do you wish to record another session? Y/N ")
        if endit.lower() == 'n':    #Adds an exit criterium for the loop
            playagain = 1  
            f.close()
        else:
            num_in = int(input("Enter a 0 or a 1. Press 2 to stop."))
    print("Recording complete.")

def copycat_binary_read(session_num):
    """
    Reads the binary file at a specified line number corresponding to the session recorded.
    """
    f = open('cc_binary_record.txt', 'r')
    for i in range(session_num):
        line = f.readline()
    if line == '':
        print("No recorded session.")
    else:
        print(line)
    return(None)

#copycat_binary_record()
copycat_binary_read(int(input("which number session do you want to see?")))