# Integer = A whole number without decimals 
my_int = 10
print("Integer:", my_int)

# Float = A number with a decimal point.
my_float = 6.90
print("Float:", my_float)

# String = A sequence of characters enclosed in a single or double quotation marks.
my_string = "My Love!"
print("String:", my_string)

# Boolean = A true or false type.
my_boolean = True
print("Boolean:", my_boolean)

# Set = An unordered collection of unique elements enclosed in curley bracket {}
my_set = {7, 5, 8}
print("Set:", my_set)

# Dictionary = A collection of key-value pairs enclosed in curly braces {}
my_dictionary = {'name': 'Riyaz', 'age': 31}
print("Dictionary:", my_dictionary)

# Tuple = An immutable ordered collection enclosed in brackets ()
my_tuple = (7, 5, 8)
print("Tuple:", my_tuple)

# Range = A sequence of numbers, often used in loops
my_range = range(5)
print("Range:", my_range)

# List = An ordered collection of elements that supports different data types.
my_list = [22, 'Hello', 3.14, True]
print("List:", my_list)

# None = A special value that represents the absence of a value 
my_none = None
print("None:", my_none)

print("\n")

# To get the data type of a variable, I can use the type() function 
print("The data type of variables I have used above:")

print("Integer:", type(my_int))
print("FLoat", type(my_float))
print("String:", type(my_string))
print("Boolean:", type(my_boolean))
print("Set:", type(my_set))
print("Dictionary:", type(my_dictionary))
print("Tuple:", type(my_tuple))
print("Range:", type(my_range))
print("List:", type(my_list))
print("None:", type(my_none))

print("\n")

# The built-in "isinstance()" function, which lets me check if a variable matches a specific data type. 
print("Using the isinstance() function:")
print("Is 'Hello' a string?", isinstance('Hello', str))
print("Is 'True' a boolean?", isinstance(True, bool))
print("Is 'John' a integer?", isinstance('John', int))