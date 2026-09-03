import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def speichern():

    datum = '2026-08-27'
    text_ = 'Hier steht neuer Text'
    punkte = 1005
    option_wert = '5'

    db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
    )
    
    cursor = db.cursor()

    sql = """
        INSERT INTO text03
        (datum, text_, punkte, option_wert)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        sql,
        (datum, text_, punkte, option_wert)
    )

    db.commit()

    print("Datensatz wurde gespeichert!")

    cursor.close()
    db.close()


speichern()