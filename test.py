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