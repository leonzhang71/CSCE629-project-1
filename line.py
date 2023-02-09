'''
#examples_of_instances
#first solution for reading the file
#filepath = '../data/test.txt'
#can switch the file name into filepath
#hello
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
that line print all list and data set
print(obj)
that line print special 'list' with full data set
print(obj["x_list"][0])
that line print the len() special data set in that list
print (len(obj["x_list"]))
this part is to use obj["x_list"][0][0] to pick up the value for data file
print(obj["x_list"][0][0])
print(len(obj["x_list"][0]))
print(obj["y_list"][0])
using loop to find and print every element for obj["x_list"][0])
'''


import pickle as pkl
import matplotlib.pyplot as plt

with open("examples_of_instances", 'rb') as f:
    obj = pkl.load(f)


x_list_copy = [x for sublist in obj["x_list"] for x in sublist]
y_list_copy = [y for sublist in obj["y_list"] for y in sublist]

'''
for x in x_list_copy:
    print("x=", float(x))

for y in y_list_copy:
    print("y=", float(y))
'''

plt.scatter(x_list_copy,y_list_copy, c = 'red')
plt.show()

