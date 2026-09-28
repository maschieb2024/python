import mysql.connector

# unter Python 3.14.0 den mysql-Connector-python auf version 9.7.0 zurückstellen

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