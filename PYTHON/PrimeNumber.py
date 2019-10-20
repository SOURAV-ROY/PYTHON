# num = 100
num = int(input("Input The Number: "))

#  Prime Number are Greater Than 1
if num > 1:
    # Check For Factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime Number")
            print(i, "Times", num//i, "is", num)
            break
    else:
        print(num, "Is A Prime Number")
else:
    print(num, "Is's Not A Prime Number => Less  Than 1 OK Guys***")