"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv) # returns ['03_modules.py']
print(sys.argv[0]) # returns 03_modules.py

# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform) 
#returns darwin
# Print out the version of Python you're using:
# YOUR CODE HERE

# A string containing the version number of the Python interpreter plus additional information on the build number and compiler used
print(sys.version)
# returns 3.8.3 (default, May 27 2020, 20:54:22) 
# [Clang 11.0.3 (clang-1103.0.32.59)]

# A tuple containing the five components of the version number:
print(sys.version_info) # major=3, minor=8, micro=3, releaselevel='final', serial=0

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getegid())
# returns 20


# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
# returns /Users/carlitosredding/Documents/GitHub/Python/Lambda-Python/Intro-Python/Python-Intro/src

# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())
# returns carlitosredding