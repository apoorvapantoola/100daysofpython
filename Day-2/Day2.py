#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:52:17 2018

@author: ApoorvaP
"""

"""
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""

inp = input("In: ").split(',')
dim = [int(x) for x in inp]

row = dim[0]
col = dim[1]

mulist = [[0 for coll in range(col)] for roww in range(row)]

for roww in range(row):
    for coll in range(col):
        mulist[roww][coll] = roww*coll

print(mulist)

"""
Write a program that accepts a comma separated sequence of words as input and prints 
the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""
inp = input("In: ").split(',')
inp.sort()
print(','.join(inp))

"""
Write a program that accepts sequence of lines as input and 
prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""
lines = []
while True:
   sen = input("In: ")
   if sen:
       lines.append(sen.upper())
   else:
       break;
       
for sent in lines:
    print(sent)
    
    
"""
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""

sen = input("IN: ").split()
print("Out: ")
print(" ".join(sorted(list(set(sen)))))


"""
Question:
Write a program which accepts a sequence of comma separated 4 digit binary 
numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""

inp = input("In: ").split(',')
val = []

for x in inp:
    xp = int(x,2)
    print(xp)
    if not xp%5:
        val.append(x)
print(",".join(val))

"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

val = []
for x in range(1000,3001):
    s = str(x)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        val.append(s)

print(",".join(val))

"""
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""

sen = input("In: ")
dic = {"DIGITS":0,"LETTERS":0}
for x in sen:
    if x.isdigit():
        dic["DIGITS"] += 1
    elif x.isalpha():
        dic["LETTERS"] += 1
    else:
        pass
print("LETTERS : ",dic["LETTERS"])
print("DIGITS : ",dic["DIGITS"])

"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

sen = input("In: ")
dic = {"UPPER CASE":0,"LOWER CASE":0}

for x in sen:
    if x.isupper():
        dic["UPPER CASE"] += 1
    elif x.islower():
        dic["LOWER CASE"] += 1
    else:
        pass

print("UPPER CASE : ",dic["UPPER CASE"])
print("LOWER CASE : ",dic["LOWER CASE"])  
        
