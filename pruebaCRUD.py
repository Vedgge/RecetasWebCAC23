import mysql.connector
import os



class VerificarCredenciales:
    def __init__(self, ruta):
        if os.path.exists(ruta):
            with open(ruta, "r") as archivo:
                lineas = archivo.readlines()    
                self.Host = lineas[0].strip()
                self.User = lineas[1].strip()
                self.Password = lineas[2].strip()
                self.Database = lineas[3].strip()
                archivo.close()
        else:
            with open ("RecetasWebCAC23\datos.txt", "w") as archivo:
                print("Desea crear archivo con las credenciales para operar en la base de datos?")
                conf = input("S/N")
                if conf.lower() =="s":
                    print("Se van a guardar las credenciales")
                    self.host = input("host: ")
                    self.user = input("user: ")
                    self.password = input("password: ")
                    self.database = input("database: ")
                    
                    archivo.write(f"{self.host}\n")
                    archivo.write(f"{self.user}\n")
                    archivo.write(f"{self.password}\n")
                    archivo.write(f"{self.database}\n")
                else:
                    print("Ingrese las credenciales, NO van a ser almacenadas")
                    self.host = input("host: ")
                    self.password = input("password: ")
                    self.database = input("database: ")
            archivo.close()

    def imprimir(self):
        print(self.Host)
        print(self.User)
        print(self.Password)
        print(self.Database)

credenciales = VerificarCredenciales("RecetasWebCAC23/datos.txt")


conexion = mysql.connector.connect(
    host = credenciales.Host,
    user = credenciales.User,
    password = credenciales.Password,
    database = credenciales.Database,
)




cursor = conexion.cursor()


# cursor.execute ("INSERT INTO categorias (Categoria) VALUES ('Cerdo')")


cursor.execute ("SELECT * from categorias")

resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

conexion.commit()
conexion.close()