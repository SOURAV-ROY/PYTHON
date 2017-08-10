'''
Created on Jun 18, 2017

@author: SOURAV
'''
Marks = input("Please enter your marks : ")
Marks = int(Marks)

if Marks >= 80:
    print("Grade = A+")
    print("***Congratulations***")
elif Marks >= 70:
    print("Grade = A")
elif Marks >= 60:
    print("Grade = A-")
elif Marks >= 50:
    print("Grade = B")
elif Marks >= 40:
    print("Grade = B-")
else:
    print("Grade = F ")
    
print("Your Marks Is : ",Marks)