# Library Management System

available_books = ["Python", "Java", "C++", "Data Structures", "DBMS"]
issued_books = []

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. View Available Books")
    print("2. Issue a Book")
    print("3. Return a Book")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        if available_books:
            print("\nAvailable Books:")
            for book in available_books:
                print("-", book)
        else:
            print("\nNo books are available.")

    elif choice == 2:
        book = input("Enter the name of the book to issue: ")

        if book in available_books:
            available_books.remove(book)
            issued_books.append(book)
            print(f'"{book}" has been issued successfully.')
        else:
            print("Book is not available.")

    elif choice == 3:
        book = input("Enter the name of the book to return: ")

        if book in issued_books:
            issued_books.remove(book)
            available_books.append(book)
            print(f'"{book}" has been returned successfully.')
        else:
            print("This book was not issued.")

    elif choice == 4:
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")