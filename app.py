from flask import Flask, render_template

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/saludo/<nombre>/<int:edad>')
def saludar(nombre, edad):
    numeros=[1,2,3,4,5,6,7,8,9]
    return  render_template('saludo.html', name=nombre, age=edad, numbers=numeros)

@app.route('/contacto')
def contacto():
    return 'en la pagina de contacto'

@app.route('/sumar')
def sumar():
    resultado = 2+2
    return 'suma de 2+2='+ str(resultado)

app.run(debug=True)