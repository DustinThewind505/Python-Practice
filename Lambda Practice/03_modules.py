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
print(sys.argv)
for arg in sys.argv:
    print(f'\n{arg}\n')

# Print out the OS platform you're using:
# YOUR CODE HERE
print(f'{sys.platform}\n')

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(f'\n{os.getpid()}\n')

# Print the current working directory (cwd):
# YOUR CODE HERE
print(f'{os.getcwd()}\n')

# Print out your machine's login name
# YOUR CODE HERE
print(f'{os.getlogin()}\n')
