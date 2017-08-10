'''
Created on Jul 3, 2017

@author: SOURAV
'''
year = input("Enter Year : ")
year = int(year)
 
# if year % 4 !=0:
#     print("No 1111")
# else:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Yes 1111")
#         else:
#             print("No 2222")
#     else:
#             print("Yes 2222")

# if year % 400 ==0:
#     print("Yes 11")
# elif year % 100 == 0:
#     print("No 11")
# elif year % 4 ==0:
#     print("Yes 22")
# else:
#     print("No 22")

if year % 100 != 0 and year % 4 == 0:
    print(year, "Is Leap Year 1")
elif year % 100 ==0 and year % 400 == 0:
    print(year,"Is Leap Year 2")
else:
    print(year,"Is not Leap Year")
