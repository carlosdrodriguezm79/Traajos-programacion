from flask import Flask, render_template, request, redirect

app = Flask(__name__)

estudiantes = []

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    edad = request.form["edad"]

    estudiantes.append({
        "nombre": nombre,
        "edad": edad
    })

    return redirect("/lista")

@app.route("/lista")
def lista():
    return render_template("lista.html", estudiantes=estudiantes)

app.run(debug=True)