# Define a list of fruits
fruits = ['apple', 'banana', 'orange', 'kiwi']

# Define two separate lists with the same contents as 'fruits'
fruits_copy = ['apple', 'banana', 'orange', 'kiwi']
other_fruits = ['apple', 'banana', 'orange', 'kiwi']

# Check if 'fruits_copy' is the same object as 'fruits'
if fruits_copy is fruits:
    print("fruits_copy is the same object as fruits")
else:
    print("fruits_copy is NOT the same object as fruits")

# Check if 'other_fruits' is equal to 'fruits'
if other_fruits == fruits:
    print("other_fruits is equal to fruits")
else:
    print("other_fruits is NOT equal to fruits")

# Check if 'other_fruits' is the same object as 'fruits'
if other_fruits is fruits:
    print("other_fruits is the same object as fruits")
else:
    print("other_fruits is NOT the same object as fruits")

# Check if 'apple' is in 'fruits'
if 'apple' in fruits:
    print("apple is in fruits")
else:
    print("apple is NOT in fruits")

# Check if 'pear' is in 'fruits'
if 'pear' in fruits:
    print("pear is in fruits")
else:
    print("pear is NOT in fruits")
