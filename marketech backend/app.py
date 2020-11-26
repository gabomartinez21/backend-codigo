from flask import Flask
from flask_restful import Api
from base_de_datos import base_de_datos
from controllers.usuario import IniciodeSesion,CrearCuenta,BusquedadeUsuario,InformaciondeUsuario

from models.usuario import UsuarioModel
from models.categoria import CategoriaModel
from models.producto import ProductoModel
from controllers.producto import ProductosController, ProductoController

from models.reclamo import ReclamoModel
from controllers.reclamo import ReclamoController

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/marketech'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://romario:innovahora@localhost:3303/marketech'
api = Api(app=app)

@app.before_first_request
def creartablas():
    base_de_datos.init_app(app)
    base_de_datos.create_all(app=app)


@app.route("/")
def rutainical():
    return "El Servidor de Marketech esta corriendo exitosamente"

api.add_resource(CrearCuenta,"/crearcuenta")
api.add_resource(IniciodeSesion,"/iniciarsesion")
api.add_resource(BusquedadeUsuario,"/usuario/<string:nombre>")
api.add_resource(InformaciondeUsuario,"/informacion/usuario/<int:id_usuario>")

api.add_resource(ProductosController,'/productos')
api.add_resource(ProductoController, '/producto/<int:id_producto>')

api.add_resource(ReclamoController, '/reclamo')

if __name__ == "__main__":
    app.run(debug=True)
