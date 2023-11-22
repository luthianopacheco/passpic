from controller.controller import *

# ------------------------------------ getDataToTable ----------------------------------------- #

# Verifica o tamanho da lista que retorna todos os dados do banco de dados do usuario
def test_get_all_data():
    user = getDataToTable()
    assert len(user) > 0

# ------------------------------------ getDataByID ----------------------------------------- #

user, endereco = getDataById('8')

# Verifica se o ID buscado no banco de dados contem o nome
def test_get_one_data_1():
    assert 'Luthiano' in user[0][1]

def test_get_one_data_2():
    assert '91010-000' in endereco[0][1]