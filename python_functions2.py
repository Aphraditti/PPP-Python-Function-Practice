
# In this activity we are going to practice writing functions in Python. 

# Please complete the following functions.


# 1.  arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*numbers):
    for number in numbers: 
        print(number)

arb_args(1, 2, 3, 4, 5)


# 2. inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(x, y):
    def inner1():
        return x + y
    
    def inner2():
        return x * y
    
    print(inner1() + inner2())
inner_func(1,2)


# 3. lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)

lunch_lady("Raymond")
lunch_lady("Raymond", "Filet Mignon")

# 4. sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(x, y):
    return x + y, x * y

print(sum_n_product(1,2))


# 5. alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
def alias_arb_args(alias, *number):
    alias(number)
alias_arb_args(arb_args, 1, 2)


# 6. arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*integer):
    length = 0
    numerator = 0
    for num in integer:
        numerator += num
        length += 1
    return numerator / length

print(arb_mean(3,5,6))




# 7. arb_longest_string - Accepts any number of strings and returns the longest one.
def longest_string(*args):
    long=0
    longest=""
    for arg in args:
        if len(arg)>long:
            long=len(arg)
            longest=arg
    return longest
    
print(longest_string("a", "abc", "ab"))


