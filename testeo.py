
from flask import Flask, request
app = Flask(__name__)

print("\033[32m","#"*60,"\033[0m")

@app.route("/")
def inicial():
    f = open('index.html', 'r')
    pagina = f.read()
    f.close()
    return pagina

@app.route("/")#, methods=["POST"])
def process():
    pagina = "Llegué" # COLOCAR LINK A PLANTILLA DEL registro
    
    
    return pagina
    
app.run(host='0.0.0.0', port=81) #Debe ir siempre al final

print("\033[31m","#"*60,"\033[0m")