#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 15:00:17 2018

@author: ApoorvaP
"""

"""
Question1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

n = []
for i in range(2000,3200):
    if((i%7)==0) and ((i%5)!=0):
        n.append(str(i))

print(','.join(n))

"""
Question2:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
def facto(a):
    if(a==0):
        return 1
    else:
        return a * facto(a-1)

b = int(input("IN:"))
print(facto(b))

"""
Question3:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
#sol1
def dicti(n):
    dic = {}
    for i in range(1,n+1):
        dic[i] = i*i
    return dic

b = int(input("IN:"))
print(dicti(b))

#sol2
n=int(input("IN:"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
    
print(d)

"""
Question4:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

num = input("num: ").split(',')
print(num)
print(tuple(num))

"""
Question5:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""
class inoutstr(object):
    def __int__(self):
        self.s = ""
        
    def getString(self):
        self.s = input("Str: ")
        
    def printString(self):
        print(self.s.upper())

strbj = inoutstr()
strbj.getString()
strbj.printString()

"""
Question6:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
import math
C = 50
H = 30
val = []
items = [x for x in input("num: ").split(',')]
for D in items:
    val.append(str(int(round(math.sqrt((2 * C * float(D))/H)))))

print(','.join(val))


        
