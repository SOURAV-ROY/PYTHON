'''
Created on Jul 14, 2017

@author: SOURAV
'''
# result = 0
# for n in range(50):
#     result = result + 1
#     print(result)1
from builtins import int

# result = 0
# num = 1
# for n in range(50):
#     result = result + num
#     num = num + 1
#     print(result)

# result = 0
# for num in range (5):
#     result = result + num
#     print(result)

num = input("Enter the number : ")
num = int(num)
result = 0
for num in range(1, num+1):
    result += num
    print("All Fibonacci Numbers By Series =>", result)
