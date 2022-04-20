"""
    Filename: list_handler.py
    Author: rathorsunpreet
    License: GNU GPLv3
"""
# Method to replace $variables in string
def replace_placeholder(rec, sender="Sunpreet"):
    tmp = ""
    # Return dictionary with email : body pair
    return tmp

# Strips : from option_file.txt and returns dictionary with
# Option : Setting pair
def strip_option(opt):
    ind_lines = [x[:-1] for x in opt]   # Strip trailing \n char

    # Return dictionary
    return dic

# Strips provided list and returns a new list 
def strip_r_list(rec):
    new_lines = [x[:-1] for x in rec]     # Strip trailing \n char
    corrected_lines = [i.split("-") for i in new_lines]     # Strip "-"
    return corrected_lines

# Add formatting to list and return a new list
def create_r_list(rec):
    inner_list = ""
    new_list = []
    # rec is a 2D list
    for outer in rec:
        inner_list = '-'.join(outer)
        inner_list += '\n'
        new_list.append(inner_list)
    return new_list

l = [["R","Sloana Botswarth","sbotswarth@gmail.com","Software Tester"], ["H","Henry Adams","hadams@yahoo.com","Javascript Developer"]]

print(create_r_list(l))
