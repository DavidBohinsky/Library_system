import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import messagebox

#///////////////////////////////////////////////////////////////////////////////////
###################             Vytvorenie DATABAZY           ######################
#///////////////////////////////////////////////////////////////////////////////////

connection = sqlite3.connect("moja_data.db")
cursor = connection.cursor()

# NOOO JE TREBA UROBIT TABULKU ZAKAZNICI NA NOVO KDE BUDE PRIMARY KEY ID_ZAK
# V DRUHEJ TABULKE KNIHY BUDE ID KNIHY PRIMAREY KEY, FOREIGN KEY (ID KNIHY) REFERENCES ZAKAZNICI (ID_ZAK)

# vytvorenie tabulky zakaznikov
#cursor.execute('''CREATE TABLE IF NOT EXISTS zakaznici (
#    Id INT PRIMARY KEY,
#    First_Name VARCHAR(50),
#    Last_Name VARCHAR(50),
#    Contact VARCHAR(30),
#    PIN_CODE INT  );        ''')

#cursor.execute('ALTER TABLE zakaznici ADD COLUMN Credit FLOAT(10)')
#connection.commit()

#cursor.execute("DROP TABLE IF EXISTS knizky ")          # vymaz tabulky

# vlozenie zakaznikov do tabulky zakaznici
#zakaznici = [
#    (1, 'Dávid', 'Bohinsky', 'david@aaa.com', 1234),
#    (2, 'Janka', 'Milá', 'janka@mila.com', 5257),
#    (3, 'Alica', 'Krátka', 'alica@zoznam.com', 9541),
#    (4, 'Ondrej', 'Mikla', 'ondrej@azet.sk', 1486)]

#cursor.executemany("INSERT INTO zakaznici (Id, First_Name, Last_Name, Contact, PIN_CODE) VALUES (?, ?, ?, ?, ?)", zakaznici)



cursor.execute("UPDATE zakaznici SET Credit = 40 WHERE Id = 4")
connection.commit()
#cursor.execute('''CREATE TABLE IF NOT EXISTS knizky (
#    bookID INT PRIMARY KEY,
#    title VARCHAR(100),
#    authors VARCHAR(50),
#   rating FLOAT,
#   num_pages INT,
#   ratings_count INT,
#   FOREIGN KEY(bookID) REFERENCES zakaznici(Id) )     ''')

#data = pd.read_csv('books_v_cvs.csv')
#knizky = 'knizky'

#data.to_sql(knizky, connection, if_exists='replace', index=False)


#cursor.execute('''CREATE TABLE IF NOT EXISTS zakaznik (
#   CUS ID INT PRIMARY KEY,
#   Credit IN,
#   PIN_CODE (INT), )    ''')

#connection.commit()

class zakaznik:
    def __int__(self, Id, Credit, PIN_CODE, Rented_books):
        self.Id = Id
        self.Credit = Credit
        self.PIN_CODE = PIN_CODE
        self.Rented_books = Rented_books




# vypis z tabulky
"""data = cursor.execute('''SELECT * FROM zakaznici''')
connection.commit()
for row in data:
   print(row)
   
vypis = cursor.fetchall()
print(vypis)
"""

#///////////////////////////////////////////////////////////////////////////////////
###################             Program         ####################################
#///////////////////////////////////////////////////////////////////////////////////


okno = tk.Tk()
okno.title("Knižný systém")

okno.geometry("250x200")

overenie_pin = tk.StringVar()
pin_kody = tk.StringVar()

#zakaz = tk.StringVar()




# Tlacidla
vloz_pin_popis = tk.Label(okno, text = "Vlož PIN: ")
vloz_pin_popis.place(x=20)

def Vstup():
    global riadok
    #cursor.execute('SELECT PIN_CODE FROM zakaznici WHERE PIN_CODE=?', [overenie_pin])
    #riadok = cursor.fetchall()

    if riadok:
        messagebox.showinfo("", "Úspešné prihlásenie")
        Hlavne_menu()
    else:
        messagebox.showinfo("", "Neúspešné prihlásenie")



vstup_tl = tk.Button(okno, width= 20, text = "Potvrď", command= Vstup)
#vstup_tl.bind("<Return>", Vstup)
okno.bind('<Return>',lambda event:Vstup())
vstup_tl.place(y=30, x=30)

pin_zak = tk.Entry(okno, width= 20, textvariable= overenie_pin)
pin_zak.place(x=80)

overenie_pin = pin_zak.get()

cursor.execute('SELECT PIN_CODE FROM zakaznici WHERE PIN_CODE=?', [overenie_pin])
connection.commit()
riadok = cursor.fetchone()

#///////////////////////////////////////////////////////////////////////////////////
###################             Hlavne menu         ################################
#///////////////////////////////////////////////////////////////////////////////////


def Kredit():
    global riadok

    kredit = tk.Tk()
    kredit.title("Kredit")
    kredit.geometry("250x250")
    #overenie_pin = pin_zak.get()
    #cursor.connection('SELECT Credit FROM zakaznici WHERE PIN_CODE=?', [overenie_pin.get()] )
    print(riadok[4])



    stav_kred_lbl = tk.Label(kredit, text="Stav kreditu: " )
    stav_kred_lbl.pack()

    dobit_btn = tk.Button(kredit, text="Dobitie kreditu")
    dobit_btn.pack()

    

def Hlavne_menu():
    global riadok
    okno.destroy()
    menu = tk.Tk()
    menu.title("Hlavne menu")
    menu.geometry("250x250")


    cursor.execute('SELECT First_Name FROM zakaznici WHERE PIN_CODE=?', [overenie_pin.get()])
    zak = cursor.fetchone()

    if zak:
        vitaj_lbl = tk.Label(menu, text= "Vitaj " + zak[0], pady=15)
        vitaj_lbl.pack()
        #messagebox.showinfo("", "Vitaj: " + zak[0])

        kred_btn = tk.Button(menu, text= "Kredit / Dobitie kreditu", pady=5, command= Kredit)
        kred_btn.pack()

        poz_knihy_btn = tk.Button(menu, text="Zoznam požičaných kníh", pady=5)
        poz_knihy_btn.pack()

        zoz_knih_btn = tk.Button(menu, text="Zoznam dostupných kníh", pady=5)
        zoz_knih_btn.pack()






okno = tk.mainloop()

connection.close()


