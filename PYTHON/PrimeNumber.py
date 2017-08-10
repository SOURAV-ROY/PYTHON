'''
Created on Jun 25, 2017
****************************************** PRINT WITHOUT PRIME NUMBERS
@author: SOURAV
'''
for x in range(2,101):
    isprime ="no"
#     print(x)
    for i in range(2,x):
        if x%i ==0:
            print(x)
            isprime="yes"
            break
            if isprime=="no":
                print(x)