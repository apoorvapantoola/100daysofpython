#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:37:34 2018

@author: ApoorvaP
"""

"""
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

"""

freq = {}   # frequency of words in text
line = input("i: ")
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words = sorted(words)

for w in words:
    print("%s:%d" % (w,freq[w]))
    

"""
Question:
    Write a method which can calculate square value of number
"""

def sqr(num):
    return num**2

print(sqr(2))
print(sqr(3))

"""
Question:
    Python has many built-in functions, and if you do not know how to use it, 
    you can read document online or find some books. 
    But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, 
    such as abs(), int(), raw_input()
    And add document for your own function
"""

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def sqr(num):
    """ prints sq of function """
    return num**2

print(sqr.__doc__)

"""
Question:
    Define a class, which have a class parameter and have a same instance parameter.
"""

class Person:
    # defining class parameter
    name = "Person"
    def __init__(self,name=None):
        # self.name is instance parameter 
        self.name=name

jeffery = Person("Jeffery")
print("%s name is %s"%(Person.name,jeffery.name))

pin = Person("pin")
pin.name = "pin"
print("%s name is %s"%(Person.name,pin.name))

"""
Question:
Define a function which can compute the sum of two numbers.
"""

def suum(a,b):
    return int(a+b)

print(suum(5,7))

"""
Question:
Define a function that can convert a integer into a string and print it in console.
"""

def ins(t):
    return str(t)

print(ins(9))

"""
Question:
Define a function that can receive two integral 
numbers in string form and compute their sum and then print it in console.
"""

def sa(a,b):
    print(int(a)+int(b))

sa("3","6")

"""
Question:
Define a function that can accept two strings as input and concatenate them and then print it in console.
"""

def ca(a,b):
    print(a+b)

ca("3","6")    

"""
Question:
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print al l strings line by line.
"""

def acc(a=input("i1: "), b = input("i2: ")):
    len1 = len(a)
    len2 = len(b)
    if(len1>len2):
        print(a)
    elif(len1<len2):
        print(b)
    else:
        print(a)
        print(b)
        
        
acc()

"""
Question:
Define a function that can accept an integer number as input and print the 
"It is an even number" if the number is even, otherwise print "It is an odd number".
"""

def eo(a):
    if(int(a)%2 == 0):
        print("It is an even number")
    else:
        print("It is an odd number")
        
        
eo(4)

"""
Define a function which can print a dictionary where the keys are numbers 
between 1 and 3 (both included) and the values are square of keys.
"""

def di():
    d=dict()
    d[1]=1**2
    d[2]=2**2
    d[3]=3**2
    print(d)
    
di()

"""
Question:
Define a function which can print a dictionary where the keys are numbers 
between 1 and 20 (both included) and the values are square of keys.
"""

def dica():
    d = dict()
    for i in range(1,21):
        d[i]=i**2
        
    print(d)
    
dica()
 