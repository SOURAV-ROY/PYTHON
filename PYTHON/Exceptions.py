try:
    age = int(input("Age :"))
    income = 10000
    risk = income/age
    print(f"Age = {age} & Income = {risk}")

except ZeroDivisionError:
    print("Age Can Not Be Zero")
except ValueError:
    print("Invalid value")
