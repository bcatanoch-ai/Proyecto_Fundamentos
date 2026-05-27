# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Credenciales de acceso para la validación
USUARIO_CORRECTO = "Bryan"
PASSWORD_CORRECTO = "1234"

@app.route("/")
def index():
    """Ruta Principal: Lee y muestra el archivo 'index.html' (la tienda) de la carpeta templates."""
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Ruta del Login: Lee 'login.html' de templates y procesa el formulario."""
    mensaje = ""
    clase = ""

    if request.method == "POST":
        # Captura los datos que el usuario ingresa en tu formulario HTML
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        # Validación lógica de credenciales de acceso
        if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTO:
            mensaje = "✅ Autenticación exitosa. ¡Bienvenido Bryan!"
            clase = "correcto"
        else:
            mensaje = "❌ Usuario o contraseña incorrectos"
            clase = "incorrecto"

    # Envía las variables 'mensaje' y 'clase' directamente a tu archivo login.html
    return render_template(
        "login.html",
        mensaje=mensaje,
        clase=clase
    )


if __name__ == "__main__":
    # Inicia el servidor web local de Flask en el puerto 8080
    app.run(host="0.0.0.0", port=8080, debug=True)
