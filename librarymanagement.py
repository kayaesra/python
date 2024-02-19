class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0) 
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            print("Book: {}, Author: {}".format(book_info[0], book_info[1]))

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        release_year = input("Enter first release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = "{},{},{},{}\n".format(title, author, release_year, num_pages)
        self.file.write(book_info)
        self.file.seek(0) 

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        lines = self.file.read().splitlines()

        new_lines = [line for line in lines if title_to_remove not in line]

        self.file.seek(0)
        self.file.truncate()
        self.file.write('\n'.join(new_lines))


lib = Library()

while True:

    print("\n*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book")
    choice = input("Enter your choice between 1-3 : ")

    if choice == 1:
        lib.list_books()

    elif choice == 2:
        lib.add_book()

    elif choice == 3:
        lib.remove_book()
    else:
        break
