alphabet = "abcdefghijklmnopqrstuvwxyz"
message = input("Enter secret message: ")

def decode(secretMessage):
    
    #Try every key value

    for key in range(len(alphabet)):
        newAlphabet = alphabet[key:] + alphabet[:key]
        attempt = ""

        for i in range(len(secretMessage)):
            index = alphabet.find(secretMessage[i])

            if index < 0:
                attempt += secretMessage[i]
            else:
                attempt += newAlphabet[index]
        print("-"*15)
        print("Key: " + str(key) + " - " + attempt)
        print("-"*15)

        #Call  decode function

decode(message)