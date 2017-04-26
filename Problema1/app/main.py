from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

#Funcion que toma el inicio del programa para posterior redirigir hacia al inicio para nuevos accesos

@app.route('/calculadora', methods = ['POST'])
def calculadora():
    '''
    Funcion donde se da inicio al calculo de comisiones, que igualmente contendrá el valor de cada comisión

    '''
    if request.method == 'POST':
        '''variables de index.html'''
        nom = request.form['nom']
        ventas = float(request.form['ventas'])
        if ventas < 25000:

               #Se utiliza el rango por comision y se asigna la comision me


            comision = ventas * (3/100)
        elif ventas >= 25000 and ventas < 50000:
            comision  = ventas * (5/100)
        elif ventas >= 50000 and ventas < 75000:
            comision = ventas * (7/100)
        elif ventas >= 75000 and ventas < 100000:
            comision = ventas * (10/100)
        elif ventas >= 100000:
            comision = ventas * (15/100)
        guardar = "%s, %4.2f, %4.2f" %(nom, ventas, comision)
        report = open("report.csv", "a+")

           #Funcion donde se crea el documenta que guardara datos ingresados y calculados


        report.write(guardar + "\n")
        report.close()
    return render_template('calculadora.html', n=nom , c = comision)

@app.route('/cortex', methods = ['POST'])
def cortex():
    if request.method == 'POST':
        return redirect(url_for("inicio"))

    #Funcion donde se puede redirigir al inicio del programa


if __name__ == "__main__":
    app.run(debug=True)
