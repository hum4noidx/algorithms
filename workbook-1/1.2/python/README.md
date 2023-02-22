# Explanation 
The provided code is a Python implementation of a simple phone book program that allows users to add, find, and delete records using a command-line interface. Here's a brief explanation of the different classes and methods in the code:

### Record class

This class represents a record in the phone book, which consists of a name and one or more phone numbers. The __init__ method initializes a new record with a given name and a list containing the first phone number. The add_phone_number method adds a new phone number to the record.

### TreeNode class

This class represents a node in the binary search tree that is used to store the records in the phone book. Each node contains a Record object and pointers to its left and right child nodes.

### PhoneBook class

This class represents the phone book itself, which is implemented as a binary search tree. The __init__ method initializes an empty phone book with a null root node. The add_record method adds a new record to the phone book by creating a new Record object and inserting it into the binary search tree in the appropriate position. If a record with the same name already exists in the phone book, the add_phone_number method of the existing record is called to add a new phone number to it. The find_record method searches the binary search tree for a record with a given name and returns its phone numbers, if it exists. The delete_record method deletes a record with a given name from the phone book by removing its corresponding node from the binary search tree.

### while loop

This loop runs continuously until the user enters the "quit" command. It prompts the user for a command and then calls the appropriate method of the PhoneBook object based on the user's input. If the user enters an invalid command, an error message is displayed.