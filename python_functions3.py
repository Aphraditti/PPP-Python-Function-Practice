# In this activity we are going to practice writing functions in Python. The prompts have been listed below. Work may be completed using a personal Replit or a local code editor. Be sure to retain access to your completed work so it can be checked by instructors.   

# Please complete the following functions.

# 1. name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(**kwargs):
    for kwarg in kwargs:
        print(kwarg)

name_args(a=10,b=20,c=30)

# OR

def name_args(**kwargs):
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

name_args(a=10,b=20,c=30)

# 2.  all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
def isTrue(kwarg):
    return kwarg == True


def name_args(**kwargs):
    return all(kwargs.values())

print(name_args(a=True, b=True, c=True))


# 3. one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
def one_true(**kwargs):
    return any(kwargs.values())


print(one_true(a=False, b=False, c=False))

# print(one_true(a=False, b=False, c=False))
# recursive_factorial - Uses recursion to find the factorial of an integer.
# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
# Input: AABBCCDD
# Output: ABCD
# recursive_reverse - Uses recursion to reverse a string.

