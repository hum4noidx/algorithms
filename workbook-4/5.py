import hashlib
import json

# Define the JSON data
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Parse the JSON data into a Python dictionary
data_dict = json.loads(json_data)

# Create a new empty hash table
hash_table = {}

# Iterate over the keys in the dictionary
for key in data_dict.keys():
    # Compute the hash value of the key using SHA-256 algorithm
    hash_value = hashlib.sha256(key.encode()).hexdigest()

    # Add the key-value pair to the hash table
    hash_table[hash_value] = data_dict[key]

# Print the hash table
print(hash_table)
