# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)
app.config['encoding'] = 'UTF-8'

import mysql.connector
import os, hashlib
from datetime import datetime

# CREO QUE SE NECESITA ELIMINAR PARTE DE LA FUNCIÓN REEMPLAZO DE PÁGINA

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
        self.cursor = self.conexion.cursor(dictionary=True)
        print('Conectado')
    
    def comitear(self):
        self.conexion.commit()
        print("Comiteado")

    def desconectar(self):
        self.conexion.close()
        print("Desconectado")
# 
class Consulta(Credenciales):

    def __init__(self, seleccion, tabla, condicion=False, orden=False, limit=8):
        super().__init__()
        self.seleccion = seleccion
        self.tabla = tabla
        self.condicion = condicion
        self.orden = orden
        self.limit = limit
    
    def consultar(self):
        self.conectar()
        if not self.orden:
            self.orden = ""
        else:
            self.orden = f" ORDER BY {self.orden} DESC limit {self.limit}"
        
        if not self.condicion:
            self.cursor.execute ("SELECT %s FROM %s" % (self.seleccion,self.tabla,)+self.orden)
        else:
            self.cursor.execute ("SELECT %s FROM %s WHERE %s" % (self.seleccion,self.tabla,self.condicion,)+self.orden)
        
        self.resultados = self.cursor.fetchall()

    def imprimir(self):
        if not self.condicion:
            print("SELECT %s FROM %s" % (self.seleccion,self.tabla,))
        else:
            print("SELECT %s FROM %s WHERE %s" % (self.seleccion,self.tabla,self.condicion,))       
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
        self.cursor.execute("INSERT INTO %s (%s) VALUES (%s)" % (self.tabla, self.columnas, self.valores,))
        Credenciales.comitear(self)
    
    def imprimir(self):
        print("INSERT INTO %s (%s) VALUES (%s)" % (self.tabla, self.columnas, self.valores,))
#
class ModificarDatos(Credenciales):
    def __init__(self,tabla, valores):
        super().__init__()
        self.tabla = tabla
        self.valores = valores

    
    def modificarDato(self):
        self.conectar()
        if self.tabla == 'recetas':
            self.cursor.execute("UPDATE recetas SET NombreReceta = '%s', Ingredientes = '%s', Receta = '%s',  Porciones = %s, urlImagen = '%s', TiempoMin = %s,idUsuario = %s, idCategoria = %s, dificultad = '%s' WHERE idReceta = %s" 
                % (self.valores["NombreReceta"], self.valores["Ingredientes"], self.valores["Receta"], self.valores["Porciones"], self.valores["urlImagen"], self.valores["TiempoMin"], self.valores["idUsuario"], self.valores["idCategoria"], self.valores["dificultad"], self.valores["id"])) 
            
        elif self.tabla == 'categorias':
            self.cursor.execute("UPDATE categorias SET Categoria = '%s' WHERE idCategoria = %s" % (self.valores["Categoria"], self.valores["id"]))

        elif self.tabla == 'favoritos':
            self.cursor.execute("UPDATE favoritos SET idReceta = %s, idUsuario = %s WHERE idFavorito = %s" % (self.valores["idReceta"], self.valores["idUsuario"], self.valores["id"]))

        elif self.tabla == 'usuarios':
            self.cursor.execute("UPDATE usuarios SET Nombre = '%s', Apellido = '%s',  Nacimiento = %s, correoElectronico = '%s', Hash = %s, Genero = '%s' WHERE idUsuario = %s" 
                % (self.valores["Nombre"], self.valores["Apellido"], self.valores["Nacimiento"], self.valores["correoElectronico"], self.valores["Hash"], self.valores["Genero"], self.valores["id"])) 
        else:
            print("Error, tabla ingresada, no válida")
        Credenciales.comitear(self)
    
    def imprimir(self): 
        if self.tabla == 'recetas':
            print("UPDATE recetas SET NombreReceta = '%s', Ingredientes = '%s', Receta = '%s',  Porciones = %s, urlImagen = '%s', TiempoMin = %s,idUsuario = %s, idCategoria = %s, dificultad = '%s' WHERE idReceta = %s" 
                % (self.valores["NombreReceta"], self.valores["Ingredientes"], self.valores["Receta"], self.valores["Porciones"], self.valores["urlImagen"], self.valores["TiempoMin"], self.valores["idUsuario"], self.valores["idCategoria"], self.valores["dificultad"], self.valores["id"])) 
            
        elif self.tabla == 'categorias':
            print("UPDATE categorias SET Categoria = '%s' WHERE idCategoria = %s" % (self.valores["Categoria"], self.valores["id"]))

        elif self.tabla == 'favoritos':
            print("UPDATE favoritos SET idReceta = %s, idUsuario = %s WHERE idFavorito = %s" % (self.valores["idReceta"], self.valores["idUsuario"], self.valores["id"]))

        elif self.tabla == 'usuarios':
            print("UPDATE usuarios SET Nombre = '%s', Apellido = '%s',  Nacimiento = %s, correoElectronico = '%s', Hash = %s, Genero = '%s' WHERE idUsuario = %s" 
                % (self.valores["Nombre"], self.valores["Apellido"], self.valores["Nacimiento"], self.valores["correoElectronico"], self.valores["Hash"], self.valores["Genero"], self.valores["id"])) 
        else:
            print("Error, tabla ingresada, no válida")
#
class EliminarDatos(Credenciales):

    def __init__(self, tabla,condicion):
        super().__init__()
        self.tabla = tabla
        self.condicion = condicion
    
    def borrar(self):
        self.conectar()

        # if not self.condicion:
        #     self.cursor.execute ("DELETE FROM %s" % (self.tabla,))
        # else:
        self.cursor.execute ("DELETE FROM %s WHERE %s" % (self.tabla,self.condicion,))
        Credenciales.comitear(self)

    def imprimir(self):
        # if not self.condicion:
        #     print("DELETE FROM %s" % (self.tabla,))
        # else:
        print("DELETE FROM %s WHERE %s" % (self.tabla,self.condicion,))       
#

print("\033[32m","#"*60,"\033[0m")

def reemplazosPagina(pagina):
    # Agregar esta función en cada @app.route que contenga un "return pagina"
    # Creación de estilos PROBABLEMENTE DEBA ELIMINARSE
    with open ('RecetasWebCAC23/formulariosweb/style.html', 'r', encoding='utf-8') as archivo:
        pagina = pagina.replace("{{style}}",archivo.read())
        archivo.close()
    
    # Carga de categorias en forma de lista
    categorias = Consulta('*','categorias')
    categorias.consultar()
    seleccion = ""
    
    
    for item in categorias.resultados:
        seleccion += f'''<option value="{item['Categoria']}">{item['Categoria']}</option>'''
    
    pagina = pagina.replace("{{opciones}}",seleccion)

    # Carrusel página principal

    seleccion = ""
    recetasNuevas = Consulta('*','recetas',False,"fechaCreacion")
    recetasNuevas.consultar()

    
    for item in recetasNuevas.resultados:
            for el in categorias.resultados:
                if el['idCategoria'] == item['idCategoria']:
                    categ = el['Categoria']
                    break
        
            seleccion += f'''<div class="item"><a href="/recetaid?={item['idReceta']}" class="a-hover"><div class="overlay-receta overlay-hover"></div><div class="receta-item"><div class="etiqueta-categoria"><a href="/recetaid?={item['idReceta']}" style="background-color: #8b84e5;" class="btn-etiqueta slide"><i class="fa fa-tag cat-dot" style="margin-right: 10px;"></i><span class="etiqueta-titulo">{categ}</span></a></div><div class="titulo-receta"><h3><a href="/buscar-receta-categoria?categoria={categ}">{item['Receta']}</a></h3></div><div class="fecha-tiempo"><span>{item['fechaCreacion']}</span><div class="separador-dot"></div><span><i class="fa fa-clock-o" aria-hidden="true" style="margin-right: 5px;"></i>{item['TiempoMin']} min</span></div></div><img src="{item['urlImagen']}" alt=""></a></div>'''
    pagina = pagina.replace("{{carrusel}}",seleccion)

    # Mostrar editar receta
    pagina = pagina.replace("{{receta}}","")
    pagina = pagina.replace("{{idReceta}}","")
    return pagina
#
def reemplazosReceta(pagina,idReceta):
    with open ('RecetasWebCAC23/formulariosweb/mostrarReceta.html', 'r', encoding='utf-8') as archivo:
        pagina = pagina.replace("{{receta}}",archivo.read())
        archivo.close()
    pagina = pagina.replace("{{idReceta}}",idReceta)
    elementos =("NombreReceta","Receta","Porciones","Ingredientes","urlImagen","TiempoMin","idUsuario","idCategoria","dificultad")

    receta = Consulta('*','recetas', f"idReceta = '{idReceta}'")
    receta.consultar()

    for elemento in elementos:
        reemplazo = "{{"+elemento+"}}"
        pagina = pagina.replace(reemplazo,str(receta.resultados[0][elemento]))
    return pagina
#
@app.route('/', methods=["GET"])
def inicial():
    data = request.args
    if data == {}:
        direccion = 'RecetasWebCAC23/index.html'
    else:
        direccion = f'RecetasWebCAC23/{data[""]}'

    f = open(direccion, 'r', encoding='utf-8')
    pagina = f.read()
    
    f.close()
    pagina = reemplazosPagina(pagina)
    return pagina
#
# Sección métodos POST
@app.route("/registro-receta", methods=["POST"])
def altaReceta():
    form = request.form
    pagina = ""
    cc = Credenciales()
    cc.conectar()

    text = f"""NombreUsuario = '{form["NombreUsuario"]}'"""
    cons = Consulta("idUsuario","usuarios",text)
    cons.consultar()

    categoria = Consulta('idCategoria','categorias', f"Categoria = '{form['categoria']}'")
    categoria.consultar()

    fecha_actual = datetime.now()
    fecha = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')
    columnas = "NombreReceta, Receta, Ingredientes, Porciones, urlImagen, TiempoMin, idUsuario, idCategoria, dificultad, fechaCreacion"
    # for elemento in form:
    #     print(elemento, form[elemento])
    # print(cons.resultados[0]['idUsuario'])
    # print(categoria.resultados[0]['idCategoria'])
    
    receta = f"""'{form["NombreReceta"]}','{form["Receta"]}','{form["Ingredientes"]}',{form["Porciones"]},'{form["urlImagen"]}',{form["TiempoMin"]},{cons.resultados[0]['idUsuario']},{categoria.resultados[0]['idCategoria']},'{form["dificultad"]}','{fecha}'"""
    registroReceta = CargaDatos("recetas", columnas, receta)
    registroReceta.insertarDato()
    
    cons = Consulta('*','recetas')
    cons.consultar()

    pagina += f'{registroReceta.imprimir()}'
    pagina += "<br>"
    pagina += "<hr>"
    pagina += receta
    pagina += f"{cons.resultados}"

    cc.desconectar()
    pagina = reemplazosPagina(pagina)
    return pagina
#
@app.route("/registro-usuario", methods=["POST"])
def altausuario():
    form = request.form
    pagina = ""
    cc = Credenciales()
    cc.conectar()
    
    hashContrasena = hashlib.sha256(form["Contrasena"].encode()).hexdigest()

    columnas = "NombreUsuario, Nombre, Apellido, Nacimiento, correoElectronico, Hash, Genero"
    usuario = f"""'{form["NombreUsuario"]}','{form["Nombre"]}','{form["Apellido"]}',{form["Nacimiento"]},'{form["correoElectronico"]}',{hashContrasena},'{form["Genero"]}'"""
    registroUsuario = CargaDatos("usuarios", columnas, usuario)
    registroUsuario.insertarDato()
    
    cons = Consulta('*','usuarios')
    cons.consultar()
    
    pagina += f'{registroUsuario.imprimir()}'
    pagina += "<br>"
    pagina += "<hr>"
    pagina += usuario
    pagina += f"{cons.resultados}"

    cc.desconectar()
    pagina = reemplazosPagina(pagina)
    return pagina
#
@app.route("/buscar-usuario", methods=['GET'])
def buscarUsuario():
    data = request.args

    columnas = "NombreUsuario, Nacimiento, correoElectronico, Genero"
    usuario = Consulta(columnas,'usuarios', f"NombreUsuario LIKE '%{data['nombreUsuario']}%'")
    usuario.consultar()
    # usuario.imprimir()
    pagina = f"{usuario.resultados}"
    
    pagina = reemplazosPagina(pagina)
    return pagina
#
@app.route("/buscar-receta", methods=['GET'])
def buscarReceta():
    data = request.args

    receta = Consulta('*','recetas', f"NombreReceta LIKE '%{data['NombreReceta']}%'")
    receta.consultar()

    pagina = f"{receta.resultados}"
    
    pagina = reemplazosPagina(pagina)
    return pagina
#
#Sección métods GET
@app.route("/recetaid", methods=['GET'])
def recetaId():
    data = request.args

    receta = Consulta('*','recetas', f"idReceta = '{data['']}'")
    receta.consultar()

    pagina = f"{receta.resultados}"
    
    pagina = reemplazosPagina(pagina)
    return pagina
#
@app.route("/buscar-receta-ingredientes", methods=['GET'])
def buscarIngrediente():
    data = request.args
    ingredientes = data['Ingredientes'].replace(" ","%")
    receta = Consulta('*','recetas', f"Ingredientes LIKE '%{ingredientes}%'")
    receta.consultar()

    pagina = f"{receta.resultados}"
    # pagina = f"{ingredientes}"
    pagina = reemplazosPagina(pagina)
    return pagina
#
@app.route("/buscar-receta-categoria", methods=['GET'])
def buscarRecetaCategoria():
    data = request.args

    categoria = Consulta('idCategoria','categorias', f"Categoria = '{data['categoria']}'")
    categoria.consultar()
    
    receta = Consulta('*','recetas', f"idCategoria= '{categoria.resultados[0]['idCategoria']}'")
    receta.consultar()

    pagina = f"{receta.resultados}"
    
    pagina = reemplazosPagina(pagina)
    return pagina
#
@app.route("/editar-receta", methods=['GET'])
def editarReceta():
    data = request.args

    receta = Consulta('*','recetas', f"idReceta = {data['idReceta']}")
    receta.consultar()
    # receta.imprimir()

    direccion = f'RecetasWebCAC23/formulariosWeb/modificarElementos.html'
    f = open(direccion, 'r', encoding='utf-8')
    pagina = f.read()
    
    if data['idReceta']:
        pagina = reemplazosReceta(pagina,data['idReceta'])

    pagina = reemplazosPagina(pagina)
    f.close()
    return pagina
#
@app.route("/edicion-receta", methods=['POST'])
def edicionReceta():
    form = request.form

    recetamod = ModificarDatos('recetas',form)
    recetamod.modificarDato()
    pagina="Receta modificada con éxito"
    return pagina
#
@app.route("/eliminar-receta", methods=['POST'])
def eliminarReceta():
    form = request.form


    recetamod = EliminarDatos('recetas',f"idReceta = '{form['id']}'")
    recetamod.imprimir()
    recetamod.borrar()
    pagina="Receta eliminada con éxito"
    return pagina

app.run(host='0.0.0.0', port=81) 

print("\033[31m","#"*60,"\033[0m")