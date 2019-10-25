phone = input("Phone :")
digits_mapping = {
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
}
# output = []
output = ""
for cn in phone:
    output += digits_mapping.get(cn, "!") + " "  # Added Space By "+" Sign Not Use "," ****** OK
print(output)
