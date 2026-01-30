# In Python, I can combine multiple strings together witht he plus(+) operator. This process is called 'string concatenation'.
str_1 = 'Hello'
str_2 = 'World'
complete_str = str_1 + ' ' + str_2
print(complete_str)

# NOTE: This only works with strings. If I concatenate a string with a number, I'll get 'TypeError'.
name = 'Riyaz'
age = 32
# print(name + age) #TypeError
# To fix this, I can convert the int into a str using str() built-in function.
print(name + str(age)) # Riyaz32

# The process of inserting variables and expressions into a string is called 'string interpolation'.
# Using f-strings (formating string literals), which used to handle interpolation with a compact and readable stntax.
print(f"My name is {name} and I am {age} years old!")

num1 = 10
num2 = 20
print(f"The sum of {num1} and {num2} is {num1 + num2}.")

# Here, I don't need to convert non-string types with the str() function.
# The value of the int variables are converted under the hood into a string during the interpolation process.
