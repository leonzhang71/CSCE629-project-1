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

#O(n^2) to find all element in one list
i = 0
j = 0
for i in range (len(obj["x_list"])):
    for j in range (len(obj["x_list"][i])):
        print("x=", float(obj["x_list"][i][j]))

#how to get data from n,c
print(len(obj["n_list"]))
print(obj["n_list"][0])
for n in obj["n_list"]:
    print("n =", n)

print(len(obj["C_list"]))
print(obj["C_list"][0])
for c in obj["C_list"]:
    print("C =", c)
    
#print every x for the list
for x in x_list_copy:
    print("x=", float(x))

for y in y_list_copy:
    print("y=", float(y))

#entire plot
#plt.scatter(x_list_copy,y_list_copy, c = 'red')
#plt.show()

#first x y set
#x = obj["x_list"][0]
#y = obj["y_list"][0]
#plt.scatter(x, y, c = 'red')
#plt.show()
'''


import pickle as pkl
import  matplotlib.pyplot as plt

with open("examples_of_instances", 'rb') as f:
    obj = pkl.load(f)

#list for x,y
x_list_copy = [x for sublist in obj["x_list"] for x in sublist]
#print(len(x_list_copy))
y_list_copy = [y for sublist in obj["y_list"] for y in sublist]
#print(len(y_list_copy))


def summationX(x,n):
    totalX = 0
    for i in range (n):
        totalX = totalX + x[i]
    return totalX

def summationX2(x,n):
    totalX2 = 0
    for i in range (n):
        totalX2 = totalX2 + x[i]**2
    return totalX2

def summationY(y,n):
    totalY  = 0
    for i in range (n):
        totalY  = totalY + y[i]
    return totalY

def summationXY(x,y,n):
    totalXY = 0
    xy = 0
    for i in range (n):
        xy = x[i] * y[i]
        totalXY = totalXY + xy
    return totalXY

def functionA(x,y,n):
    sumX = summationX(x,n)
    sumY = summationY(y,n)
    sumXY = summationXY(x,y,n)
    sumX2 = summationX2(x,n)
    valueA = (n*(sumXY) - sumX*sumY)/(n*(sumX2)-(sumX)**2)
    return valueA

def functionB(x,y,n):
    sumX = summationX(x,n)
    sumY = summationY(y,n)
    valueB = (sumX - sumY)/n
    return valueB

def errorL(x,y,n):
    sumX = summationX(x,n)
    sumY = summationY(y,n)
    valueA = functionA(x,y,n)
    valueB = functionB(x,y,n)

    errorValue = (sumY - valueA*sumX - valueB)

    return errorValue

    n2 = 2
    n3 = 3
    n4 = 4
    n5 = 5
    n6 = 6 
    resulterrorbest = errorL(x_list_copy,y_list_copy,nbest)
    print("best fit =", resulterrorbest)
    resulterror2 = errorL(x_list_copy,y_list_copy,n2)
    print("n is 2 =", resulterror2)
    resulterror3 = errorL(x_list_copy,y_list_copy,n3)
    print("n is 3 =", resulterror3)
    resulterror4 = errorL(x_list_copy,y_list_copy,n4)
    print("n is 4 =", resulterror4)
    resulterror5 = errorL(x_list_copy,y_list_copy,n5)
    print("n is 5 =", resulterror5)
    resulterror6 = errorL(x_list_copy,y_list_copy,n6)
    print("n is 6 =", resulterror6)

def main():
    i = 2
    n = 94
    nbest = 31
    kline = 0

    for i in range (n):
        try: 
            Evalue = errorL(x_list_copy,y_list_copy,i)
            print("n =", i, " ,error value=",Evalue)
        except ZeroDivisionError:
            print("Warning: division by zero at i =", i)

    
    for i in range (n):
        partition_list = []
        try:
            if errorL(x_list_copy,y_list_copy,i) > errorL(x_list_copy,y_list_copy,i+1):
                partition_list.append(i)
                kline = kline + 1
                print("line =", kline, ",end point =" ,i)
        except ZeroDivisionError:
            print("Warning: division by zero at i =", i)







if __name__ == "__main__":
    main()