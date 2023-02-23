# Whitespacing Formatting
for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
print("done looping")

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

#Modules
import re #working with regex
import re as regex
my_regex = regex.compile("[0 - 9]+", regex.I)

#Functions
def double(x):
    return x * 2

def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double) #2

y = apply_to_one(lambda x: x + 4)
another_double = lambda x : 2 * x #shouldn't

def my_print(message = "hello"):
    print(message)

my_print("hi") #hi
my_print() #hello

def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last
full_name("Joel", "Grus") # "Joel Grus"
full_name("Joel") # "Joel Something"
full_name(last="Grus") # "What's-his-name Grus"

#Strings
