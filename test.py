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


for headline in headlines:
  
    if len(news_ticker) + len(headline) + 1 <= 140:
       
        news_ticker += headline + " "
    else:
        
        characters_remaining = 140 - len(news_ticker) - 1
        news_ticker += headline[:characters_remaining]
        break


print(news_ticker)
