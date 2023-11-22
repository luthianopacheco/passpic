from persistencia.conexao_db import databaseConnection

# Salvando dados no banco de dados
def insertData(nome:str, cpf:str, data_nascimento:str, celular:str, user_image:str, 
            cep:str, logradouro:str, numero:str, complemento:str, bairro:str, cidade:str, uf:str, pais:str):
    try:
        # buscando a conexão com o banco de dados
        connection = databaseConnection()
        cursor = connection.cursor()

        # fazendo os comandos de insert no banco de dados
        user_query = f'insert into user values (null, "{nome}","{cpf}","{data_nascimento}","{celular}","{user_image}");'
        endereco_query = f'insert into endereco values (null, "{cep}","{logradouro}","{numero}","{complemento}","{bairro}","{cidade}","{uf}","{pais}");'
        cursor.execute(user_query)
        connection.commit()
        cursor.execute(endereco_query)
        connection.commit()

        # fechando as conexões
        cursor.close()
        connection.close()
        
    except Exception as e:
        cursor.close()
        connection.close()
        print (e)


# ------------------------------------------------------------------------------------------------------------- #


def getDataToTable():
    try:
        connection = databaseConnection()
        cursor = connection.cursor()

        user_query = f'select * from user;'
        cursor.execute(user_query)
        user_data = cursor.fetchall()
        # endereco_query = f'select * from endereco'
        # cursor.execute(endereco_query)
        # endereco_data = cursor.fetchall()

        user_list = []
        # endereco_list = []

        for item in user_data:
            user_list.append(item)
        
        # for item in endereco_data:
        #     endereco_list.append(item)


        cursor.close()
        connection.close()

        return user_list
    except Exception as e:
        cursor.close()
        connection.close()
        print (e)    


# ------------------------------------------------------------------------------------------------------------- #

def getDataById(id):
    try:
        connection = databaseConnection()
        cursor = connection.cursor()

        user_query = f'select * from user where iduser={id};'
        endereco_query = f'select * from endereco where idendereco={id}'
        cursor.execute(user_query)
        user_data = cursor.fetchall()
        cursor.execute(endereco_query)
        endereco_data = cursor.fetchall()

        user_list = []
        endereco_list = []

        for item in user_data:
            user_list.append(item)
        
        for item in endereco_data:
            endereco_list.append(item)


        cursor.close()
        connection.close()

        return user_list, endereco_list
    except Exception as e:
        cursor.close()
        connection.close()
        print (e)    


# ------------------------------------------------------------------------------------------------------------- #


def updateData(id, nome:str, cpf:str, data_nascimento:str, celular:str, 
               cep:str, logradouro:str, numero:str, complemento:str, bairro:str,
               cidade:str, uf:str, pais:str):
    try:
        connection = databaseConnection()
        cursor = connection.cursor()
        
        user_query = f'update user set nome="{nome}", cpf="{cpf}", data_nascimento="{data_nascimento}", celular="{celular}" where iduser={id};'
        endereco_query = f'update endereco set cep="{cep}", logradouro="{logradouro}", numero="{numero}", complemento="{complemento}", bairro="{bairro}", cidade="{cidade}", uf="{uf}", pais="{pais}" where idendereco={id};'
        cursor.execute(user_query)
        connection.commit()
        cursor.execute(endereco_query)
        connection.commit()
        
        
        cursor.close()
        connection.close()

    except Exception as e:
        cursor.close()
        connection.close()
        print (e)    
        

# ------------------------------------------------------------------------------------------------------------- #


def deleteData(id):
    try:
        connection = databaseConnection()
        cursor = connection.cursor()
        
        user_query = f'delete from user where iduser={id}'
        endereco_query = f'delete from endereco where idendereco={id}'
        cursor.execute(user_query)
        connection.commit()
        cursor.execute(endereco_query)
        connection.commit()
        
        cursor.close()
        connection.close()

    except Exception as e:
        cursor.close()
        connection.close()
        print (e)    
        

# ------------------------------------------------------------------------------------------------------------- #

# Teste get - OK
# user, endereco = getData()
# print(user[0])
# print('\n\n','-'*20,'\n\n')
# print(endereco)

        # ------------------------------------------------------------------------------------------- #

# Teste update - OK
# updateData(id='5', nome='Juliana', cpf='99988877745', data_nascimento='1990-09-09', celular='11888776655', 
#            cep='01001-000', logradouro='Av. Augusta', numero='3535', complemento='Loja 1056', bairro='Sé',
#            cidade='São Paulo', uf='SP', pais='BR')

        # ------------------------------------------------------------------------------------------- #

# Teste delete - OK
# deleteData(id='8')

        # ------------------------------------------------------------------------------------------- #
