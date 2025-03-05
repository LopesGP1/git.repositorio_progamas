import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '65323310',
    database = 'usuario',
)
cursor = conn.cursor()
#cruse
id_cliente =  input ("Digite o id do cliente:")
senha = input ("Digite sua senha :")
nome_usuario = input ("Digite seu nome :")
email = input ("Digite seu email")
comando = f'insert into tb_lg_usuario (id_cliente,senha,nome_usuario,email) values ("{id_cliente}","{senha}","{nome_usuario}","{email}")'

cursor.execute(comando)
conn.commit()

cursor.close()
conn.close()    
