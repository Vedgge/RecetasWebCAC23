import mysql.connector
import os

class Credenciales:
    # Obtiene credenciales para operar en la Base de Datos (BdD).
    # Abre y cierra la conección con la misma.
    # A modo de prueba es capaz de imprimirlas también.
    def __init__(self):
        ruta = "RecetasWebCAC23/datos.txt"
        if os.path.exists(ruta):
            with open(ruta, "r") as archivo:
                lineas = archivo.readlines()    
                self._host = lineas[0].strip()
                self._user = lineas[1].strip()
                self._password = lineas[2].strip()
                self._database = lineas[3].strip()
                archivo.close()
        else:
            with open ("RecetasWebCAC23\datos.txt", "w") as archivo:
                print("Desea crear archivo con las credenciales para operar en la base de datos?")
                conf = input("S/N")
                if conf.lower() =="s":
                    print("Se van a guardar las credenciales")
                    self._host = input("host: ")
                    self._user = input("user: ")
                    self._password = input("password: ")
                    self._database = input("database: ")
                    
                    archivo.write(f"{self.host_}\n")
                    archivo.write(f"{self._user}\n")
                    archivo.write(f"{self._password}\n")
                    archivo.write(f"{self._database}\n")
                else:
                    print("Ingrese las credenciales, NO van a ser almacenadas")
                    self.host_ = input("host: ")
                    self._password = input("password: ")
                    self._database = input("database: ")
            archivo.close()

    def imprimir(self):
        print("@"*10)
        print(self._host)
        print(self._user)
        print(self._password)
        print(self._database)
        print("@"*10)

    def conectar(self):
        self.conexion = mysql.connector.connect(
            host = self._host,
            user = self._user,
            password = self._password,
            database = self._database,
        )
        self.cursor = self.conexion.cursor()
    
    def desconectar(self):
        self.conexion.commit()
        self.conexion.close()
        print("Desconectado")
# 

class Consulta(Credenciales):

    def __init__(self, seleccion, tabla):
        super().__init__()
        self.seleccion = seleccion
        self.tabla = tabla
    
    def consultar(self):
        self.conectar()
        self.cursor.execute (f"SELECT {self.seleccion} from {self.tabla}")

        self.resultados = self.cursor.fetchall()
        for fila in self.resultados:
            print(fila)



class CargaDatos(Credenciales):

    def __init__(self,tabla, columnas, valores):
        super().__init__()
        self.tabla = tabla
        self.columnas = columnas
        self.valores = valores
    
    def insertarDato(self):
        self.conectar()
        self.cursor.execute(f"INSERT INTO {self.tabla} ({self.columnas}) VALUES ('{self.valores}')")
        Credenciales.desconectar(self)
    
    def imprimir(self):
        print(f"INSERT INTO {self.tabla} ({self.columnas}) VALUES ('{self.valores}')")



# cons = Consulta("*","categorias")
# cons.consultar()

# carga = CargaDatos("categorias","Categoria","Veganas")
# carga.imprimir()
# carga.insertarDato()
# cons.consultar()
# # cursor.execute ("INSERT INTO categorias (Categoria) VALUES ('Cerdo')")