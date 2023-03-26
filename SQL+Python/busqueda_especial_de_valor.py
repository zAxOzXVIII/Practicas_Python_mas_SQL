import pymysql as py

conexion = py.connect(
    host="localhost",
    user="root",
    password="",
    database="prueba1_py"
)
cursor=conexion.cursor()

# query="SELECT * FROM persona"
query="SELECT id_p,nombre,fecha_nacimiento FROM persona WHERE nombre LIKE '%o'"
cursor.execute(query)
datos=cursor.fetchall()

for row in datos:
    print(row)