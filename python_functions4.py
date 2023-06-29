
# For each of the functions described below, plan the best way to write the function. Remember that there may be a recursive and an iterative solution to many problems. The best solution to any problem is the solution that you understand best. As long as your function is named correctly, accepts the correct parameters, and returns the correct output, you can be confident that you have succeeded at your task. 

# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

print(max_num(5, 10, 3))  
print(max_num(2, 7, 9))   
print(max_num(-1, 0, 1))  


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(mult_list([2, 3, 4]))      
print(mult_list([-1, 5, -2]))   
print(mult_list([0, 10, 100]))   



# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]

print(rev_string("Hello"))      
print(rev_string("Python"))    
print(rev_string("12345"))     


# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(number, start_range, end_range):
    return start_range <= number <= end_range

print(num_within(3, 2, 4))     
print(num_within(3, 1, 3))     
print(num_within(10, 2, 5))    
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.



# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.