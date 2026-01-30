a_str = "Hello Peasents!"
print(a_str)
print(f"1st character of {a_str} is {a_str[0]}.")
print(f"Last character of {a_str} is {a_str[-1]}.")

# String Slicing, lets me extract a portion of a string or work with only a specific part of it.
# Basic Syntax: string[start:stop]
print(a_str[1:5]) # ello, index 5 excluded.
print(a_str[:5]) # Hello, start index omitted. So, extracts everything from 0.
print(a_str[6:]) # Peasents!, Omitting stop index. So, everything from index 6 to the end is extracted.

# Slicing a string does not modify a string.
# What if omit both strat and end index?
print(a_str[:]) # Hello Peasents!, Prints out everything without slicing anything from the string.

# there's a optional 'step' parameter, which is used to specify the increment between each index in the slice.
# So, if I want only odd numbered index characters from the string.
print("Odd numbered index characters:", a_str[0:len(a_str):2])

# I can reverse a string using the 'step' parameter by setting step to -1, leaving start & stop blank.
print("Reversed string:", a_str[::-1])