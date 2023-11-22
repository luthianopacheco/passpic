from persistencia.conexao_db import databaseConnection

# Verifica a conexao com o banco de dados - Xampp deve estar conectado
def test_conexao_db():
    connection = databaseConnection()
    assert connection.is_connected() == True