# Define the input string of integers
input_string = "86, 90, 27, 29, 38, 30, 40"

# Split the string into a list of integers
input_list = [int(x) for x in input_string.split(", ")]

# Initialize the hash table as an array of size 7
hash_table = [None] * 7


# Define the hashing function as remainder division by 7
def hash_function(x):
    return x % 7


# Iterate through the input list and insert each integer into the hash table
for x in input_list:
    index = hash_function(x)
    if hash_table[index] is None:
        hash_table[index] = x
    else:
        # Collision handling - linear probing
        while hash_table[index] is not None:
            index = (index + 1) % 7
        hash_table[index] = x

# Print the resulting hash table
print(hash_table)
