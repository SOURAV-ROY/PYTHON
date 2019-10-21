weight = int(input("Enter Inout: "))
unit = input('(L)bs or (K)g : ')
if unit.upper() =="L":
    converted = weight * 0.45
    print(f"You are {converted} Kilos")
elif unit.upper() == "K":
    converted = weight // 0.45
    print(f"You Are {converted} Pounds")
else:
    print("Enter Right Value")
