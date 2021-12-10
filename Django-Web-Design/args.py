def mine(*args): #use any name, just include *
    count = 0
    for x in args:
        count += x
    return print(count)

def my_arg(*names): # *value is always a tuple, not a list.
    for name in names:
        print(f"Hello, {name}.")

mine(1, 4, 10, 304)
my_arg('John', 7, "Jason")

# **kwargs works just like *args, but instead of accepting positional
# arguments it accepts keyword (or named) arguments
def kw(**kwargs):
    value = ""
    for arg in kwargs.values():
        value += arg + " "
    return print(value)

kw(first="John", middle="David", last="Howell")

# Here, the * operator tells print() to unpack the list first.
my_list = [1, 2, 3, 4, 5]
print(*my_list)

def my_sum(a, b, c, d, e):
    print(a + b + c)

my_sum(*my_list)

def my_mult(*args):
    result = 1
    for x in args:
        result *= x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_mult(*list1, *list2, *list3))

#  say you need to split a list into three different parts.
# extract_list_body.py
a, *b, c = my_list
print(f"a: {a}, b: {b}, c: {c}")

# split the items of any iterable object
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)

# merge two different dictionaries by using the unpacking operator **:
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

# unpack a string:

# string_to_list.py
a = [*"RealPython"]
print(a)
*a, = "RealPython" # another way to write it.
print(a)
