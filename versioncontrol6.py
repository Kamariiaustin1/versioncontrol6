def encode(password):
    encoded_password = ""
    for digit in password:
        # Convert the digit to an integer, add 3, and convert it back to a string
        encoded_digit = str(int(digit) + 3)
        encoded_password += encoded_digit
    return encoded_password

# Decoder function (to be implemented by your partner)
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        # Convert the digit to an integer, subtract 3, and convert it back to a string
        decoded_digit = str(int(digit) - 3)
        decoded_password += decoded_digit
    return decoded_password

# While loop for the main menu program
while True:
    print("Menu")
    print('-------------')
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
# input function to take user selection
    selection = input("Please enter an option: ")

    if selection == '1':
        passcode = input("Please enter your password to encode: ")
        encoded_passcode = encode(passcode)
        print("Your password has been encoded and stored! ")
    elif selection == '2':
        if not encoded_passcode:  # if user doesn't select 1 as their first option they will have no password to decode.
            print("Please code a password. ")
        else:  # if they select 1 they will activate this line of code
            print(f'The encoded password is {encoded_passcode}, and the original password is {(encoded_passcode)}. ')
    elif selection == '3':   # user exits the program by selecting this option
        break
    else:
        print('Please try again.')
