import webbrowser 

class Books:  # Create books class
    def __init__(self, title, author, genre, pages, link):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.purchases = 0  # Track the number of purchases
        self.read = False
        self.owned = False
        self.link = link

# Book options
b1 = Books("The President's Daughter", "Nan Britton", "Thriller", 439, "https://www.gutenberg.org/cache/epub/74595/pg74595-images.html")
b2 = Books("The Baseball Boys of Lakeport", "Edward Stratemeyer", "Sports", 315, "https://www.gutenberg.org/cache/epub/74593/pg74593-images.html")
b3 = Books("The Boys of Columbia High on the Ice", "Grahm B Forbes", "Sports", 272, "https://www.gutenberg.org/cache/epub/74588/pg74588-images.html")

# Create lists
availableList = [b1, b2, b3]
purchasedList = []
readList = []
genreList = ["Thriller", "Sports"]

# Update lists after user actions
def updateLists(avail, purch, read):
    purch.clear()
    read.clear()
    for book in avail:
        if book.owned:
            purch.append(book)
            if book.read:
                read.append(book)

def description(book):
    print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Pages: {book.pages}, Purchases: {book.purchases}")

# Marks books as read
def mark_as_read(book):
    book.read = True
    print(f"You have finished reading {book.title}.")

# Main user interaction menu
def mainMenu(available, purchased, read):
    while True:
        print("\nUSER MENU (input the number to select an option)")
        print("1. Find a book")
        print("2. Display books purchased")
        print("3. Display books read")
        print("4. EXIT")
        inp = input("Choose an option: ")

        if inp == "1":
            print("1. Search by genre")
            print("2. Top Sellers")
            print("3. Search by title")
            print("4. Search by author")
            availMenu(available)
            updateLists(available, purchased, read)

        elif inp == "2":
            if len(purchased) >= 1:
                print("\nPurchased Books:")
                for book in purchased:
                    description(book)
                purchMenu(purchased)
                updateLists(available, purchased, read)
            else:
                print("No books purchased")

        elif inp == "3":
            if len(read) >= 1:
                print("\nBooks Read:")
                for book in read:
                    description(book)
                readMenu(read)
                updateLists(available, purchased, read)
            else:
                print("No books read")

        elif inp == "4":
            break

def availMenu(avail):
    inp = input()
    try:
        selected_index = int(inp) - 1
        if 0 <= selected_index < len(avail):
            if inp == "1":
                genreSelection(genreList)
            elif inp == "2":
                topSellers(avail)
            elif inp == "3":
                searchByTitle(avail)
            elif inp == "4":
                searchByAuthor(avail)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def genreSelection(genrelist):
    for i in range(len(genrelist)):
        print(f"{i + 1}. {genrelist[i]}")
    inp = input("Choose a genre (number): ")
    selected_index = int(inp) - 1
    if 0 <= selected_index < len(genrelist):
        print(f"Books in {genrelist[selected_index]}:")
        for book in availableList:
            if book.genre == genrelist[selected_index]:
                print(f"{book.title} by {book.author}")
        purchasePrompt(availableList)
    else:
        print("Invalid genre selection.")

def topSellers(available):
    # Sort books by number of purchases in descending order
    sorted_books = sorted(available, key=lambda x: x.purchases, reverse=True)
    print("Top Sellers:")
    for book in sorted_books:
        description(book)
    purchasePrompt(sorted_books)

def searchByTitle(available):
    title = input("Enter the title to search: ").lower()
    found_books = [book for book in available if title in book.title.lower()]
    if found_books:
        for book in found_books:
            description(book)
        purchasePrompt(found_books)
    else:
        print("No books found with that title.")

def searchByAuthor(available):
    author = input("Enter the author's name to search: ").lower()
    found_books = [book for book in available if author in book.author.lower()]
    if found_books:
        for book in found_books:
            description(book)
        purchasePrompt(found_books)
    else:
        print("No books found by that author.")

def purchasePrompt(bookList):
    while True:
        inp = input("Would you like to purchase a book? (yes/no): ")
        if inp.lower() == "yes":
            for i, book in enumerate(bookList):
                print(f"{i + 1}. {book.title}")
            inp = input("Choose a book to purchase (number), or 'back' to return: ")
            if inp.lower() == 'back':
                return  # Return to the previous menu
            try:
                selected_index = int(inp) - 1
                if 0 <= selected_index < len(bookList):
                    bookList[selected_index].owned = True
                    bookList[selected_index].purchases += 1  # Increment the purchases count
                    print(f"You have purchased {bookList[selected_index].title}.")
                    updateLists(availableList, purchasedList, readList)
                    return  # Exit the purchase prompt
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
        elif inp.lower() == "no":
            return  # Exit the purchase prompt
        else:
            print("Please enter 'yes' or 'no'.")

def purchMenu(purch):
    inp = input("Choose a Book (number): ")
    try:
        selected_index = int(inp) - 1
        if 0 <= selected_index < len(purch):
            print("1. Mark as read")
            print("2. Open book")
            print("3. Back to menu")
            inp2 = input("Choose an option: ")
            if inp2 == "1":
                mark_as_read(purch[selected_index])
            elif inp2 == "2":
                print(f"Opening {purch[selected_index].title}...")
                webbrowser.open_new(purch[selected_index].link)
            elif inp2 == "3":
                print("Returning to Menu")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def readMenu(read):
    inp = input("Choose a Book (number): ")
    try:
        selected_index = int(inp) - 1
        if 0 <= selected_index < len(read):
            print("1. Read book again")
            print("2. Mark as unread")
            print("3. Back to menu")
            inp2 = input("Choose an option: ")
            if inp2 == "1":
                print(f"Opening {read[selected_index].title}...")
                webbrowser.open_new(read[selected_index].link)
            elif inp2 == "2":
                read[selected_index].read = False
                print(f"You have marked {read[selected_index].title} as unread.")
            elif inp2 == "3":
                print("Returning to Menu")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

mainMenu(availableList, purchasedList, readList)
