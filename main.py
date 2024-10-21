import webbrowser 

class Books: #create books class
    def __init__(self, title, author, genre, pages,link):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.purcheses = 0
        self.read = False
        self.owned = False
        self.link = link

# book options
b1 = Books("The President's Daughter", "Nan Britton", "Thriller", 439,"https://www.gutenberg.org/cache/epub/74595/pg74595-images.html")
b2 = Books("The baseball boys of Lakeport", "Edward Stratemeyer", "Sports", 315,"https://www.gutenberg.org/cache/epub/74593/pg74593-images.html")
b3 = Books("The boys of Columbia High on the ice", "Grahm B Forbes", "Sports", 272,"https://www.gutenberg.org/cache/epub/74588/pg74588-images.html")

#create lists
availableList = [b1, b2, b3]
purchasedList = []
readList = []

#update lists after user actions
def updateLists(avail, purch, read):
    purch.clear()
    read.clear()
    for book in avail:
        if book.owned:
            purch.append(book)
            if book.read:
                read.append(book)

def description(book):
    print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre} Pages: {book.pages}")

#marks books as read
def mark_as_read(book):
    book.read = True
    print(f"You have finished reading {book.title}.")

#main user interaction menu
def mainMenu(available, purchased, read):
    while True:
        print("\nUSER MENU (input the number to select an option)")
        print("1. Display books available")
        print("2. Display books purchased")
        print("3. Display books read")
        print("4. EXIT")
        inp = input("Choose an option: ")

        if inp == "1":#if input is available books
            for i, book in enumerate(available):
                print(f"{i + 1}. {book.title}")
            availMenu(available)
            updateLists(available, purchased, read)

        elif inp == "2": #if input is purchased books
            if len(purchased) >= 1:
                print("\nPurchased Books:")
                for i, book in enumerate(purchased):
                    description(book)
                purchMenu(purchased)
                updateLists(available, purchased, read)
            else:
                print("No books purchased")

        elif inp == "3": #if input is read books
            if len(read) >= 1:
                print("\nBooks Read:")
                for book in read:
                    description(book)
                readMenu(readList)
                updateLists(available, purchased, read)
            else:
                print("No books read")

        elif inp == "4": #exit application
            break

def availMenu(avail): #menu if available is chosen
    inp = input("Choose a Book (number): ")
    try:
        selected_index = int(inp) - 1
        if 0 <= selected_index < len(avail):
            print(f"Would you like to purchase {avail[selected_index].title}?")
            print("1. Yes")
            print("2. No")
            inp2 = input()
            if inp2 == "1":
                avail[selected_index].owned = True
                updateLists(availableList, purchasedList, readList)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def purchMenu(purch): #menu if purchased is chosen
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
            elif inp2 == "3":
                print("Returning to Menu")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

mainMenu(availableList, purchasedList, readList)
