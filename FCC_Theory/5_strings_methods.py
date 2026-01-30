# Python has a number of built-in methods that make working with strings a breeze.

# Original String
a_str = "    hello World    "
print(f"Original String: {a_str}")

# upper()
print(f"Uppercase: {a_str.upper()}")

# lower()
print(f"Lowercase: {a_str.lower()}")

# strip() = returns a new string with the specified leading or trailing characters removed.
# If no argument is passed it removes leading and trailing whitespace.
print(f"Whitespace Stripped: {a_str.strip()}")

# replace(old, new) = returns a new string with all occurrences of old replaced by new.
print(f"Replaced string: {a_str.replace('hello', 'Hi')}")

# split(separator) = Splits a string on a specified separator into a list of strings.
# If no separator is specified, it splits on whitespace.
print(f"Split words: {a_str.split()}")

# join(iterable) = Joins elements of an iterable into a string with a separator.
a_str = a_str.split()
print(f"Joined sting: {' '.join(a_str)}")
a_str = " ".join(a_str)
# print(a_str)

# startswith(prefix) = Returns a boolean indicating if a string starts with the specified prefix.
print(f"Is the string starts with 'hello'? {a_str.startswith('hello')}")

# endswith(suffix) = Returns a boolean indicating if a string ends with the specified suffix
print(f"Is the string ends with 'world'? {a_str.endswith('world')}") # False because 'hello World'

# find(substring) = Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
print(f"The index of the first occurrence of 'World': {a_str.find('World')}")
print(f"The index of the first occurrence of 'hero': {a_str.find('hero')}")

# count(substring) = Returns the number of times a substring appears in a string.
print(f"The number of times letter 'l' appears in '{a_str}': {a_str.count('l')}")

# capitalize()
print(f"Capitalized: {a_str.capitalize()}")

# isupper() = Returns True if all letters in the string are uppercase and False if not.
print(f"Is all letters Uppercase? {a_str.isupper()}")

# islower() = Returns True if all letters in the string are lowercase and False if not.
print(f"Is all letters lowercase? {a_str.islower()}")

# title() = Returns a new string with the first letter of each word capitalized.
print(f"Title case: {a_str.title()}")