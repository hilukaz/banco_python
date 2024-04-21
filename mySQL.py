import mysql.connector
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa a variável de ambiente PASSWORD
password = os.getenv('PASSWORD')

try:
    # Estabeleça a conexão com o MySQL 
    conexao = mysql.connector.connect(
        host="localhost",  # Se estiver executando o MySQL localmente
        user="root", 
        password=password,  
        database="python"  # O nome do banco de dados que você deseja acessar
    )

    # Verifique se a conexão foi estabelecida
    if conexao.is_connected():
        print("Conexão ao MySQL bem-sucedida!")

    # Crie um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Crie uma tabela (se ela ainda não existir)
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), idade INT)")
    
    # Função para criar um registro (Create)
    def criar_usuario(nome, idade):
        sql = "INSERT INTO usuarios (nome, idade) VALUES (%s, %s)"
        val = (nome, idade)
        cursor.execute(sql, val)
        conexao.commit() # Confirma a inserção no banco de dados
        print(cursor.rowcount, "registro inserido.")

    # Função para ler todos os registros (Read)
    def ler_usuarios():
        cursor.execute("SELECT * FROM usuarios")
        result = cursor.fetchall()
        for row in result:
            print(row)

    # Função para atualizar um registro (Update)
    def atualizar_usuario(id, novo_nome):
        sql = "UPDATE usuarios SET nome = %s WHERE id = %s"
        val = (novo_nome, id)
        cursor.execute(sql, val)
        conexao.commit()
        print(cursor.rowcount, "registro(s) atualizado(s).")

    # Função para deletar um registro (Delete)
    def deletar_usuario(id):
        sql = "DELETE FROM usuarios WHERE id = %s"
        val = (id,)
        cursor.execute(sql, val)
        conexao.commit()
        print(cursor.rowcount, "registro(s) removido(s).")

    # Exemplos de uso
    criar_usuario("Alice", 25)
    criar_usuario("Bob", 30)
    ler_usuarios()
    atualizar_usuario(1, "Alice Silva")
    deletar_usuario(2)

    # Feche o cursor e a conexão quando terminar
    cursor.close()
    conexao.close()

except mysql.connector.Error as erro:
    print("Erro ao conectar ao MySQL:", erro)
    cursor.close()
    conexao.close()
