"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
# w for write, r for read, a for appending any data written.
# YOUR CODE HERE
foo = open('foo.txt', 'r')
print(foo.read())
# print(foo.read(500))
# print(foo.readlines())

foo.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open('bar.txt', 'w')
a = ['Hello \n', 'I love you \n', 'tell me your name \n']
bar.writelines(a)
bar.close()

bar = open('bar.txt', 'r')
print(bar.read())
# print(bar.readlines())
bar.close()
# 
'''
Do you bite your thumb at us, sir?
I do bite my thumb, sir.
Do you bite your thumb at us, sir?
No, sir. I do not bite my thumb at you, sir, but I bite my thumb, sir.
Do you quarrel, sir?
Quarrel, sir? No, sir.
'''