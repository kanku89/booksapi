import pyodbc
import booksapi

def connection():
    con = pyodbc.connect("DRIVER={MySQL ODBC 5.3 Unicode Driver};SERVER=de2.fcomet.com;PORT=3306;"
                         "DATABASE=yugenpin_booksapi;UID=yugenpin_bookapp;PASSWORD=Booksapi@123;")
    return con

