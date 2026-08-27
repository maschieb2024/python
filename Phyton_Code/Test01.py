import pandas as pd
from datetime import datetime as dt, date, timedelta

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 100
# pd.options.display.max_colwidth = 100
pd.options.display.width = None

wtheute = (date.today().weekday())

# zum Testen
wtheute = dt.strptime('30.09.2024', '%d.%m.%Y').weekday()

if wtheute == 5:
Importdatei = "/Users/macmario/Dateien/HKABOS_MO.txt"
else :
Importdatei = "/Users/macmario/Dateien/HKABOS.txt"

df = pd.read_csv(Importdatei,
    nrows = 500,
    index_col = False,
    header = None,
    delimiter = ';',
    names = ['KZ','Erscheinung','WBKdNr','WBAboNr','NWKdNr','NWVerkehrsNr',
        'Anrede','Titel','Vorname','Hausname','Zusatz1','Zusatz2','Zusatz3',
        'Strasse','HausNr','HausBs','Lkz','Plz','Ort','Tour','Ablage','Gs','Bezirk','Produkt',
        'StueckMo','StueckDi','StueckMi','StueckDo','StueckFr','StueckSa','StueckSo','Stuecktgl',
        'Lieferhinweis','VertArt']
)
# print(df)

# Spalte eweise anfügen und Einzeltage anpassen
df.insert(34,"Eweise",'')

# alles zu String
df.astype(str)
df['Stuecktgl'] = df['Stuecktgl'].astype(str)

print(df['Stuecktgl'][:10])

df.loc[df['Stuecktgl'] == '1', 'Eweise'] = 'XXXXXX '

print(df['Eweise'])