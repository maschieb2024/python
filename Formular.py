import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def show_error(message):
    messagebox.showerror("Fehler", message)

def ausgabe():
    datum = datum_feld.get()
    monika = monika_feld.get().strip()
    hermann = hermann_feld.get().strip()
    doris = doris_feld.get().strip()
    mario = mario_feld.get().strip()
    option = auswahl.get()
    gode = monika + hermann
    geuro = abs(gode +5)/2
    gges = geuro + 5

    if not monika.isdigit():
        show_error("Monika muss eine Zahl sein!")
        return

    if not hermann.isdigit():
        show_error("Hermann muss eine Zahl sein!")
        return

    print("Datum: ", datum)
    print("Monika: ", monika)
    print("Hermann: ", hermann)
    print("Doris: ", doris)
    print("Mario: ", mario)
    print("Option: ", option)
    print(gode)
    print(geuro)
    print(gges)

    messagebox.showinfo("Gespeichert", "Die Daten wurden erfolgreich gespeichert!")

    monika_feld.delete(0, tk.END)
    hermann_feld.delete(0, tk.END)
    doris_feld.delete(0, tk.END)
    mario_feld.delete(0, tk.END)
    auswahl.set("")
    gode.set(0)
    geuro.set(0)
    gges.set(0)

    fenster = tk.Tk()
    fenster.title("Formular")

    ttk.Label(fenster, text = "Spieltag:").grid(row = 0, column = 0, sticky = "w", padx = (20, 5), pady = (20, 5))
    datum_feld = DateEntry(fenster, date_pattern = "dd.mm.yyyy")
    datum_feld.grid(row = 0, column = 1, sticky = "w", padx = (0, 20), pady = (20, 5))

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

    ttk.Label(fenster, text = "Auswahl:").grid(row = 5, column = 0, sticky = "w", padx = (20, 5), pady = (10, 5))
    auswahl = tk.StringVar(value = "")
    ttk.Radiobutton(fenster, text = "Godesaer", variable = auswahl, value = "Godesaer").grid(row = 6, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))
    ttk.Radiobutton(fenster, text = "Schiebel", variable = auswahl, value = "Schiebel").grid(row = 7, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))
    ttk.Radiobutton(fenster, text = "Auswärts", variable = auswahl, value = "Auswärts").grid(row = 8, column = 1, sticky = "w", padx = (0, 20), pady = (10, 5))

    ttk.Button(fenster, text = "Speichern", command = ausgabe).grid(row = 9, column = 0, columnspan = 3, pady = (10, 5))
    ttk.Button(fenster, text = "Ende", command = fenster.destroy).grid(row = 9, column = 2, columnspan = 3, pady = (10, 5))

    fenster.mainloop()