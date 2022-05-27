# Author = "Sharath",

# program 1
'''
Write a Python program to create an array of 5
integers and display the array items.
Access individual element through indexes
'''
'''
def arrayInt(n):
    ary = []
    for i in range(1,n+1,2):
        ary.append(i)
    print (ary)
    print ("Access first three items individually")
    for i in range (0,3):
        print (ary[i])
    print ("*+*+*+*+*+*+*+*+*+*+*+*")
    ary2 = [ary[i] for i in range (0,3)]
    print (ary2)
    print(ary[i] for i in range(0,3)) #cannot directly print forloop
        

print ("start")
userInput = int(input("enter the length of the array: " ))
arrayInt(userInput)
'''

#program 2
'''
Write a Python program to append a new item to the end
of the array.
'''
'''
def arrayAppend(a,n):
    a.append(n)
    print (a)
    return a

a = []
#n = int(input("enter the no to be inserted: "))
loop = int(input("enter the no of time the loop to be executed: "))

for i in range(0,loop):
    n = int(input("enter the no to be inserted: "))
    a = arrayAppend(a,n)
'''
    
