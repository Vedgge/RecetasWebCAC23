import mysql.connector
import os

# Falta agregar una forma de utilizar la consulta agregando la opción --where--

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
    
    def comitear(self):
        self.conexion.commit()
        print("Comieteado")

    def desconectar(self):
        self.conexion.close()
        print("Desconectado")
# 
class Consulta(Credenciales):

    def __init__(self, seleccion, tabla,condicion):
        super().__init__()
        self.seleccion = seleccion
        self.tabla = tabla
        self.condicion = condicion
    
    def consultar(self):
        if not self.condicion:
            self.conectar()
            self.cursor.execute (f"SELECT {self.seleccion} from {self.tabla}")

        self.resultados = self.cursor.fetchall()
        for fila in self.resultados:
            print(fila)
#
class CargaDatos(Credenciales):
    # valores, al igual que columnas por algún motivo necesita ingresar entre "", y si por algún motivo
    # Se inscribe un único valor, debe hacerse "'elemento a ingresar'"

    def __init__(self,tabla, columnas, valores):
        super().__init__()
        self.tabla = tabla
        self.columnas = columnas
        self.valores = valores
    
    def insertarDato(self):
        self.conectar()
        self.cursor.execute(f"INSERT INTO {self.tabla} ({self.columnas}) VALUES ({self.valores})")
        Credenciales.comitear(self)
    
    def imprimir(self):
        print(f"INSERT INTO {self.tabla} ({self.columnas}) VALUES ({self.valores})")
#

# #######################
# Conexión de la BdD
# Inicio de código CRUD
cc = Credenciales()
cc.conectar()

# # #######################
# # CRUD en tabla categorias

# categoriaNueva = CargaDatos("categorias","Categoria","'Veganas'")
# categoriaNueva.imprimir()
# categoriaNueva.insertarDato()

# consultaCategorias = Consulta("*","categorias",False)
# consultaCategorias.consultar()

# # #######################
# # CRUD en tabla usuarios

# datoUsuario = "'NOm', 'AP', '2005', 'mail@gmail.com', 'jklñ', 'masc'"
# usuario = CargaDatos("usuarios","Nombre, Apellido, Nacimiento, correoElectrónico, Hash, Genero",datoUsuario)
# usuario.imprimir()
# usuario.insertarDato()

# consultaUsuarios = Consulta("*","usuarios",False)
# consultaUsuarios.consultar()

# # #######################
# # CRUD en tabla recetas

# datosReceta ="'NOm', 'AP', '20', 'mail@gmail.com', '2', '1', '6', 'Intermedio'"
# receta = CargaDatos("recetas","NombreReceta, Receta, Porciones, urlImagen, TiempoMin, idUsuario, idCategoria, dificultad",datosReceta)
# receta.imprimir()
# receta.insertarDato()

# consultaRecetas = Consulta("*","usuarios",False)
# consultaRecetas.consultar()

# #######################
# CRUD en tabla favoritos

# favoritoNuevo = CargaDatos("favoritos","idReceta, idUsuario","'1', '1'")
# favoritoNuevo.imprimir()
# favoritoNuevo.insertarDato()

# consultaFavoritos = Consulta("*","favoritos",False)
# consultaFavoritos.consultar()



print("#"*60)



# #######################
# Desconexión de la BdD
# Fin de código CRUD
cc.desconectar()