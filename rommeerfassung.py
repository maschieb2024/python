import tkinter as tk
import math
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

# Funktion zum Speichern der Daten in der Datenbank
def speichern(datum,monika,hermann,doris,mario,option_wert,gode,geuro,ggode,schi,seuro,gschi):

    db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
    )
    
    cursor = db.cursor()

    sql = """
        INSERT INTO romme
        (datum,monika,hermann,doris,mario,option_wert,gode,geuro,ggode,schi,seuro,gschi)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        sql,
        (datum,monika,hermann,doris,mario,option_wert,gode,geuro,ggode,schi,seuro,gschi)
    )
    db.commit()

    # print("Datensatz wurde gespeichert!")

    cursor.close()
    db.close()



# Funktion zum Anzeigen von Fehlermeldungen
def show_error(message):
    messagebox.showerror("Fehler", message)
    
# Ausgabe und Aufbereitung und Speicherung
def ausgabe():
    datum = datum_feld.get()
    monika = monika_feld.get().strip()
    hermann = hermann_feld.get().strip()
    doris = doris_feld.get().strip()
    mario = mario_feld.get().strip()
    option_wert = auswahl.get()

    

    if not monika.isdigit() or not hermann.isdigit() or not doris.isdigit() or not mario.isdigit():
        show_error("Alle Werte müssen Zahlen sein oder \ndürfen nicht leer sein!")
        return

    # Summen Godesaer
    gode = int(monika) + int(hermann) 
    geuro = round((float(abs(gode)/2)/100), 2)
    ggode = float(geuro) + 5.00
    ggode = math.ceil(ggode * 10) / 10


    # Summen Schiebel
    schi= int(doris) + int(mario)
    seuro = round((float(abs(schi)/2)/100), 2)
    gschi = float(seuro) + 5.00
    gschi = math.ceil(gschi * 10) / 10


    # print("Datum: ", datum)
    # print("Monika: ", monika)
    # print("Hermann: ", hermann)
    # print("Doris: ", doris)
    # print("Mario: ", mario)
    # print("option_wert: ", option_wert)
    # print("Punkte Godesaer: ", gode)
    # print("Euro Godesaer: ", geuro)
    # print("Gesamt Godesaer: ", ggode)
    # print("Punkte Schiebel: ", schi)
    # print("Euro Schiebel: ", seuro)
    # print("Gesamt Schiebel: ", gschi)

    speichern(datum,monika,hermann,doris,mario,option_wert,gode,geuro,ggode,schi,seuro,gschi)

    messagebox.showinfo(
    "Gespeichert",
    f"Gespeichert\n"
    f"Godesaer: {gode} Punkte - Gesamt: {ggode:.2f} €\n"
    f"Schiebel: {schi} Punkte - Gesamt: {gschi:.2f} €"
    )

    monika_feld.delete(0, tk.END)
    hermann_feld.delete(0, tk.END)
    doris_feld.delete(0, tk.END)
    mario_feld.delete(0, tk.END)
    auswahl.set("")
    gode=0
    geuro=0
    ggode=0
    schi=0
    seuro=0
    gschi=0

fenster = tk.Tk()
fenster.title("Formular")

# Datum
ttk.Label(fenster, text = "Spieltag:").grid(row = 0, column = 0, sticky = "w", padx = (20, 5), pady = (20, 5))
datum_feld = DateEntry(fenster, date_pattern = "dd.mm.yyyy")
datum_feld.grid(row = 0, column = 1, sticky = "w", padx = (0, 20), pady = (20, 5))

# Punkte Monika, Hermann, Doris, Mario
ttk.Label(fenster, text = "Monika:").grid(row = 1, column = 0, sticky = "w", padx = (20, 5), pady = (10, 5))
monika_feld = ttk.Entry(fenster, width = 20)
monika_feld.grid(row = 1, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))

ttk.Label(fenster, text = "Hermann:").grid(row = 2, column = 0, sticky = "w", padx = (20, 5), pady = (10, 5))
hermann_feld = ttk.Entry(fenster, width = 20)
hermann_feld.grid(row = 2, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))

ttk.Label(fenster, text = "Doris:").grid(row = 3, column = 0, sticky = "w", padx = (20, 5), pady = (10, 5))
doris_feld = ttk.Entry(fenster, width = 20)
doris_feld.grid(row = 3, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))

ttk.Label(fenster, text = "Mario:").grid(row = 4, column = 0, sticky = "w", padx = (20, 5), pady = (10, 5))
mario_feld = ttk.Entry(fenster, width = 20)
mario_feld.grid(row = 4, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))

# Spielort - Vorgabe Godesaer
ttk.Label(fenster, text = "Auswahl:").grid(row = 5, column = 0, sticky = "w", padx = (20, 5), pady = (10, 5))
auswahl = tk.StringVar(value = "Godesaer")
ttk.Radiobutton(fenster, text = "Godesaer", variable = auswahl, value = "Godesaer").grid(row = 6, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))
ttk.Radiobutton(fenster, text = "Schiebel", variable = auswahl, value = "Schiebel").grid(row = 7, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))
ttk.Radiobutton(fenster, text = "Auswärts", variable = auswahl, value = "Auswärts").grid(row = 8, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))

# Buttons
ttk.Button(fenster, text = "Speichern", command = ausgabe).grid(row = 9, column = 0, columnspan = 3, pady = (10, 5))
ttk.Button(fenster, text = "Ende", command = fenster.destroy).grid(row = 9, column = 2, columnspan = 3, pady = (10, 5))

# Hauptfenster ausführen
fenster.mainloop()