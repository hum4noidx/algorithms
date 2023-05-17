
# Define the plaintext and the substitution cipher
plaintext = "This is a secret message."
substitution = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
    'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
    'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
    'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
    'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b',
    'z': 'a', ' ': ' '
}

# Encrypt the plaintext
ciphertext = ""
for char in plaintext:
    if char.lower() in substitution:
        ciphertext += substitution[char.lower()]
    else:
        ciphertext += char

# Print the encrypted text
print("The encrypted text is:", ciphertext)