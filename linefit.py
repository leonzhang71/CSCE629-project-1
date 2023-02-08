#examples_of_instances
#first solution for reading the file
#filepath = '../data/test.txt'
#can switch the file name into filepath
#hello
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte


import pickle as pkl
with open("examples_of_instances", 'rb') as f:
    obj = pkl.load(f)

    #that line print all list and data set
    #print(obj)
    
    #that line print special 'list' with full data set
    #print(obj["x_list"])

    #that line print the len() special data set in that list
    #print (len(obj["x_list"][1]))

    #this part is to use obj["x_list"][0][0] to pick up the value for data file
    #print(obj["x_list"][0][0])

print(len(obj["x_list"][0]))

#print(obj["x_list"][0])

#using loop to find and print every element for obj["x_list"][0])
i = 0
for i in range (len(obj["x_list"][0])):
    print(float(obj["x_list"][0][i]))




