#author sharath
'''
user defined method
'''
def appendArrayElement(arr,n):
    if (n==0):
        print(arr)
    else:
        element = int(input("enter the element you need to be inserted: "))
        arr.append(element)
        appendArrayElement(arr,n-1)

'''
main method starts here
'''
arr = []
n = int (input ("enter the no o elements to be inserted: "))
appendArrayElement(arr,n)
