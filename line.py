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
for i in range (len(obj["x_list"])):
    for j in range (len(obj["x_list"][i])):
        print("x=", float(obj["x_list"][i][j]))
'''


import pickle as pkl
import matplotlib.pyplot as plt

with open("examples_of_instances", 'rb') as f:
    obj = pkl.load(f)

'''
#O(n^2) to find all element in one list
i = 0
j = 0
for i in range (len(obj["x_list"])):
    for j in range (len(obj["x_list"][i])):
        print("x=", float(obj["x_list"][i][j]))
'''

#list for x,y
x_list_copy = [x for sublist in obj["x_list"] for x in sublist]
#print(len(x_list_copy))
y_list_copy = [y for sublist in obj["y_list"] for y in sublist]
#print(len(y_list_copy))

'''
#how to get data from n,c
print(len(obj["n_list"]))
print(obj["n_list"][0])
for n in obj["n_list"]:
    print("n =", n)

print(len(obj["C_list"]))
print(obj["C_list"][0])
for c in obj["C_list"]:
    print("C =", c)
'''

'''
#print every x for the list
for x in x_list_copy:
    print("x=", float(x))

for y in y_list_copy:
    print("y=", float(y))
'''
print(obj["n_list"][0])
plt.scatter(x_list_copy,y_list_copy, c = 'red')
plt.show()

