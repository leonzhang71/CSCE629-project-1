#examples_of_instances
#first solution for reading the file
#filepath = '../data/test.txt'
#can switch the file name into filepath
#hello

import pickle as pkl
with open("examples_of_instances", 'rb') as f:
    obj = pkl.load(f)
    print(obj)
