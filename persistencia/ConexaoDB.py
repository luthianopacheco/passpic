import mysql.connector

# conexão com banco de dados
def databaseConnection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_passpic',
        )
        return connection
    
    except Exception as e:
        connection.close()
        print(e)