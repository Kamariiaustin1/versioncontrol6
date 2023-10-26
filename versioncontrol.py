def encode_password(passcode):  # Activated for menu option 1.... Encodes passcode
    encoded_passcode = ""
    for num in passcode:
        move_num = str((int(num) + 3) % 10)  # each number will be moved up by three digits
        encoded_passcode += move_num
    return encoded_passcode


def decode_password(encoded_passcode):  # Activated for menu option 2....  Decodes passcode
    passcode = ""
    for num in encoded_passcode:
        move_num = str((int(num) - 3) % 10)  # each number will be moved down by three digits
        passcode += move_num
    return passcode

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
        encoded_passcode = encode_password(passcode)
        print("Your password has been encoded and stored! ")
    elif selection == '2':
        if not encoded_passcode:  # if usecator doesn't select 1 as their first option they will have no password to decode.
            print("Please code a password. ")
        else:  # if they select 1 they will activate this line of code
            print(f'The encoded password is {encoded_passcode}, and the original password is {decode_password(encoded_passcode)}. ')
    elif selection == '3':   # user exits the program by selecting this option
        break
    else:
        print('Please try again.')