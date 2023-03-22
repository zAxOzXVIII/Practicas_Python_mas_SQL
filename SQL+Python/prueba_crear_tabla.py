# Importamos pymysql
import pymysql

conexion= pymysql.connect(
    host="localhost",
    user="root",
    password="",
    # database="",
    # port=""
    
)

query = conexion.cursor()

sql = "CREATE DATABASE IF NOT EXISTS prueba1_py"
# try:
if(query.execute(sql)):
    print("Se ha creado una base de datos")
else:
    conexion.close
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="prueba1_py"
    )
    query = conexion.cursor()
# except ProgrammingError as e:
# print("Error: "+e)

sql2 = """CREATE TABLE IF NOT EXISTS persona(
    id_p INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(48) NOT NULL,
    cedula VARCHAR(9) NOT NULL,
    fecha_nacimiento DATE,
    hobbie VARCHAR(64),
    PRIMARY KEY(id_p)
    )"""
query.execute(sql2)

conexion.commit()
conexion.close()