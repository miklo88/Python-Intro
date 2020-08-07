"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the print operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('print()')
print('x is', x)
print('y is', y)
print('z is', z)
# Use the 'format' string method to print the same thing
print(format('format()'))
print('x is', format(x))
print('y is', format(y))
print('z is', format(z))
# Finally, print the same thing using an f-string
print(f'f-strings')
print(f'x is', x)
print(f'y is', y)
print(f'z is', z)