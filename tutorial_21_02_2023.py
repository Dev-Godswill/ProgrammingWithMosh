# For loop

# for item in ['Mosh', 'James', 'John']: # you use [] to define a list 
#   print (item)

# for item in range(5,10,2):
#   print (item)

# Program to calculate the total cost of all the items in a shopping cart
# prices = [10, 20, 30]

# since this is a for loop, we have to define a variable that would store our price value with an initial value set to 0, so that variable runs through the list

# total_cost = 0
# for price in prices:
#   total_cost += price # this is adding 0 to all values in prices 0+10, 0+20, 0+30
# print (f"Total: {total_cost}")

# # Nested Loop
# for x in range (4):
#   print (x)
#   # for y in range (3):
#   #   print (f"({x}, {y})")

# # Program to print shape of numbers
# numbers = [2, 1, 1, 4]

# for x_count in numbers:
#   # print ('x' * x_count) # shortcut version
#   output = ''
#   for count in range (x_count):
#     output += 'x'
#   print (output) 

# # List
# largest_number = [30, 3, 5, 6, 10, 20, 50, 2]
# print (max(largest_number))

# # 2D List
# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# for row in matrix:
#   for item in row:
#     print (item)

# # List Methods
# numbers = [0, 1, 2, 3, 4, 5]
# numbers.insert(3, 30)
# print(numbers)

# Program to remove duplicates in a list
numbers = [9, 9, 10, 9, 0, 1, 2, 3, 4]
uniques = []

for number in numbers:
  if number not in uniques:
    uniques.append(number)
print(uniques)