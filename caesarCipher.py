""""Caesar Cipher message encryption which allows user to enter message, shift, then calls to the function to output finalized secret message!"""


def encrypt ( string, shift ):
    # will store result of encryption
    encryption = " "

    # loop through the length of the string
    for i in len(string):
        if (string[i].lower()): 
        # first check if it is in lowercase and convert accordingly
        # using ascii keys converts string to appropriate caesar cipher
            encryption += str(int(string[i] + shift - 97) % 26 + 97)
        else:
        # same thing but for uppercase
            encryption += str(int(string[i] + shift - 97) % 26 + 65)
    
    return encryption


print("Welcome to Caesar Cipher encyprtion and decryption: ")
shift_input = input("Enter your shift: ")
message_input = input("Enter your message: ")

print(encrypt ( shift_input, message_input))