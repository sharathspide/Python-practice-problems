#ggggggggggarararararggggggggggararararargggggggggg

userInput = input("Enter the string of DNA sequence: ")

#print (userInput[:len(userInput):])
subStr=[]
count = 0
for i in range (0,len(userInput)):
    if (len(userInput[i:i+10])== 10):
        subStr.append(userInput[i:i+10])

print (subStr)
setSubStr = {}
for i in range(0,len(subStr)):
    for j in range(i+1,len(subStr)):
        if (subStr[i]==subStr[j]):
            count = count+1
            #print ("i: ",i)
            #print ("j: ",j)
    #print (count)
    if (count >= 1):
        print (subStr[i])
        count = 0
