favorite_foods = []


def add_favorite_foods(food_name, rating):
    favorite_foods.append((food_name, int(rating)))

def show_favorites():
    print("Favourite Foods:")
    for x, y in favorite_foods:
        print(f"Food: {x}, Rating: {y}")

def find_best_food():
    if favorite_foods:
        return max(favorite_foods, key=lambda item: item[1])[0]
    return "No foods have been added yet"

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
            rating = input("Enter the rating (1-5): ")
            while not rating.isdigit() or not 1 <= int(rating) <= 5:
                print("Invalid Input")
                rating = input("Enter the rating (1-5): ")
            add_favorite_foods(food_name, rating)

    elif choice == "2":
        show_favorites()

    elif choice == "3":
        best_food= find_best_food()
        print(f"The best food is: {best_food}")

    elif choice == "4":
        print("adios")
        break

    else:
        print("Invalid Choice")









