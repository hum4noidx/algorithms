def caesar_cipher(message, key):
    """
    Encrypts a message using the Caesar cipher with the specified key.
    :param message: The message to encrypt.
    :param key: The encryption key.
    :return: The encrypted message.
    """
    result = ""

    # Iterate over each character in the message
    for char in message:
        if char.isalpha():
            # Shift the character by the key amount
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + key) % 26 + ord(
                'a' if char.islower() else 'A'))
            result += shifted_char
        else:
            # Just append non-alphabetic characters as is
            result += char

    return result


# Get input from the user
message = input("Enter the message to encrypt: ")
key = int(input("Enter the encryption key: "))

# Encrypt the message
encrypted_message = caesar_cipher(message, key)

print("Encrypted message:", encrypted_message)
print("Decrypted message:", caesar_cipher(encrypted_message, -key))