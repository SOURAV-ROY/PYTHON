message = input(" > ")
# words = message.split(" ")
words = message.split(' ')
emoji = {
    ":)": "😊",
    ":(": "😥"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)
