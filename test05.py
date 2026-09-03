import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def speichern():

    datum = datum_feld.get()
    text_ = text_feld.get("1.0", tk.END).strip()
    option = auswahl.get()

    print("Datum: ",datum)
    print("Text: ",text_)
    print("Option: ",option)

fenster = tk.Tk()
fenster.title("formular")
fenster.geometry("500x500")

# Datum
ttk.Label(fenster, text="Datum:").pack(anchor="w",padx=20,pady=(20,5))

datum_feld = DateEntry(fenster, date_pattern = "dd.mm.yyyy")
# datum_feld = tk.Text(fenster, height=1, width=20)

datum_feld.pack(anchor="w",padx=20)

# text
ttk.Label(fenster, text="Text:").pack(anchor="w",padx=20,pady=(20,5))
text_feld = tk.Text(fenster, height=8, width=50)
text_feld.pack(anchor="w",padx=20)

# options_button
ttk.Label(fenster, text="Auswahl:").pack(anchor="w",padx=20,pady=(20,5))
auswahl = tk.StringVar(value="Option 1")

ttk.Radiobutton(fenster, text="Option 1", variable=auswahl, value="Option 1",).pack(anchor="w",padx=30)
ttk.Radiobutton(fenster, text="Option 2", variable=auswahl, value="Option 2",).pack(anchor="w",padx=30)
ttk.Radiobutton(fenster, text="Option 3", variable=auswahl, value="Option 3",).pack(anchor="w",padx=30)

# speichern
ttk.Button(fenster, text="Speichern", command=speichern).pack(pady=10)
# Ende
ttk.Button(fenster, text="Ende", command=fenster.destroy).pack(pady=5)

fenster.mainloop()

# print("auswahl: ",auswahl.get())