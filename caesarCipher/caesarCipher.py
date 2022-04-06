""""Caesar Cipher message encryption which allows user to enter message, shift, then calls to the function to output finalized secret message!"""

def encrypt (string, shift):
    # will store result of encryption
    encryption = ""

    # traverse length of the string
    for i in range(len(string)): 
        if (string[i].isupper()):  
            # lowercase letters of the string 
            encryption += chr((ord(string[i]) + shift - 64) % 26 + 65)
        else: 
            # keep the same case as they're already lowercase
            encryption += chr((ord(string[i]) + shift - 96) % 26 + 97)
    
    return encryption
 
def main():
    print("Welcome to Caesar Cipher encryption and decryption:\n")
    
    # message = str
    message_input = input("Enter your message: ")
    # shift_input = int
    shift_input = int(input("Enter your shift: "))

    # print if shift_input isn't int and if message_input isn't str
    if not type(shift_input) == int and not type(message_input) == str:
        print("\nPlease enter integer for shift input and/or string for message input")

    print(f"\nPlain text: {message_input}")
    print(f"Shift pattern: {shift_input}")
    print(f"Cipher: {encrypt(message_input, shift_input)}")

if __name__ == "__main__":
    main()