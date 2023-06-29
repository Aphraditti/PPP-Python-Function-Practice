def myFunc():
    print("hello")
    print("world")
    def anotherFunc():
        print("hi")
    return 5

myFunc()


# ## Section 1 - variables and functions: 

# # Question 1: Create two variables. One should be a string data type, and the other should be of type int.

# # Use a single print statement to print both variables:

#  x = 'string'
#  y = 1
#     print(x, y)

# # Question 2: Create a Python function that prints a greeting with a name as the parameter.

# # Invoke the function with a name argument of your choosing:

# def printGreeting(name: str) -> str:
#         print(name)

# printGreeting("Aphra")


# ## Section 2 - lists:

# # Question 3: Create a list of your favorite movies with  at least 4 elements:

# movies = ['bridesmaids', 'star wars', 'deuce bigelow', 'something about mary']

# # Question 4: Use a print statement to print the list item at the index of 1:

# print(movies[1])

# # Question 5: Append a movie to the end of your list:


# # Use a print statement to print this ammended list:

# movies += ("highlander")
# print(movies)

# ## Section 3 - dictionaries:

# # Question 6: Create a dictionary named 'cellphone' with 2 key:value pairs that are the properties of your cellphone.
# #The keys should be: "color" and "number".
# #Fill out the values on your own:

# cellphone= {
#     "color": "blue",
#     "num": 12
# }



# # Question 7: Access a value from inside the dictionary (Try to print the value of the 'color' property).

# print(cellphone["color"])


# ## Section 4 - strings:

# # Question 8: Create a variable and store a string with multiple words in it:

# myString = "this is my funny string lol"



# # Question 9: Utilize the method that capitalizes the first letter of each word in your string - store this new string in a new variable:

# newString = myString.title()
# print(newString)


# # Use a print statement to print the new string:





# #Bonus:

# # Question 10: Uncomment and look into this nested dictionary - try to relate your knowledge of objects and arrays in JavaScript.

# students_in_order = {
#   1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
#   2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
#   3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
# }

# # Question 10 A: Write a print function that outputs the second student in the dictionary

# def printSecondStudent(students_in_order):
#     print(students_in_order[2])

# printSecondStudent(students_in_order)


# # Question 10 B: Write a print statement that outputs the name "Zayn" using the dictionary

# print(students_in_order[3]['name'])

# # Question 10 C: Write a print statment that outputs the age of Esteban from the dictionary

# print(students_in_order[1]['age'])



# #Section 1 - sets and tuples:
# #Pre-Question: Take a look at this JavaScript Array:
# # let javaScriptArray = [12, 55, 33, 40, 55, 33, 20, 12]

# # How would you remove duplicates from this JavaScript Array? Take a few minutes to consider what steps are necessary to iterate through this array in JavaScript and remove the duplicates values.

# # What advantages are available when we're working with Python? If this Array was instead a set, we wouldn't be able to store multiple values in it. Uncomment the identical set below and run the print statement. What did you notice in the console return?

# my_set = {12, 55, 33, 40, 55, 33, 20, 12}

# print(my_set)

# #Question 1a: Create a set of your own with at least 3 different elements.
# my_set = {1,2,3}


# #Question 1b: Add an item to the set that you just created.
# my_set.pop()
# print(my_set)

# #Question 1c: Print the set with the new data that you added to it:


# #Question 2a: Create a tuple with at least 3 elements inside of it.
# my_tuple = ("a", "b", "c")
# second_tuple = ("d", "e")


# #Question 2b: Print the tuple you just created.
# print(my_tuple)
# print(my_tuple + second_tuple)



# #Section 2 - loops:

# # days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# # Question 3: Use a for loop to iterate through the 'days' list above and print the days of the week:


# x = 10
# add_list = [10, 6, 12, 4, 5]
# # Question 4: Uncomment the list and variable x above.  Loop through add_list and add each value to x. Print the value of x at each increment:
# for num in add_list:
#     x += num
#     print(x)



# # Question 5: While Loops 

# #Declare an iterator variable (set to the number 1) and write a While loop that adds 5 to the value of the variable starting_value as long as the iterator is under 10:


# iterNum = 1
# starting_value = 5
# while iterNum < 10:
#     starting_value += 5
#     print(starting_value)
#     iterNum += 1




# #Section 3 - conditionals: if, elif, else statements

# favorite_movie = "Madagascar"    
# #Question 6a: Uncomment the favorite_movie variable above and change the value to the title of your favorite movie
# #Below, write a conditional statement that prints the string "that's a great movie" if the favorite_movie variable equals your favorite movie.
# #Otherwise (else), print the string "that's not my favorite movie".  
# #Mess around with the value of the favorite_movie variable and trigger both conditional responses:
# if favorite_movie == "Madagascar":
#     print("that's a great movie")
# else:
#     print("that's not my favorite movie")


# #Question 6b: Uncomment the movie_list variable below and implement a for loop that iterates through each item in the list. 
# #If the item is a blueberry (or another fruit), print "item is a fruit and not movie"; 
# #if the item is a car manufacturing company like Toyota, print "item is a car and not a movie"; 
# #otherwise, just print the movie in the list:

# movie_list = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]
# for movie in movie_list:
#     if movie == "blueberries":
#         print("item is a fruit and not movie")
#     elif movie == "Toyota":
#         print("item is a car and not a movie")
#     else:   
#         print(movie)



# #BONUS - conditional and operators practice:
# a = 5
# b = 5
# c = 12
# #Question 7a: Use the correct operator to add variables a & c:
# print(a+c)


# #Question 7b: Use the correct operator to subtract variables b & c:
# print(b-c)


# #Question 7c: Use the correct comparison operator that shows if variables a & b equal each other:
# print(a==b)


# #Question 7d: Use the correct operator to find the quotient of variables c & a
# print(c/a)


# #Question 7e: Use the correct operator to find if variables c & b are not equal to each other:
# print(c!=b)

# # use the correct operator to find the remainder of c divided by b
# print(c%b)