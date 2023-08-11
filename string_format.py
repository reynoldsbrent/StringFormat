"""
Read the file line by line and create a list of tuples.
Each tuple contains the item (string), the number of items (integer) the price per item (float).
To identify the individual parts per line, use the method .split(). Prepare an f-string to output the data as specified.
"""

list_of_tup = []
line_list = []
line_tuple = ()
with open("invoice_data.txt", 'r')  as file:
    for line in file:
        line_list = line.split()
        line_tuple = (line_list[0], int(line_list[1]), float(line_list[2]))
        list_of_tup.append(line_tuple)

for product in list_of_tup:
    print(f"{product[0]:15s} {product[1]:3d} {product[2]:7.2f} {product[1]*product[2]:8.2f}")