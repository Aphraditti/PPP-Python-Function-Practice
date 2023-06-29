
# #Function Definiton Practice:
# # Define functions according to the following prompts. Write code to then call your functions. Run your code to make sure that each function works.

# #1. A function that accepts no arguments and is named say_hello and returns nothing; it just prints hello.
# def say_hello():
#     print("hello")

# say_hello()

# #2. A sum function that accepts two integers and returns the sum.
# def sum(num1 : int, num2 : int) -> int:
#     return num1+num2

# print(sum(1,2))

# #3. An average function that accepts two numbers and returns the average.
# def average(num1 : int, num2 : int) -> int:
#     return (num1+num2)/2

# print(average(1,2))


# #4. A function that accepts a first name and a last name and formats them to "{last_name}, {first_name}" (returns a string).
# def fullName(firstName:str, lastName:str):
#     return f"{lastName}, {firstName}"

# print (fullName("Raymond", "Wang"))


# #5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.
# def studentInfo(firstName, lastName, gradYear, studentId) -> list:
#     return [firstName, lastName, gradYear, studentId]

# print(studentInfo("Raymond", "Wang", 2018, 123))


# #6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
# def over_18(x):
#     return x > 18

# print(over_18(1))
# print(over_18(19))

# #7. A function that takes a string and prints the string in reverse (no return value).
# def reverseString(string):
#     result = ""
#     for character in string:
#         result = character + result
#     return result 

# print (reverseString("Hello World")

# example #1: 
# test = (1,2,3,4)
# one, *two, four = test 

# print(one)
# print(two)
# print(four)

# example #2: 

# test = [2,3,4]
# print([1,*test])

