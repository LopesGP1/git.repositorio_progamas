import mysql.connector

# Conectar ao MySQL
conn = mysql.connector.connect(
    host="localhost",  # Ou IP do servidor
    user="root",       # Seu usuário do MySQL
    password='65323310',  # Coloque sua senha do MySQL aqui
    database="ts_login"   # Nome do banco de dados que deseja conectar
)
# Criar um cursor para executar comandos SQL
cursor = conn.cursor()
#s dados ao usuário
nome = input("Nome: ")
seg_nome = input("Segundo nome: ")
ult_nome = input("Último nome: ")
data_nasc = input("Data de nascimento (YYYY-MM-DD): ")
nume_pai = input("Nome do pai: ")
nume_mae = input("Nome da mãe: ")
cidade = input("Cidade: ")

# Tupla com os valores coletados
valores = (nome, seg_nome, ult_nome, data_nasc, nume_pai, nume_mae, cidade)

# Executar o comando e salvar no banco
cursor.execute(sql, valores)
conn.commit()
print(f"Cliente {nome} cadastrado com sucesso!")
# Fechar conexão
cursor.close()
conn.close()
 #Comando SQL para inserir dados na tabela
#sql = """
#INSERT INTO cliente (nome, seg_nome, ult_nome, data_nasc, nume_pai, nume_mae, cidade)
#VALUES (%s, %s, %s, %s, %s, %s, %s)
#"""
# Pedir o