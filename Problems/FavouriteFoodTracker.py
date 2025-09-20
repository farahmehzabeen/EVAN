"""
Problem: "Favorite Foods Tracker"
Objective: Create a Python program that helps the user keep track of their favorite foods and their ratings.

Requirements:

Create a List: Create an empty list called favorite_foods.

Adding Items: Write a function named add_favorite_food that takes two arguments: the name of the food (as a string) and
its rating (as an integer between 1 and 5). This function should add a tuple (food_name, rating) to the favorite_foods
list.

Displaying the List: Write a function named show_favorites that prints all items in the favorite_foods list, each on a
new line, formatted like: "Food: [food_name], Rating: [rating]".

Finding the Best: Write a function named find_best_food that goes through the favorite_foods list and returns the name
of the food with the highest rating. If there are multiple foods with the same highest rating, return the first one found.

User Interaction: Write a simple loop in the main part of the program that allows the user to add foods and their
ratings. Include an option to display all favorite foods and find the best food.

Input Validation: Ensure that the food rating is an integer between 1 and 5. If the user enters an invalid rating,
prompt them to enter it again.

Sample Output:

Welcome to the Favorite Foods Tracker!

Choose an option:
1. Add a favorite food
2. Show all favorite foods
3. Find the best food
4. Exit

Your choice: 1
Enter food name: Pizza
Enter food rating (1-5): 5

Your choice: 1
Enter food name: Apple Pie
Enter food rating (1-5): 4

Your choice: 2
Favorite Foods:
Food: Pizza, Rating: 5
Food: Apple Pie, Rating: 4

Your choice: 3
The best food is: Pizza

Your choice: 4
Goodbye!
"""

# Initialize the list of favorite foods
favorite_foods = []


# Function to add a favorite food
def add_favorite_food(food_name, rating):
    favorite_foods.append((food_name, int(rating)))


# Function to show all favorite foods
def show_favorites():
    print("Favorite Foods:")
    for food, rating in favorite_foods:
        print(f"Food: {food}, Rating: {rating}")


# Function to find the best food
"""
Check if the favorite_foods list is not empty: The initial if condition checks whether the favorite_foods list contains 
any items. If the list is empty, the function will immediately return the string "No foods have been added yet." This is
 a guard clause that prevents errors that would occur from trying to find a maximum in an empty list.

Finding the Maximum: If the favorite_foods list is not empty, the function uses the max function to find the tuple with 
the highest rating. The max function is a built-in Python function that returns the largest item in an iterable. 
However, since each item in the favorite_foods list is a tuple containing both the name of the food and its rating, 
you need to tell the max function how to determine which item is "larger" (i.e., better) than another.

Key Function: The key parameter of the max function allows you to specify a function that will be called on each element
 in the iterable before making comparisons. In this case, a lambda function is used: lambda item: item[1]. This lambda 
 function takes a single argument (which will be a tuple from the favorite_foods list) and returns the second element 
 of the tuple, which is the rating of the food. By doing this, you're instructing the max function to compare the foods 
 based on their ratings, not the entire tuple.

Return the Name of the Food with the Highest Rating: Once the max function finds the tuple with the highest rating, the 
[0] indexing operation is used to extract just the name of the food (the first element of the tuple) from that tuple. 
This name is then returned by the function.

Result: The end result is that find_best_food will return the name of the food with the highest rating from the 
favorite_foods list. If there are multiple foods with the same highest rating, max will return the first one it 
encounters in the list.
"""


def find_best_food():
    if favorite_foods:
        return max(favorite_foods, key=lambda item: item[1])[0]
    return "No foods have been added yet."


# Main loop for interaction
while True:
    print("\nWelcome to the Favorite Foods Tracker!")
    print("Choose an option:")
    print("1. Add a favorite food")
    print("2. Show all favorite foods")
    print("3. Find the best food")
    print("4. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        food_name = input("Enter food name: ")
        rating = input("Enter food rating (1-5): ")
        while not rating.isdigit() or not 1 <= int(rating) <= 5:
            print("Invalid rating. Please enter a number between 1 and 5.")
            rating = input("Enter food rating (1-5): ")
        add_favorite_food(food_name, rating)
    elif choice == "2":
        show_favorites()
    elif choice == "3":
        best_food = find_best_food()
        print(f"The best food is: {best_food}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
