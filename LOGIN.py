from flask import Flask, render_template, request

app = Flask(__name__)

usuario_correcto = "admin"
password_correcto = "1234"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/validar", methods=["POST"])
def validar():

    usuario = request.form["usuario"]
    password = request.form["password"]

    if usuario == usuario_correcto and password == password_correcto:
        return render_template("panel.html", usuario=usuario)

    else:
        return "Usuario o contraseña incorrectos"

app.run(debug=True)