from datetime import date
import sys

# Type and print
print("hello")
name= "my name is Faizan"
a1=100
print(a1)
print(type(a1))

# operators
total=0
apple=5
bannana=6
oranges=5
total=bannana+oranges
print(total)
if oranges == bannana: total=0

print(total)

# Python tokens
#if else keywrods

s1='''multiline
 test is working'''

print(s1)

hs= name[0:4]
print(hs)


# find string middle
list = [4, 6, 7, 8, 9, 10]

def middle_remover(lst,s,e):
    middle = lst[:s] + lst[e+1:] 
    return middle

print(middle_remover(list,2,3))

for i in list:
    print(i)

def GetdateToday():
    return date.today()

print(GetdateToday())