#'''Noelle Bauer  Python OOP Basics'''

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, book):
        if book in self.books:
            print('Error: {} is already in the list.'.format(book))
        else:
            self.books.append(book)

    def __str__(self):
        book_list = ', '.join(self.books) or 'Nor published books'
        return 'the author, {}, has published the following books: {}'.format(self.name, book_list)

def main():
    author_one = Author('Author Name')
    author_one.publish('First Book')
    author_one.publish('Second Book')
    author_one.publish('Third Book')

    print(author_one)

    author_one.publish('Forth Book')

main()