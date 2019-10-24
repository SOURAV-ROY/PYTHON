customer = {
    "name": "Sourav Roy",
    'age': 25,
    "email": "sourav@gmail.com",
    "is_verified": True
}
customer["name"] = "John Smith"
customer["birthDate"] = "10th June 1996"

print(customer['birthDate'])
# print(customer['Name'])
print(customer.get('name', "John Doe")) # Default Value Set If Not Correct The Key
