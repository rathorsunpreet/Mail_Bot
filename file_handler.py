"""
    Filename: file_handler.py
    Author: rathorsunpreet
    License: GNU GPLv3
"""

"""
File Formats:
    r_list.txt:
    Identifier,Name,Email Adress,Position,Date
    The header is marked with a #.
    So header becomes: #,Id,Name,Email,Address,....

    body_file.txt:
    Normal Email Body with $variables, to be substituted from r_list.txt

    option_file.txt:
    Option: Value

    Note:
    In all three files anything preceded by # is to be considered
    as a comment and not evaluated
"""

import csv

# File Handlers
r_file = None   # Recipient File 
b_file = None   # Body File
o_file = None   # Options File

# Boolean to check if file was created
r_check = False
b_check = False
o_check = False

# Method to open recipient and body files based on ftype variable's value
# Correlation between ftype and different files.
# ftype         file to open
# 0             r_file
# 1             b_file
# 2             o_file
def open_file(ftype):
    # Use the global variables
    global r_file, b_file, o_file
    global r_check, b_check, o_check
    # Open recipient file
    if ftype == 0:
        try:
            r_file = open("r_list.txt","r+")
        except:
            print ("r_list.txt does not exist, creating new one!")
            r_file = open("r_list.txt","w+")
            r_check = True
        return r_check
    # Open body file
    elif ftype == 1:
        try:
            b_file = open("body_file.txt", "r+")
        except:
            print ("body_file.txt do not exist, creating new one!")
            b_file = open("body_file.txt", "w+")
            b_check = True
        return b_check
    else:
        try:
            o_file = open("option_file.txt", "r+")
        except:
            print ("option_file.txt do not exist, creating new one!")
            o_file = open("option_file.txt", "w+")
            o_check = True
        return o_check

# File lines read from r_list.txt
lines = []
# File content of body_file.txt
b_content = ""
# Content of option_file.txt
o_content = [] 

# Method to read contents of each file
# Correlation between ftype and different files.
# ftype         file to open
# 0             r_file
# 1             b_file
# 2             o_file
def read_file(ftype):
    # Recipient File Operations
    if ftype == 0:
        # Check if files existed, extract info into list
        if r_check == False:
            reader = csv.reader(r_file, delimiter=',', skipinitialspace=True)      # allows for format data, data, data
            for row in reader:
                if '#' in row:
                    continue
                else:
                    lines.append(row)
            return lines
    # Body File Operations
    elif ftype == 1:
        if b_check == False:
            b_content = b_file.read()
            return b_content
    # Option File Operations
    else:
        if o_check == False:
            o_content = o_file.readlines()
            return o_content

# Method to write to each file
# Correlation between ftype and different files.
# ftype         file to open
# 0             r_file
# 1             b_file
# 2             o_file
def write_file(ftype, content):
    # Recipient File Operations
    if ftype == 0:
        r_file.write(content)
        print("Recipient File written")
    # Body file Operations
    elif ftype == 1:
        b_file.write(content)
        print("Body File written")	
    # Option file Operations
    else:
        o_file.write(content)
        print("Option File written")	

# Method to close file
# Correlation between ftype and different files.
# ftype         file to open
# 0             r_file
# 1             b_file
# 2             o_file
def close_file(ftype):
    if ftype == 0:
        r_file.close()
    elif ftype == 1:
        b_file.close()
    else:
        o_file.close()


# Test Statements
open_file(0)
print(read_file(0))
close_file(0)
