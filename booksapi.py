from tkinter import *
from tkinter import ttk
import sqlite3


class Search():


    def __init__(self, master):

        self.frame_search = ttk.Frame(master)
        master.title('Books API')

#Wygląd searcha

        self.frame_search.pack()

        ttk.Label(self.frame_search, text= 'Autor:').grid(row = 0, column = 0, sticky = 'sw')
        ttk.Label(self.frame_search, text= 'Tytuł:').grid(row = 0, column = 1, sticky = 'sw')
        ttk.Label(self.frame_search, text= 'Zakres dat:').grid(row = 0, column = 2, sticky = 'sw')
        ttk.Label(self.frame_search, text= 'Gatunek:').grid(row = 0, column = 3, sticky = 'sw')
        ttk.Label(self.frame_search, text= 'Ocena:').grid(row = 0, column = 4, sticky = 'sw')

        self.author = ttk.Entry(self.frame_search)
        self.title = ttk.Entry(self.frame_search)
        self.genre = ttk.Combobox(self.frame_search, values = ('To', 'Jest', 'Kurde', 'Dramat'))
        self.rating = ttk.Combobox(self.frame_search, values = ('1', '2', '3', '4', '5'))

        self.author.grid(row = 1, column = 0)
        self.title.grid(row= 1, column=1)

        self.genre.grid(row= 1, column=3)
        self.rating.grid(row=1, column=4)

        self.search = ttk.Button(self.frame_search, text='Szukaj')
        self.add_new = ttk.Button(self.frame_search, text='Dodaj nową')
        self.add_new.grid(row=3, column =0, sticky = 'nw')
        self.search.grid(row=2, column = 0, sticky = 'nw')

 #   def pokaz_dane(self):
  #      (self.author.get())



#funkcja czyszczenia

    def clear(self):
        self.author.delete(0, 'end')
        self.title.delete(0, 'end')

    def db_search(self):
        db = sqlite3.connect()

        cur = db.cursor()
        cur.execute()


#Wygląd wyników wyszukiwania

        #self.frame_show = ttk.Frame(master)


  #  def conditions(self):





def main():

    root = Tk()
    search = Search(root)
    root.mainloop()


if __name__ == '__main__': main()