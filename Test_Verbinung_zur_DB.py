import mysql.connector

print("Connector:", mysql.connector.__version__)

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DifdMac!2024",
        database="msdb"
    )

    print("Verbindung erfolgreich!")

    db.close()

except Exception as e:
    print("Fehler:")
    print(type(e).__name__)
    print(e)