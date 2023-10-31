from flask import Flask, render_template, send_from_directory
from flask_swagger import swagger

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    Pagina de inicio de la API.

    Esta es la pagina de inicio de la API que devuelve un saludo simple.

    ---
    responses:
      200:
        description: Saludo exitoso
    """
    return "Hello friend!"


@app.route("/users", methods=["GET"])
def get_users() -> dict:
    """
    Obtiene la lista de usuarios.

    Este endpoint devuelve una lista de usuarios.

    ---
    responses:
      200:
        description: Lista de usuarios exitosa
    """
    return {"users": ["Pablo", "Jesús", "Rodolfo"]}


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id) -> dict:
    """
    Obtiene un usuario por ID.

    Este endpoint devuelve un usuario por su ID.

    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del usuario a obtener

    responses:
      200:
        description: Usuario encontrado
      404:
        description: Usuario no encontrado
    """
    return {"user": {"id": id, "name": "Pablo"}}


# Ruta para servir la interfaz de usuario de Swagger-UI
@app.route("/dist/<path:filename>")
def serve_static(filename):
    return send_from_directory("dist", filename)


@app.route("/apidocs")
# Endpoint para la documentación Swagger
def apidocs() -> dict:
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "User test API"
    return swag


@app.route("/swagger")
# Ruta para servir la interfaz de usuario de Swagger-UI
def swagger_ui():
    return render_template("swagger.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
