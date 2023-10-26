# Encoder function
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

# Main function
def main():
    while True:
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter the 8-digit password: ")
            encoded_password = encode(password)
            print("Encoded password:", encoded_password)
        elif choice == "2":
            encoded_password = input("Enter the encoded password: ")
            original_password = decode(encoded_password)
            print("Decoded password:", original_password)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()