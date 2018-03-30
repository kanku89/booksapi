from tkinter import *
from tkinter import ttk

import functions
import booksapi



class new_book():

    def __init__(self, master):

        self.frame_add_new = ttk.Frame(inicjacja.frame_search)
        master.title('Dodaj nową książkę')

        # Wygląd Adda

        self.frame_add_new.pack()

        ttk.Label(self.frame_add_new, text='Autor:').grid(row=0, column=0, sticky='sw')
        ttk.Label(self.frame_add_new, text='Tytuł:').grid(row=2, column=0, sticky='sw')
        ttk.Label(self.frame_add_new, text='Rozpoczęto:').grid(row=4, column=0, sticky='sw')
        ttk.Label(self.frame_add_new, text='Zakończono:').grid(row=4, column=1, sticky='sw')
        ttk.Label(self.frame_add_new, text='Gatunek:').grid(row=4, column=2, sticky='sw')
        ttk.Label(self.frame_add_new, text='Liczba stron:').grid(row=4, column=3, sticky='sw')
        ttk.Label(self.frame_add_new, text='Recenzja:').grid(row=6, column=0, sticky='sw')
        ttk.Label(self.frame_add_new, text='Streszczenie:').grid(row=8, column=0, sticky='sw')
        ttk.Label(self.frame_add_new, text='Ocena:').grid(row=4, column=4, sticky='sw')


        # self.date_start = ttkcalendar.CalendarDialog(self.frame_add_new)
        self.author = ttk.Entry(self.frame_add_new)
        self.title = ttk.Entry(self.frame_add_new)
        self.pages = ttk.Entry(self.frame_add_new)
        self.genre = ttk.Combobox(self.frame_add_new, values=('To', 'Jest', 'Kurde', 'Dramat'))
        self.rating = ttk.Combobox(self.frame_add_new, values=('1', '2', '3', '4', '5'))

        # self.date_start.grid(row=4, column = 5)
        self.author.grid(row=1, column=0)
        self.title.grid(row=3, column=0)
        self.pages.grid(row=5, column=3)

        self.genre.grid(row=5, column=2)
        self.rating.grid(row=5, column=4)

        self.add_new = ttk.Button(self.frame_add_new, text='Dodaj nową', command= self.dodaj_ksiazke)
        self.add_new.grid(row=10, column=0, sticky='nw')

    def dodaj_ksiazke(self):
        # db_con = functions.connection()
        # cur = db_con.cursor()
        #
        # self.spent = self.date_end - self.date_start
        #
        # sql = '''
        # INSERT INTO 'BOOKS'('AUTHOR', 'TITLE', 'DATE_START', 'DATE_END', 'PAGES', 'REVIEW', 'SUMMARY', 'SPENT', 'RATING')
        # VALUES('self.author.get()', 'self.title.get()', 'self.date_start.get()', 'self.date_end.get()', 'self.pages.get()',
        #  'self.review.get()','self.summary.get()', 'self.spent' 'self.rating.get()'
        # '''
        # cur.execute(sql)

        self.frame_add_new.destroy()



def main():

    root = Tk()
    add_new_book = new_book(root)
    root.mainloop()
