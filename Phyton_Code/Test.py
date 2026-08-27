import pandas as pd
from datetime import datetime as dt, date, timedelta

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 100
# pd.options.display.max_colwidth = 100
pd.options.display.width = None

wtheute=(date.today().weekday())

# zum Testen
wtheute=dt.strptime('30.09.2024', '%d.%m.%Y').weekday()

if wtheute == 5:
    Importdatei = "/Users/macmario/Dateien/HKABOS_MO.txt"
else:
    Importdatei = "/Users/macmario/Dateien/HKABOS.txt"

df = pd.read_csv(Importdatei,
                 nrows = 5000,
                 index_col = False,
                 header = None,
                 delimiter = ';',
                 names = ['KZ','Erscheinung','WBKdNr','WBAboNr','NWKdNr','NWVerkehrsNr',
                          'Anrede','Titel','Vorname','Hausname','Zusatz1','Zusatz2','Zusatz3',
                          'Strasse','HausNr','HausBs','Lkz','Plz','Ort','Tour','Ablage','Gs','Bezirk','Produkt',
                          'StueckMo','StueckDi','StueckMi','StueckDo','StueckFr','StueckSa','StueckSo','Stuecktgl',
                          'Lieferhinweis','VertArt']
                 )

# Spalte eweise anfügen und Einzeltage anpassen
df.insert(34,"eweise",'')

# alles zu String
df.astype(str)

# Datum aus df zum Werktag ermitteln
dateitag=str(df["Erscheinung"].values[1])
wtdatei=(dt.strptime(dateitag, '%d.%m.%Y').weekday())

# Auf Alte Datei testen
if wtheute == wtdatei:
    print('Datei ist alt')
    df=''
    
# Auf Anzahl Datensätze prüfen 
if len(df.index) <= 1:
    print('zuwening Datensätze')

# fehlerhafte Bezirke löschen
df.drop(df[df["Bezirk"] == 0].index, inplace=True)
df.drop(df[df["Bezirk"] >= 995].index, inplace=True)

# Titel auf Blank          
df['Titel'] = ''

# Zusätzliche ; entfernen
df.replace(',',';')


df['StueckMo']=df['StueckMo'].astype(str)
df['StueckDi']=df['StueckDi'].astype(str)
df['StueckMi']=df['StueckMi'].astype(str)
df['StueckDo']=df['StueckDo'].astype(str)
df['StueckFr']=df['StueckFr'].astype(str)
df['StueckSa']=df['StueckSa'].astype(str)
df['Stuecktgl']=df['Stuecktgl'].astype(str)

df['StueckMo']=df['StueckMo'].replace('0',' ').replace('1','X')
df['StueckDi']=df['StueckDi'].replace('0',' ').replace('1','X')
df['StueckMi']=df['StueckMi'].replace('0',' ').replace('1','X')
df['StueckDo']=df['StueckDo'].replace('0',' ').replace('1','X')
df['StueckFr']=df['StueckFr'].replace('0',' ').replace('1','X')
df['StueckSa']=df['StueckSa'].replace('0',' ').replace('1','X')
df['Stuecktgl']=df['Stuecktgl'].replace('0',' ').replace('1','X')

# eweise mit Einzeltagen fuellen
df['eweise']=df['StueckMo']+df['StueckDi']+df['StueckMi']+df['StueckDo']+df['StueckFr']+df['StueckSa']+' '

# Bei Vollabo alle X setzen
# print(df['Stuecktgl'][:10])

# Eweise auf Voll, wenn taeglich = 1
df.loc[df['Stuecktgl'] == 'X', 'eweise'] = 'XXXXXX '
    
print(df[:5])



# update HKABOS set [Vert-Art] = replace([Vert-Art],';','') from HKABOS
# update HKABOS set [WB-Kd-Nr] = '' from HKABOS where [WB-Abo-Nr] like '%/%'
