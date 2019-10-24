numbers = [10, 2, 3, 3, 4, 4, 5, 7]
# numbers.append(30)
# numbers.insert(1, 10)
# numbers.remove(5)
# numbers.clear()
# numbers.pop()
# print(numbers.index(4))
# print(50 in numbers)  # False***********************
# print(numbers.count(4))
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# numbers.append(50)
# print(numbers)
# print(numbers2)

# REMOVE DUPLICATE ITEMS ***********************
uniqueList = []
# sourav = "Sourav"
for number in numbers:
    if number not in uniqueList:
        uniqueList.append(number)
# print("Array List: ", uniqueList, numbers)
print(F"Array List :> {uniqueList}")
