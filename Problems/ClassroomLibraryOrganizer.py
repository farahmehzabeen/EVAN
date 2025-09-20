"""
Problem: "Classroom Library Organizer"
Objective: Create a Python program to help organize a classroom library. The program will track books by their title and
the number of copies available. Your student will learn how to add, update, remove books, and search for books in the
 library.

Requirements:

Set Up the Library: create an empty list called classroom_library.

Adding Books: Write a function named add_book that takes two arguments: the book title (as a string) and the number of
copies (as an integer). This function should add a dictionary { 'title': book_title, 'copies': num_copies } to the
classroom_library list. If the book already exists, increase the number of copies instead of adding a new entry.

Removing Books: Write a function named remove_book that takes the book title as an argument and removes the book from
the library. If there are multiple copies, decrease the number of copies by one. If it's the last copy, remove the book
entirely from the list.

Searching for a Book: Write a function named search_book that searches for a book by its title and returns the number of
copies available. If the book is not found, it should return a message indicating that the book is not available in the
library.

Displaying the Library: Write a function named show_library that prints all the books in the library, each on a new
line, formatted like: "Title: [book_title], Copies: [num_copies]".

User Interaction: Implement a simple text-based menu system that allows the user to add books, remove books, search for
a book by title, and display all books in the library.

Input Validation: Ensure that the number of copies is a positive integer when adding or updating books.

Sample Output:

Welcome to the Classroom Library Organizer!

Choose an option:
1. Add a book
2. Remove a book
3. Search for a book
4. Show all books
5. Exit

Your choice: 1
Enter book title: The Little Prince
Enter number of copies: 3

Your choice: 4
Library Books:
Title: The Little Prince, Copies: 3

Your choice: 2
Enter book title to remove: The Little Prince

Your choice: 4
Library Books:
Title: The Little Prince, Copies: 2

Your choice: 5
Goodbye!
"""

# Initialize the classroom library as an empty list
classroom_library = []


# Function to add or update a book in the library
def add_book(title, copies):
    for book in classroom_library:
        if book['title'] == title:
            book['copies'] += copies
            return
    # If the book doesn't exist, add a new entry
    classroom_library.append({'title': title, 'copies': int(copies)})


# Function to remove a book or decrease its copy count
def remove_book(title):
    for book in classroom_library:
        if book['title'] == title:
            if book['copies'] > 1:
                book['copies'] -= 1
            else:
                classroom_library.remove(book)
            return "Book removed successfully."
    return "Book not found."


# Function to search for a book by title
def search_book(title):
    for book in classroom_library:
        if book['title'] == title:
            return f"Title: {book['title']}, Copies: {book['copies']}"
    return "Book not found in the library."


# Function to display all books in the library
def show_library():
    if classroom_library:
        print("Library Books:")
        for book in classroom_library:
            print(f"Title: {book['title']}, Copies: {book['copies']}")
    else:
        print("The library is currently empty.")


# Main loop for user interaction
while True:
    print("\nWelcome to the Classroom Library Organizer!")
    print("Choose an option:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Show all books")
    print("5. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        copies = int(input("Enter number of copies: "))
        while not 1 <= copies <= 100:
            print("Invalid number of copies.")
            copies = int(input("Enter number of copies: "))
        add_book(title, copies)
        print("Book added successfully.")
    elif choice == "2":
        title = input("Enter book title to remove: ")
        print(remove_book(title))
    elif choice == "3":
        title = input("Enter book title to search: ")
        print(search_book(title))
    elif choice == "4":
        show_library()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
