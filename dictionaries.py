# dictionaries : {key: value}
# dictionaries : {"bug" : An error in a program that prevent the program from running expected}

programming_dictionary = {
    "bug" : "An error in a program that prevent the program from running expected",
    "function" : "A piece of code that you can easily call over and over again",
    "loop" : "The action of doing something over and over again"}


# Adding key & value in dictionary
programming_dictionary["programming"] = "The process or activity of writing computer programs."



#how to retrieve value from dictionary
print(programming_dictionary)
print(programming_dictionary["bug"])

# Printing Keys and Values Separately
print("Keys:", list(programming_dictionary.keys()))
print("Values:", list(programming_dictionary.values()))

# Printing key-value pairs as tuples
print("Key-Value Pairs:", list(programming_dictionary.items()))

# Printing with a loop
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Printing a dictionary using a loop and the items() method
for key, value in programming_dictionary.items():
    print(key, ":", value)

# Printing a dictionary using a loop and the keys() method
for key in programming_dictionary.keys():
    print(key, ":", programming_dictionary)

# Printing a dictionary using f-strings
for key, value in programming_dictionary.items():
    print(f"{key.capitalize()} has the definition {value}.")

# Printing a dictionary using the format() method
for key, value in programming_dictionary.items():
    print("{} has the definition {}.".format(key.capitalize(), value))

