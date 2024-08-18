import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime as dt



# ///////////////////////////////////////////////////////////////////////////////////
###################             Vytvorenie DATABAZY           ######################
# ///////////////////////////////////////////////////////////////////////////////////

connection = sqlite3.connect("moja_data.db")
cursor = connection.cursor()


# vytvorenie tabulky zakaznikov
# cursor.execute('''CREATE TABLE IF NOT EXISTS zakaznici (
#    Id INT PRIMARY KEY,
#    First_Name VARCHAR(50),
#    Last_Name VARCHAR(50),
#    Contact VARCHAR(30),
#    PIN_CODE INT  );        ''')

# cursor.execute('ALTER TABLE zakaznici ADD COLUMN Credit FLOAT(10)')
# connection.commit()

# cursor.execute("DROP TABLE IF EXISTS knizky ")          # vymaz tabulky

# vlozenie zakaznikov do tabulky zakaznici
# zakaznici = [
#    (1, 'Dávid', 'Bohinsky', 'david@aaa.com', 1234),
#    (2, 'Janka', 'Milá', 'janka@mila.com', 5257),
#    (3, 'Alica', 'Krátka', 'alica@zoznam.com', 9541),
#    (4, 'Ondrej', 'Mikla', 'ondrej@azet.sk', 1486)]

# cursor.executemany("INSERT INTO zakaznici (Id, First_Name, Last_Name, Contact, PIN_CODE) VALUES (?, ?, ?, ?, ?)", zakaznici)

#cursor.execute("UPDATE zakaznici SET Credit = 53 WHERE Id = 1")
#connection.commit()


# cursor.execute('''CREATE TABLE IF NOT EXISTS knizky (
#    bookID INT PRIMARY KEY,
#    title VARCHAR(100),
#    authors VARCHAR(50),
#   rating FLOAT,
#   num_pages INT,
#   ratings_count INT,
#   FOREIGN KEY(bookID) REFERENCES zakaznici(Id) )     ''')

  #cursor.execute('ALTER TABLE knizky ADD COLUMN Availability STR(1)')        # dodatocne vytvoreny stlpec dostupnosti
#connection.commit()
#print("stlpec vytvoreny")

#cursor.execute('ALTER TABLE knizky ADD COLUMN Book_Owner INT(4)')        # dodatocne vytvoreny stlpec Book_Owner
#connection.commit()
#print("vytvoreny stlpec")

#cursor.execute(""" UPDATE knizky SET Availability = 'A' """)           # nastavenie A/available na vsetky riadky v stlpe dostupnost
#connection.commit()

# data = pd.read_csv('books_v_cvs.csv')
# knizky = 'knizky'

# data.to_sql(knizky, connection, if_exists='replace', index=False)


# ///////////////////////////////////////////////////////////////////////////////////
###################             Program         ####################################
# ///////////////////////////////////////////////////////////////////////////////////


okno = tk.Tk()
okno.title("Knižný systém")

okno.geometry("250x200")

overenie_pin = tk.StringVar()
pin_kody = tk.StringVar()
dobitie = tk.StringVar()
suma = tk.StringVar()
kred = ""
nova_suma = ""
pozad_kniha = tk.StringVar()
pozad_kniha_vratenia = tk.StringVar()
zoznam_poz_knih = []
dostupnost = tk.StringVar()

# Text - vloz PIN
vloz_pin_popis = tk.Label(okno, text="Vlož PIN: ")
vloz_pin_popis.place(x=20)

def Vstup():
    global data_z_riadku_zak
    overenie_pin = pin_zak.get()
    cursor.execute('SELECT * FROM zakaznici WHERE PIN_CODE=?', [overenie_pin])
    data_z_riadku_zak = cursor.fetchone()

    if data_z_riadku_zak:
        messagebox.showinfo("", "Úspešné prihlásenie")
        Hlavne_menu()
    else:
        messagebox.showinfo("", "Neúspešné prihlásenie")


vstup_tl = tk.Button(okno, width=20, text="Potvrď", command=Vstup)
okno.bind('<Return>', lambda event: Vstup())
vstup_tl.place(y=30, x=30)

pin_zak = tk.Entry(okno, width=20, textvariable=overenie_pin)
pin_zak.place(x=80)

def logika_pozicania():
    global pozad_kniha_entry
    global okno_chcem_pozic
    global data_z_riadku_zak


    poz_kniha = pozad_kniha_entry.get()

    cursor.execute('SELECT * FROM knizky WHERE bookID =?', (poz_kniha,))
    data_z_riadku_knihy = cursor.fetchone()


    dostupnost = data_z_riadku_knihy[6]


    if dostupnost == "A":
        cursor.execute("UPDATE knizky SET Availability = 'U' WHERE bookID = ?", (poz_kniha,) )
        cursor.fetchall()
        connection.commit()
        #do riadku book_owner vkladam ID zakaznika
        cursor.execute("UPDATE knizky SET Book_Owner =? WHERE bookID =?", (data_z_riadku_zak[0], poz_kniha))
        cursor.fetchone()
        connection.commit()


        info_lbl = tk.Label(okno_chcem_pozic, text="Kniha bola vypožičaná", fg = "red")
        info_lbl.place(x=65, y=110)
    else:
        nedostupna_lbl = tk.Label(okno_chcem_pozic, text="Kniha nieje k dispozícii", fg = "red")
        nedostupna_lbl.place(x=65, y=110)

#-----------------------------------------------------------------------------

def logika_vratenia():
    global vratena_kniha_entry
    global okno_chcem_vratit
    global data_z_riadku_zak
    global zak


    vratena_kniha = vratena_kniha_entry.get()
    print(vratena_kniha)

    cursor.execute('SELECT * FROM knizky WHERE bookID =?', (vratena_kniha,))
    data_z_riadku_knihy = cursor.fetchone()

    dostupnost = data_z_riadku_knihy[6]

    if dostupnost == "U":
        
        cursor.execute("UPDATE knizky SET Availability = 'A' WHERE bookID = ?", (vratena_kniha,))
        cursor.fetchall()
        connection.commit()
        # do riadku book_owner vkladam ID zakaznika
        cursor.execute("UPDATE knizky SET Book_Owner = '-' WHERE bookID = ?", (vratena_kniha,))
        cursor.fetchone()
        connection.commit()

        info_lbl = tk.Label(okno_chcem_vratit, text="Kniha bola vrátená", fg="red")
        info_lbl.place(x=65, y=110)
    else:
        nedostupna_lbl = tk.Label(okno_chcem_vratit, text="Zadal si nespravnu knihu", fg="red")
        nedostupna_lbl.place(x=65, y=110)

def chcem_vratit():
    global data_z_riadku_zak
    global vratena_kniha_entry
    global okno_chcem_vratit

    okno_chcem_vratit = tk.Tk()
    okno_chcem_vratit.title("")
    okno_chcem_vratit.geometry("270x270")

    info_lbl = tk.Label(okno_chcem_vratit, text="Vlož ID knihy ktorú chceš vrátiť:", anchor='center')
    info_lbl.place(x=20, y=5)
    vratena_kniha_entry = tk.Entry(okno_chcem_vratit, width=15, textvariable=pozad_kniha_vratenia)  # zistujem cislo pozicanej knihy
    vratena_kniha_entry.place(x=80, y=40)
    potvrd_btn = tk.Button(okno_chcem_vratit, text="Potvrď", command=logika_vratenia)
    potvrd_btn.place(x=100, y=70)



def zoznam_pozic_knih():
    global pozad_kniha_entry
    global okno_chcem_pozic
    global data_z_riadku_zak
    global data_z_riadku
    okno_poz_knih = tk.Tk()
    okno_poz_knih.title("Tvoj zoznam požičaných kníh")
    okno_poz_knih.geometry("700x300")

    #vytvaram tabulku kde vypisujem knihy ku konkr ID zakaznikovi
    dotaz = "SELECT knizky.title FROM zakaznici INNER JOIN knizky" \
            " ON knizky.Book_Owner = zakaznici.Id" \
            " WHERE zakaznici.Id = %s" % data_z_riadku_zak[0]

    cursor.execute(dotaz)

    vlastnici_kniziek = cursor.fetchall()

    zoznam = ttk.Treeview(okno_poz_knih, columns=('authors', ), show='tree', height=40)
    zoznam.pack(fill='x')

    zoznam.column("#0", width=0, stretch=tk.NO)

    for r in vlastnici_kniziek:
        zoznam.insert('', 'end', values=r)


    scrollbar = ttk.Scrollbar(zoznam, orient="vertical", command=zoznam.yview)
    zoznam.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    zoznam.pack(side='left', fill='both', expand=True)

def chcem_pozic():
    global data_z_riadku_zak
    global pozad_kniha_entry
    global okno_chcem_pozic

    okno_chcem_pozic = tk.Tk()
    okno_chcem_pozic.title("")
    okno_chcem_pozic.geometry("270x270")

    info_lbl = tk.Label(okno_chcem_pozic, text="Vlož ID knihy ktorú chceš požičiať", anchor='center')
    info_lbl.place(x=20, y=5)
    pozad_kniha_entry = tk.Entry(okno_chcem_pozic, width=15, textvariable=pozad_kniha)     #zistujem cislo pozicanej knihy
    pozad_kniha_entry.place(x=80, y=40)
    potvrd_btn = tk.Button(okno_chcem_pozic, text="Potvrď", command=logika_pozicania)
    potvrd_btn.place(x=100, y=70)



def dostupne_knihy():
    okno_dos_knih = tk.Tk()
    okno_dos_knih.title("Dostupné Knihy")
    okno_dos_knih.geometry("1350x900")

    cursor.execute('SELECT * FROM knizky')
    riadky_knihy = cursor.fetchall()

    zoznam = ttk.Treeview(okno_dos_knih, columns=('bookID', 'Title', 'Authors', 'Rating', 'Num_Pages',
                                                  'Ratings_count', 'Availability'),show='headings', height=40)
    zoznam.pack(fill='x')

    for r in riadky_knihy:
        zoznam.insert('', 'end', values=r)

    #nastavenie textu hlaviciek
    zoznam.heading('bookID', text='ID', anchor='center')
    zoznam.heading('Title', text='Title', anchor='center')
    zoznam.heading('Authors', text='Authors', anchor='center')
    zoznam.heading('Rating', text='Rating', anchor='center')
    zoznam.heading('Num_Pages', text='Num Pages', anchor='center')
    zoznam.heading('Ratings_count', text='Ratings Count', anchor='center')
    zoznam.heading('Availability', text='Availability', anchor='center')
    zoznam.pack()
    # nastavenie sirky stlpcov
    zoznam.column('bookID', width=8, anchor='center')
    zoznam.column('Title', width=500)
    zoznam.column('Authors', width=200)
    zoznam.column('Rating', width=30, anchor='center')
    zoznam.column('Num_Pages', width=30, anchor='center')
    zoznam.column('Ratings_count', width=50, anchor='center')
    zoznam.column('Availability', width=75, anchor='center')

    scrollbar = ttk.Scrollbar(zoznam, orient="vertical", command=zoznam.yview)
    zoznam.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    zoznam.pack(side='left', fill='both', expand=True)

def pripisanie_kreditu():       # konkr hodnoty som musel "prehodit" do str
    global kredit
    global pozad_sum_dob
    global data_z_riadku_zak

    pin = data_z_riadku_zak[4]

    suma = pozad_sum_dob.get()
    suma_int = int(suma)
    print(type(suma_int))

    stary_kredit = data_z_riadku_zak[5]
    stary_kredit_int = int(data_z_riadku_zak[5])
    print(stary_kredit_int)
    print(type(stary_kredit_int))

    nova_suma = stary_kredit_int + suma_int
    nova_suma_str = str(nova_suma)
    print(nova_suma_str)
    print(type(nova_suma_str))

    cursor.execute('UPDATE zakaznici SET Credit = Credit + ? WHERE PIN_Code = ?', (suma_int, pin))
    connection.commit()

    messagebox.showinfo("", "Kredit úspešne dobitý")

    stav_kred_lbl.config(text="Stav kreditu: " + nova_suma_str)

    kredit.after(1, kredit.destroy)

#///////////////////////////////////////////

def Dobitie_Kreditu():
    global data_z_riadku_zak
    global kredit
    global pozad_sum_dob

    dobi_lbl = tk.Label(kredit, text="Zadaj sumu: ")
    dobi_lbl.place(x=10, y=70)
    pozad_sum_dob = tk.Entry(kredit, width=8, textvariable=suma)
    pozad_sum_dob.place(x=83, y=70)

    potvrd_btn = tk.Button(kredit, text="Potvrď", command=pripisanie_kreditu)
    potvrd_btn.place(x=85, y=90)

def Kredit():
    global kredit
    global data_z_riadku_zak
    global stav_kred_lbl
    kredit = tk.Tk()
    kredit.title("Kredit")
    kredit.geometry("250x250")

    stav_kred_lbl = tk.Label(kredit, text="Stav kreditu: " + str(data_z_riadku_zak[5]))
    stav_kred_lbl.pack()

    dobit_btn = tk.Button(kredit, text="Dobitie kreditu", command=Dobitie_Kreditu)
    dobit_btn.pack()


def Hlavne_menu():
    global zak
    okno.destroy()
    menu = tk.Tk()
    menu.title("Hlavne menu")
    menu.geometry("250x250")

    cursor.execute('SELECT First_Name FROM zakaznici WHERE PIN_CODE=?', [overenie_pin.get()])
    zak = cursor.fetchone()

    if zak:
        vitaj_lbl = tk.Label(menu, text="Vitaj " + zak[0], pady=15)
        vitaj_lbl.pack()
        # messagebox.showinfo("", "Vitaj: " + zak[0])

        kred_btn = tk.Button(menu, text="Kredit / Dobitie kreditu", pady=5, command=Kredit)
        kred_btn.pack()

        poz_knihy_btn = tk.Button(menu, text="Zoznam požičaných kníh", pady=5, command=zoznam_pozic_knih)
        poz_knihy_btn.pack()

        zoz_dos_knih_btn = tk.Button(menu, text="Zoznam dostupných kníh", pady=5, command=dostupne_knihy)
        zoz_dos_knih_btn.pack()

        chcem_poz_btn = tk.Button(menu, text="Chcem si požičiať", pady=5, command=chcem_pozic)
        chcem_poz_btn.pack()

        chcem_vratit_btn = tk.Button(menu, text="Chcem vrátiť", pady=5, command=chcem_vratit)
        chcem_vratit_btn.pack()

        datum = dt.datetime.now()
        datum_lbl = tk.Label(menu, text=f"{datum:%A, %B %d, %Y}", font="Calibri, 8")
        datum_lbl.place(x=105, y=225)



okno = tk.mainloop()

connection.close()


