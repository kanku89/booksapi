import os


def main():
    auth = input('Podaj nazwisko autora: ')
    tytul = input('Podaj tytuł książki: ')
    page = input('Ilość stron książki: ')

    if tytul and auth != '':
        p = Book(pages=page, title=tytul, author=auth)
        p.new_book()
        p.what()

    else:
        print('Nie wprowadzono tytułu lub autora, zakończono dodawanie książki')


class Book(object):

    def __init__(self, title, author, pages=None):
        self.title = title
        self.author = author
        self.pages = pages

    def what(self):
        print('Dodano książkę:\nAutor: {}\nTytuł: {}\nIlość stron: {}'.format(self.author, self.title, self.pages))

    def new_book(self):
        dirname = os.getcwd()
        filename = 'books.txt'
        filepath = os.path.join(dirname, filename)
        with open(filepath, 'w+') as file:
            file.write(self.title + ',' + self.author + ',' + self.pages)


if __name__ == '__main__':
    main()
