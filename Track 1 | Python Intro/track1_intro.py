# Which version of Python are you in?
# - From your terminal :
# - Pawans-MacBook-Pro:~ pawanyaddanapudi$ python3 --version
# - Python 3.7.6
# - Run in this console
import sys
sys.version

# Print
print(sys.version)

# Get into Python shell
# - Through terminal: Execute the version command above
# - Run using PyCharm

# How to run code in Python - Through PyCharm "Run" - Runs the complete code in the current file: Demo - Through
# PyCharm selection - Runs only the selected code in the current file: Demo as above - Through terminal - Runs the
# complete code in the file - pawanyaddanapudi@Pawans-MacBook-Pro python-for-engineering-and-analytics % python3
# ./Track\ 1\ \|\ Python\ Intro/track1_intro.py

# Modules and import them
import sys
sys.version

# sys is module which we are importing into the current python session.
# There are many modules which comes by default with python3 installation.

# Check modules location & Other modules
print('.\n'.join(sys.path))
# We will see much more in detail in later tracks on the same

# Install modules
# - from Pycharm: Demo
# - from terminal: pip3 install pandas
import pandas


# Variables
a = 1
print(a)
a = "OrSkl"
print(a)
print("This is Track 1 session")
del a
print(a)

# Data Types : Numbers, Strings, Float, Booleans
a = 1
print(type(a))
a = "OrSkl"
print(type(a))
a = True  # Remember its case sensitive.
print(type(a))
a = 0.87977
print(type(a))

# Data structures: Lists, Tuples, Sets, Dictionaries
a = [1, 2, 3, 4]
print(a[0])
print(type(a))
a = ["OrSkl", "Consulting", "Services"]
print(type(a))
print(a[1])
a = (1, 2, 3, 4)
print(a[0])
print(type(a))
a = {1, 2, 3, 4}
print(a[0])
print(type(a))
a = {1, 2, 3, 4, 4}
print(a)
print(type(a))
a = [1, 2, 3, 4, 4]
print(a)
print(type(a))
a = {"name": "Orskl", "place": "Hyderabad"}
print(type(a))
print(a["name"])
print(a["place"])


# Indentations
# Loops: If...Else, While, For
a = True

if a is True:
    print("a is True")
    print("Testing Indentation")
    print("Test successful")
else:
    print("a is False")

a = 0
while a < 5:
    print(a)
    a += 1

a = [0, 1, 2, 3, 4]
for a in range(0, 5):
    print(a)

