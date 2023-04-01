from pymysql import *

conexion = connect(
    host="localhost",
    user="root",
    password="",
    database="prueba1_py"
)
cursor = conexion.cursor()
sql = "UPDATE persona SET nombre='{}', cedula='{}', hobbie='{}', fecha_nacimiento='{}' WHERE nombre='{}'".format("Miguelangel", "32231042", 
                                                                                        "Jugar GTA5 mientras come pepitos",
                                                                                        "1978/03/21",
                                                                                        "Saupaulo")
cursor.execute(sql)

sql = "SELECT nombre, hobbie, fecha_nacimiento FROM persona WHERE cedula LIKE '%042'"
cursor.execute(sql)

datos = cursor.fetchall()

for row in datos:
    print(row)

conexion.commit()
cursor.close()