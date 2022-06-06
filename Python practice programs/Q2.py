'''
def logic (a,b,k):
    res = a
    if (k == 1):
        res = a&b  
        '''
'''
        for i in range(1,k+1):
            if (i%2 != 0):
                res = res & b
            else:
                res = b
                '''
'''
    else:
        res = b
    return res       


test = int(input())#"enter the no of test cases: "

for i in range (0,test):
    a = int(input())#"enter the value for a: "
    b = int(input())#"enter the value for b: "
    k = int(input())#"enter the value for k: "
    res = logic(a,b,k)
    print (res)
'''


'''
a = 5
b = 4
c = 3
d = 2

print(b and a and c and d) # print_stat1 t or f
print(c | b | a | d) # print_stat2 grt no
'''

dic = {}

dic ["name"] =["jimmi" , "summi", input()] 
dic ["marks"] = ["50", "10", "89"]
print (dic.items())





                
