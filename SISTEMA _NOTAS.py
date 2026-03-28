from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notas = []

@app.route("/")
def inicio():
    return render_template("notas.html", notas=notas)

@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    n1 = float(request.form["nota1"])
    n2 = float(request.form["nota2"])
    n3 = float(request.form["nota3"])

    promedio = (n1 + n2 + n3) / 3

    notas.append({
        "nombre": nombre,
        "nota1": n1,
        "nota2": n2,
        "nota3": n3,
        "promedio": round(promedio,2)
    })

    return redirect("/")

app.run(debug=True)