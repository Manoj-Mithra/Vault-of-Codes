"""
Secret Code Generator (Caesar Cipher Encoder / Decoder)
Author: Penugonda Manoj Mithra
Email: penugondamanojmithra@gmail.com
Internship: VaultofCodes.in - Python Programming

Description:
A cryptographic Python utility that implements the classic Caesar Cipher
algorithm to encode and decode messages with a customizable numeric shift key.
Maintains letter casing and preserves whitespace and special characters.
"""

# -------------------- FUNCTIONS --------------------

def encode(message, shift):
    """Encodes the given message by shifting letters forward by 'shift'."""
    result = ""
    for char in message:
        if char.isalpha():  # Process only letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces/punctuation unchanged
    return result


def decode(message, shift):
    """Decodes the given message by shifting letters backward by 'shift'."""
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


def menu():
    """Displays menu and handles user input."""
    while True:
        print("\n=== Secret Code Generator ===")
        print("1. Encode a Message")
        print("2. Decode a Message")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            msg = input("Enter the message to encode: ")
            try:
                shift = int(input("Enter shift value (e.g., 2): "))
                encoded = encode(msg, shift)
                print(f"\nEncoded Message: {encoded}\n")
            except ValueError:
                print("Invalid shift value. Please enter a number.")

        elif choice == '2':
            msg = input("Enter the message to decode: ")
            try:
                shift = int(input("Enter shift value (e.g., 2): "))
                decoded = decode(msg, shift)
                print(f"\nDecoded Message: {decoded}\n")
            except ValueError:
                print("Invalid shift value. Please enter a number.")

        elif choice == '3':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# -------------------- MAIN PROGRAM --------------------
if __name__ == "__main__":
    menu()
