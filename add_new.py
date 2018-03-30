from tkinter import *
from tkinter import ttk
from tkinter import ttkcalendar
import functions
import booksapi



class new_book():

    def __init__(self, master):

        self.frame_add_new = ttk.Frame(master)
        master.title('Dodaj nową książkę')

        # Wygląd Adda

        self.frame_add_new.pack()

        ttk.Label(self.frame_add_new, text='Autor:').grid(row=0, column=0, sticky='sw')
        ttk.Label(self.frame_add_new, text='Tytuł:').grid(row=0, column=1, sticky='sw')
        ttk.Label(self.frame_add_new, text='Rozpoczęto:').grid(row=0, column=2, sticky='sw')
        ttk.Label(self.frame_add_new, text='Zakończono:').grid(row=0, column=2, sticky='sw')
        ttk.Label(self.frame_add_new, text='Gatunek:').grid(row=0, column=3, sticky='sw')
        ttk.Label(self.frame_add_new, text='Liczba stron:').grid(row=0, column=4, sticky='sw')
        ttk.Label(self.frame_add_new, text='Recenzja:').grid(row=0, column=4, sticky='sw')
        ttk.Label(self.frame_add_new, text='Streszczenie:').grid(row=0, column=4, sticky='sw')
        ttk.Label(self.frame_add_new, text='Ocena:').grid(row=0, column=5, sticky='sw')

        self.date_start = ttkcalendar.CalendarDialog(self.frame_add_new)
        self.author = ttk.Entry(self.frame_add_new)
        self.title = ttk.Entry(self.frame_add_new)
        self.pages = ttk.Entry(self.frame_add_new)
        self.genre = ttk.Combobox(self.frame_add_new, values=('To', 'Jest', 'Kurde', 'Dramat'))
        self.rating = ttk.Combobox(self.frame_add_new, values=('1', '2', '3', '4', '5'))

        self.date_start.grid(row=4, column = 5)
        self.author.grid(row=1, column=0)
        self.title.grid(row=1, column=1)
        self.pages.grid(row=1, column=4)

        self.genre.grid(row=1, column=3)
        self.rating.grid(row=1, column=5)

        self.add_new = ttk.Button(self.frame_add_new, text='Dodaj nową', command=self.pokaz_dane)
        self.add_new.grid(row=3, column=0, sticky='nw')
        self.search.grid(row=2, column=0, sticky='nw')

