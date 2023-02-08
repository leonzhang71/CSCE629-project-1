#examples_of_instances
#first solution for reading the file
#filepath = '../data/test.txt'
#can switch the file name into filepath
#hello
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte


import pickle as pkl
with open("examples_of_instances", 'rb') as f:
    obj = pkl.load(f)
    #this part is to use obj["x_list"][0][0] to pick up the value for data file
    print(obj["x_list"][0][0])



'''
f = open("examples_of_instances", "rb")
print(f.read())
'''