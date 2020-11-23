from flask import Flask, render_template, request

app = Flask(__name__)

#rutas
@app.route('/') #significa ruta raiz
def index():
    return render_template('index.html')

@app.route('/saludo/<nombre>/<int:edad>')
def saludar(nombre,edad):

    numeros=[1,2,3,4,5,6,7,8,9]
    return render_template('saludo.html',name=nombre, age=edad, numbers=numeros)

@app.route('/contacto', methods=['GET','POST'])
def contacto():
    #obteniendo formulario de contanto
    if request.method == 'GET':
        return render_template('contacto.html')

    #guardando la informacion de contacto
    nombres = request.form.get('nombres')
    email = request.form.get('email')
    celular = request.form.get('celular')
    observacion = request.form.get('observacion')

    return 'guardando informacion'+ nombres, email, celular, observacion

@app.route('/sumar')
def sumar():
    resultado = 2+2
    return 'la suma de 2+2=' + str(resultado)

app.run(debug=True)