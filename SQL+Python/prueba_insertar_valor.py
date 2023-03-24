import pymysql as my

conexion = my.connect(
    host="localhost",
    user="root",
    password="",
    database="prueba1_py"
)
query = conexion.cursor()

sql = "INSERT INTO persona(nombre,cedula,fecha_nacimiento,hobbie) VALUES ('{}','{}','{}','{}')".format("Gru Edsrn","21224553","1938/2/22","Juega Fifa")

query.execute(sql)

conexion.commit()
conexion.close()