#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:48:13 2018

@author: ApoorvaP
"""

"""
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

a = input("In: ")
n1 = int("%s" %a)
n2 = int("%s%s"%(a,a))
n3 = int("%s%s%s"%(a,a,a))
n4 = int("%s%s%s%s"%(a,a,a,a))

summ = n1+n2+n3+n4

print(summ)

"""
Question:
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""

in1 = input("In: ").split(',')
in2 = [x for x in in1 if int(x)%2!=0] # list Comprehension
print(",".join(in2))

"""
Question:
Write a program that computes the net amount of a bank account based a transaction 
log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
""""
netamt = 0
while True:
    inp = input("In: ")
    if not inp:
        break;
    val = inp.split(" ")
    typ = val[0]
    amt = int(val[1])
    if typ == "D":
        netamt += amt
    elif typ== "W":
        netamt-=amt
    else:
        pass
    
print(netamt)

"""
Question:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""

import re
val = []
items = [x for x in input("In: ").split(',')]
for p in items: 
    if(len(p)<6 or len(p)> 12):
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    val.append(p)
    
print(",".join(val))

"""
Question:
You are required to write a program to sort the (name, age, height) tuples by 
ascending order where name is string, age and height are numbers. 
The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""

from operator import itemgetter

l = []
while True:
    s = input("In: ")
    if not s:
        break;
    l.append(tuple(s.split(",")))
    
print(sorted(l,key=itemgetter(0,1,2)))


"""
Question:
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.
"""
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in putNumbers(100):
    print(i)
    
    
"""
Question
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. 
Please write a program to compute the distance from current position after a 
sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""
import math

pos = [0,0]

while True:
    s = input("In: ")
    if not s:
        break
    move = s.split(" ")
    direction = move[0]
    step = int(move[1])
    
    if direction=="UP":
        pos[1]+=step
    elif direction=="DOWN":
        pos[1]-=step
    elif direction=="LEFT":
        pos[0]-=step
    elif direction == "RIGHT":
        pos[0]+=step
    else:
        pass
    
print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
    
                    

