from tkinter import *
from tkinter import ttk

import functions
import booksapi



class new_book():

    def __init__(self, master):

        self.frame_add_new = ttk.Frame(master)
        master.title('Dodaj nową książkę')

        # Wygląd Adda

        self.frame_add_new.pack()

        ttk.Label(self.frame_add_new, text='Autor:').grid(row=0, column=0, sticky='sw')
        ttk.Label(self.frame_add_new, text='Tytuł:').grid(row=2, column=1, sticky='sw')
        ttk.Label(self.frame_add_new, text='Rozpoczęto:').grid(row=4, column=0, sticky='sw')
        ttk.Label(self.frame_add_new, text='Zakończono:').grid(row=4, column=1, sticky='sw')
        ttk.Label(self.frame_add_new, text='Gatunek:').grid(row=0, column=4, sticky='sw')
        ttk.Label(self.frame_add_new, text='Liczba stron:').grid(row=0, column=5, sticky='sw')
        ttk.Label(self.frame_add_new, text='Recenzja:').grid(row=0, column=6, sticky='sw')
        ttk.Label(self.frame_add_new, text='Streszczenie:').grid(row=0, column=7, sticky='sw')
        ttk.Label(self.frame_add_new, text='Ocena:').grid(row=0, column=8, sticky='sw')


        # self.date_start = ttkcalendar.CalendarDialog(self.frame_add_new)
        self.author = ttk.Entry(self.frame_add_new)
        self.title = ttk.Entry(self.frame_add_new)
        self.pages = ttk.Entry(self.frame_add_new)
        self.genre = ttk.Combobox(self.frame_add_new, values=('To', 'Jest', 'Kurde', 'Dramat'))
        self.rating = ttk.Combobox(self.frame_add_new, values=('1', '2', '3', '4', '5'))

        # self.date_start.grid(row=4, column = 5)
        self.author.grid(row=1, column=0)
        self.title.grid(row=3, column=0)
        self.pages.grid(row=1, column=4)

        self.genre.grid(row=1, column=3)
        self.rating.grid(row=1, column=5)

        self.add_new = ttk.Button(self.frame_add_new, text='Dodaj nową', command= self.dodaj_ksiazke)
        self.add_new.grid(row=10, column=0, sticky='nw')

    def dodaj_ksiazke(self):
        db_con = functions.connection()
        cur = db_con.cursor()

        self.spent = self.date_end - self.date_start

        sql = '''
        INSERT INTO 'BOOKS'('AUTHOR', 'TITLE', 'DATE_START', 'DATE_END', 'PAGES', 'REVIEW', 'SUMMARY', 'SPENT', 'RATING') 
        VALUES('self.author.get()', 'self.title.get()', 'self.date_start.get()', 'self.date_end.get()', 'self.pages.get()',
         'self.review.get()','self.summary.get()', 'self.spent' 'self.rating.get()'        
        '''
        cur.execute(sql)

        for row in cur:
            print('{} {} {} {} {} {} {} {}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        functions.clear()

def main():

    root = Tk()
    add_new = new_book(root)
    root.mainloop()
