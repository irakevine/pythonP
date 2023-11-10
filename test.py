# 1. Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

# Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?

# After the loop is done, what's the value of break_num? It is the case that break_num should be a number that is the first number larger than end_num.

# print("hello yuio")
# print("hello cvbnm")

start_num = 5  
end_num = 100 
count_by = 2   



break_num = start_num  
while break_num <= end_num:
   
    print(break_num)

    
    break_num += count_by


# 2. Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.

# Now in addition, address what would happen if someone gives a start_num that is greater than end_num. If this is the case, set result to "Oops!  Looks like your start value is greater than the end value.  Please try again."

# Otherwise, set result to the value of break_num.

start_num = 5  # provide some start number, replace 5 with a number you choose
end_num = 100  # provide some end number that you stop when you hit, replace 100 with a number you choose
count_by = 2   # provide some number to count by, replace 2 with a number you choose


if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
   
    break_num = start_num 
    while break_num <= end_num:
       

       
        break_num += count_by

    
    result = break_num


print(result)




# 3. Write a while loop that finds the largest square number less than an integer limit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

# For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40  
nearest_square = None


num = 1


while num * num <= limit:
    nearest_square = num * num
    num += 1


print("The largest square number less than or equal to", limit, "is", nearest_square)


manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))



# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

# Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs. Press the Run button from the top bar to run the code in a cell.
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

# Write a loop to create the news ticker
for headline in headlines:
    # Calculate the available space for the current headline
    space_remaining = 140 - len(news_ticker)
    
    # Check if there's enough space to add the next headline along with a space
    if space_remaining >= len(headline) + 1:
        # If there's enough space, add the headline and a space to the news ticker
        news_ticker += headline + " "
    else:
        # If there's not enough space, truncate the headline and break the loop
        news_ticker += headline[:space_remaining]
        break

# Ensure the ticker is exactly 140 characters by trimming if needed
news_ticker = news_ticker[:140]

# Print the resulting news ticker
print(news_ticker)

# Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

# For instance, 6 has four factors: 1, 2, 3, 6.

# 1 X 6 = 6

# 2 X 3 = 6

# So we know 6 is not a prime number.

# This practice is not graded. Using the workspace on the Coding Space page, write code to check if the numbers provided in the list check_prime are prime numbers.

# If the numbers are prime, the code should print "[number] is a prime number."
# If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".

# 7 IS a prime number 26 is NOT a prime number, because 2 is a factor of 26

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

# Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points.

# Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
# write your for loop here
# Iterate through the coordinates and labels using zip
for x, y, z, label in zip(x_coord, y_coord, z_coord, labels):
    # Create the string for each point and append it to the points list
    point_str = f"{label}: {x}, {y}, {z}"
    points.append(point_str)

# Print the list of points
print(points)

# Use zip to create a dictionary cast that uses names as keys and heights as values.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

# Create the dictionary using zip
cast = dict(zip(cast_names, cast_heights))

# Print the resulting dictionary
print(cast)

# Unzip the cast tuple into two names and heights tuples.
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# Define names and heights tuples
names = ()
heights = ()

# Unzip the cast tuple
for actor in cast:
    actor_name, actor_height = actor
    names += (actor_name,)
    heights += (actor_height,)

# Print the names and heights tuples
print("Names:", names)
print("Heights:", heights)

# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

# Use the zip function with the * operator to transpose the data
data_transpose = tuple(zip(*data))

# Print the transposed data
for row in data_transpose:
    print(row)

# Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# Create a new list to store the modified cast information
modified_cast = []

# Iterate through the cast list using enumerate
for index, character in enumerate(cast):
    # Append the name followed by the character's height to the modified_cast list
    modified_cast.append(f"{character} {heights[index]}")

# Replace the original cast list with the modified_cast list
cast = modified_cast

# Print the modified cast list
print(cast)

# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# Use a list comprehension to extract and convert first names to lowercase
first_names = [name.split()[0].lower() for name in names]

# Print the resulting list of first names in lowercase
print(first_names)

# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.


# Use a list comprehension to create a list of names passed that only include those that scored at least 65.
scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

# Use a list comprehension to filter names with scores at least 65
passed = [name for name, score in scores.items() if score >= 65]

# Print the list of names of students who passed
print(passed)

def readable_timedelta(days):
    weeks = days // 7
    remaining_days = days % 7

    if weeks == 1:
        week_str = "1 week"
    else:
        week_str = f"{weeks} weeks"

    if remaining_days == 1:
        day_str = "1 day"
    else:
        day_str = f"{remaining_days} days"

    if weeks == 0:
        return f"{day_str}"
    elif remaining_days == 0:
        return f"{week_str}"
    else:
        return f"{week_str} and {day_str}"

# Example usage:
days = 10
result = readable_timedelta(days)
print(result)

# Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values.

def population_density(population, land_area):
    if land_area == 0:
        return "Land area cannot be zero."
    
    density = population / land_area
    return density

# Example usage:
population = 8000000  # Replace with the actual population value
land_area = 1000  # Replace with the actual land area value

density = population_density(population, land_area)
print(f"Population density: {density} people per square unit")


# map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. The code below uses map() to find the mean of each list in numbers to create the list averages. Give it a test run to see what happens.

# Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

# filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True. The code below uses filter() to get the names in cities that are fewer than 10 characters long to create the list short_cities. Give it a test run to see what happens.

# Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter().

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)

# x= 0
# While x < 5:
# print(“Not there yet, x=” + str(x))

# x= x + 1
# print(“x= ” + str (X))

# my_variable= 5
# While my_variable < 10:
# print(“Hello”)
# my_variable +=1
# x= 1 
# sum= 0
# While x < 10:
# Sum += x
# x+ = 1
# Product = 1
# While x<10:
# Product = product * x 
# x+= 1


# months= [‘January’, ‘February’,’March’,’April ’,’septermber’,’october’,’november’,’December’ ]
# print(months[0])
# print(months[1])
# print(months[7])


# def to_celsius(x):
# Return (x-32)*5/9
# For x in range (0,101,10):
# print(x, to _celsius(x))


for n in range(1, 5, 6):  
    print(n)


#     teams = ['Dragons ',',‘Wolves’,’pandas’, ’Unicorns’]
# For home_team in teams:
# For away_team in terms:
# If home_team != away_team:
# print(home_tem + “away-team”)

# greet_friends(“Barry”)

# with open('another_file.txt', 'r') as f:
# file_data = f.read()

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())



#     import time 
# import numpy as np

# X = np.random.random(10000000)

# start= time.time()
# sum(x) / len(x)
# print (time.time()- start)

# start =time.time()
# np.mean(x)
# print(time.time() - start)

# Here is the code demonstrated in the video above:

# Why use NumPy?
# import time
# import numpy as np
# x = np.random.random(100000000)

# # Case 1
# start = time.time()
# sum(x) / len(x)
# print(time.time() - start)

# # Case 2
# start = time.time()
# np.mean(x)
# print(time.time() - start)

## We import NumPy into Python
# import numpy as np

# ## We create a 1D ndarray that contains only integers
# x = np.array([1, 2, 3, 4, 5])

# ## Let's print the ndarray we just created using the print() command
# print('x = ', x)

## 1-D array
x = np.array([1, 2, 3])
x.ndim

## 2-D array
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
Y.ndim

## Here the`zeros()` is an inbuilt function that you'll study on the next page. 
## The tuple (2, 3, 4( passed as an argument represents the shape of the ndarray
y = np.zeros((2, 3, 4))
y.ndim

# Example 1.a - Using a 1-D Array of Integers
## We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])


## We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# Example 1.b - Using 1-D Array of Strings

# ## We create a rank 1 ndarray that only contains strings
# x = np.array(['Hello', 'World'])

# ## We print information about x
# print('x = ', x)
# print('x has dimensions:', x.shape)
# print('x is an object of type:', type(x))
# print('The elements in x are of type:', x.dtype)
x = ['Hello' 'World']
