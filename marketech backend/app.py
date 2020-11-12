from flask import Flask
from flask_restful import Api
from base_de_datos import base_de_datos
from models.usuario import UsuarioModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/marketech'
api = Api(app=app)

@app.before_first_request
def creartablas():
    base_de_datos.init_app(app)
    base_de_datos.create_all(app=app)


@app.route("/")
def rutainical():
    return "El Servidor de Marketech esta corriendo exitosamente"

if __name__ == "__main__":
    app.run(debug=True)
