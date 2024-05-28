from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return {
    'message': 'hola, Mundo!!!'
  }
"""correr un comando en lenguaje python que permita listar objetos
  en /storage/<uid>

  incluir /public/ que permite listar los archivos del contenedor <uid>

  incluir /download/<name.ext> que permite descargar el archivo <name.ext>


  /upload/<uid>/<name.ext> que permite enviar un archivo al contenedor <uid>
@app.route('/despedirse')
def bye_world():
  return {
    'message': 'Adiós, mundo!!!'
  }


app.run()
