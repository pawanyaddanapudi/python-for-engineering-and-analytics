
# Functions: UDF, Lambda
def orskl_func(input):
    print("Passed in value is " + input)


orskl_func("OrSkl Python Intro")
orskl_func("Self Learning Tracks")

a = [1, 2, 3, 4, 5]
f = lambda x: x * x
[f(x) for x in a]

# Comprehensions: List, Dict
number_list = [x ** 2 for x in range(10) if x % 2 == 0]
my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]

dict_ob = {'a':15, 'b': 12, 'A': 8, 'Z':7}
dict_ob_comp = { k.lower() : dict_ob.get(k.lower(), 0) + dict_ob.get(k.upper(), 0) for k in dict_ob.keys() }


# Classes
class test():
    orskl = 1

obj = test
obj.orskl

# Inheritance
class parent():
    orskl_1 = 10

class child(parent):
    pass

obj = child()
obj.orskl_1

# Local & Global variables
del a
def orskl_fun():
    a = 2

orskl_fun()
a

def orskl_fun():
    global a
    a = 2

orskl_fun()
a

# Dates
import datetime

x = datetime.datetime.now()
print(x)

# Regular expressions
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
x

# Handling Files
f = open("../Track 2 | Python Intro/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("../Track 2 | Python Intro/demofile2.txt", "r")
print(f.read())
