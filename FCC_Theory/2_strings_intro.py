# A string is a sequence of characters surrounded by either single or double quotation marks. 

# A single line string 
a_str = "Hello"
print(a_str, type(a_str))

# A multi-line string, I must use a triple double or single quotes 
a_multiline_str = """'This is a
Multiline 
String'"""
print(a_multiline_str, type(a_multiline_str))

# Using the escape character backslash (\) 
quote = "She said, \"Hello, my dear!\""
print(quote)

# To check if a string contains one or more characters. Using 'in' operator. It returns boolean. 
greeting = "Hello Humans!"
print('Hello' in greeting) #True
print('hey' in greeting) #False
print('Hell' in greeting) #True
print("H" in greeting) #True
print('Hum' in greeting) #True

# Using built-in function called len(), to get the length of a string for indexing purposes.
a_quote = "A Custom Made Reality, Only for Yourself!"
print(a_quote, ":", len(a_quote), "characters long!")

# Each character in a string has a position called an index. The index of the forst character is always '0'. 
# I must use [] with the index of the character I want to access inside.
greeting = "Hello Pests!"
print(greeting[0], '- 1st letter of greeting variable.') # H
print(greeting[6], '- 7th letter of greeting variable.') # P

# Negative indexing, starts from -1, -2,...
print(greeting[-1], '- last letter of greeting variable.')
print(greeting[-2], '- 2nd last letter of greeting variable.')

# Strings are immutable data types in Python. This means I can assign a different string to a variable.
greeting = 'hello'
greeting = 'hi'
print(greeting)

# Direct modification of a string isn't allowed.
greeting = 'hello'
# greeting[0] = 'H' # replacing only the first character. It gives TypeError.
# Other immutable data types in Python are: int, float, boolean, tuple and range.