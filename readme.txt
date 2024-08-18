Program: Knižný systém
O čom je tento program?
Tento program je jednoduchý systém na správu knižnice, ktorý umožňuje používateľom požičať si knihy, vrátiť ich, spravovať svoj kredit 
a zobraziť zoznam dostupných kníh. Program využíva SQLite databázu na ukladanie informácií o zákazníkoch a knihách. 
Používateľské rozhranie je vytvorené pomocou knižnice Tkinter.

Hlavné funkcie programu:
Správa databázy:

Program vytvára databázu s tabuľkami pre zákazníkov a knihy.
Ukladá informácie o zákazníkoch, vrátane ich mena, kontaktných údajov a PIN kódu.
Ukladá informácie o knihách, vrátane titulu, autorov, hodnotenia, počtu strán, dostupnosti a vlastníka knihy.
Prihlásenie používateľa:

Používateľ sa prihlási pomocou svojho PIN kódu.
Po úspešnom prihlásení je presmerovaný do hlavného menu, kde môže vykonávať ďalšie operácie.
Požičanie a vrátenie kníh:

Používateľ si môže požičať knihu, ak je dostupná.
Požičaná kniha sa označí ako nedostupná a jej vlastník sa zmení na aktuálneho používateľa.
Používateľ môže knihu vrátiť, čím sa kniha označí ako dostupná a vlastníctvo sa vymaže.
Správa kreditu:

Používateľ môže zobraziť stav svojho kreditu a dobiť si kredit.
Zobrazenie zoznamu kníh:

Program umožňuje zobraziť zoznam všetkých dostupných kníh.
Používateľ môže zobraziť zoznam kníh, ktoré má aktuálne požičané.
Technológie použité v programe:
SQLite3: Pre správu databázy.
Tkinter: Pre vytvorenie grafického používateľského rozhrania.
Pandas (komentované): Potenciálne použitie pre import/export dát z/do CSV súborov.
Inštrukcie pre použitie:
Spustite program a prihláste sa pomocou PIN kódu.
V hlavnom menu vyberte požadovanú akciu: zobrazenie kníh, požičanie knihy, vrátenie knihy alebo správa kreditu.
Po ukončení práce sa prihlásenie uzavrie a spojenie s databázou sa automaticky ukončí.




README
Program: Book System
What is this program about?
This program is a simple library management system that allows users to borrow books, return them, manage their credit, and view a list of available books. The program uses an SQLite database to store information about customers and books. The user interface is created using the Tkinter library.

Main Features of the Program:
Database Management:

The program creates a database with tables for customers and books.
It stores customer information, including their first name, last name, contact details, and PIN code.
It stores book information, including title, authors, rating, number of pages, availability, and the book owner.
User Login:

Users can log in using their PIN code.
After a successful login, the user is redirected to the main menu, where they can perform various operations.
Borrowing and Returning Books:

Users can borrow a book if it is available.
Borrowed books are marked as unavailable, and the owner is set to the current user.
Users can return a book, marking it as available and clearing the ownership.
Credit Management:

Users can view their credit balance and top up their credit.
Viewing Book Lists:

The program allows users to view a list of all available books.
Users can also view a list of books they have currently borrowed.
Technologies Used:
SQLite3: For database management.
Tkinter: For creating the graphical user interface.
Pandas (commented out): Potential use for importing/exporting data from/to CSV files.
Instructions for Use:
Run the program and log in using your PIN code.
In the main menu, choose the desired action: view books, borrow a book, return a book, or manage your credit.
After finishing your work, the session will close and the connection to the database will be automatically terminated.