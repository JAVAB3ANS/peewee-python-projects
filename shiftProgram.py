# Alphabet variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""

# Receive user input
message = input("Please enter a secret message: ").lower();
key = int(input("Please enter a number to shift by: "))

#  Create a new alphabet that is shifted by the key value
if key == 0:
    newAlphabet = alphabet
    print(newAlphabet)
elif key > 0:
    partialOne = alphabet[:key]
    partialTwo = alphabet[key:]
    newAlphabet = partialTwo + partialOne
    print(newAlphabet)
else:
    partialOne = alphabet[:(26 + key)]
    partialTwo = alphabet[(26 + key):]
    newAlphabet = partialTwo + partialOne
    print(newAlphabet)

# A variable to store the encoded message
newMessage = ""
myMessage = ""

# Loop through and encode the message
for i in range(0, len(myMessage)):
    index = newAlphabet.find(myMessage[i])

    if index < 0:
        newMessage += myMessage[i]
    else:
        newMessage += newAlphabet[index]