weight = int(input("Enter Inout: "))
unit = input('(L)bs or (K)g : ')
if unit.upper() =="L":
    converted = weight * 0.45
    print(weight, f"Pound from {converted} Kilos")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(weight, f"Kilo from {converted} Pounds")
else:
    print("Enter Right Value")
