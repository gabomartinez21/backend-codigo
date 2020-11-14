from flask_restful import Resource, reqparse
from models.producto import ProductoModel

class ProductosController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "id_categoria",
        type=str,
        required=True,
        help="Falta seleccionar la categoría del producto"
    )
    parser.add_argument(
        "id_usuario",
        type=str,
        required=True,
        help="Falta seleccionar al usuario que publicó el producto"
    )
    parser.add_argument(
        "imagen",
        type=str,
        required=True,
        help="Falta subir una imagen para mostrar el producto"
    )
    parser.add_argument(
        "nombre",
        type=str,
        required=True,
        help="Falta ingresar el nombre del producto"
    )
    parser.add_argument(
        "descripcion",
        type=str,
        required=True,
        help="Falta ingresar la descripcion del producto"
    )
    parser.add_argument(
        "stock",
        type=int,
        required=True,
        help="Falta ingresar el stock del producto"
    )
    parser.add_argument(
        "precio",
        type=float,
        required=True,
        help="Falta ingresar el precio del producto"
    )
    parser.add_argument(
        "precio_oferta",
        type=float,
        required=True,
        help="Falta ingresar el precio de oferta del producto"
    )
    def get(self):
        productos = ProductoModel.query.all()
        resultado = []
        for producto in productos:
            # print(libro)
            temporal = producto.mostrar_json()
            # temporal['estante'] = producto.estante.mostrar_json()
            resultado.append(temporal)
            # print(producto.estante.mostrar_json())
            # print(libro.est_id)
        return {
            'ok':True,
            'content':resultado
        }
    def post(self):
        data = self.parser.parse_args()
        producto = ProductoModel(data['id_categoria'], data['id_usuario'], data['imagen'],data['nombre'],data['descripcion'], data['stock'], data['precio'], data['precio_oferta'])
        producto.guardar_bd()
        return {
            'ok':True,
            'message':'El producto se guardó exitosamente.',
            'content': producto.mostrar_json()
        }
        try:
            producto.guardar_bd()

            return {
                'ok':True,
                'message':'El producto se guardó exitosamente.',
                'content': producto.mostrar_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el producto.'
            },500

class ProductoController(Resource):
    def get(self, id_producto):
        producto = ProductoModel.query.filter_by(id=id_producto).first()
        informacion = producto.mostrar_json()
        if producto:
            return {
                'ok':True,
                'content':informacion,
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el producto.'
            }, 404

    def put(self, id_producto):
        producto = ProductoModel.query.filter_by(id=id_producto).first()
        if producto:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "id_categoria",
                type=str,
                required=True,
                help="Falta seleccionar la categoría del producto"
            )
            parser.add_argument(
                "id_usuario",
                type=str,
                required=True,
                help="Falta seleccionar al usuario que publicó el producto"
            )
            parser.add_argument(
                "imagen",
                type=str,
                required=True,
                help="Falta subir una imagen para mostrar el producto"
            )
            parser.add_argument(
                "nombre",
                type=str,
                required=True,
                help="Falta ingresar el nombre del producto"
            )
            parser.add_argument(
                "descripcion",
                type=str,
                required=True,
                help="Falta ingresar la descripcion del producto"
            )
            parser.add_argument(
                "stock",
                type=int,
                required=True,
                help="Falta ingresar el stock del producto"
            )
            parser.add_argument(
                "precio",
                type=float,
                required=True,
                help="Falta ingresar el precio del producto"
            )
            parser.add_argument(
                "precio_oferta",
                type=float,
                required=True,
                help="Falta ingresar el precio de oferta del producto"
            )

            data = parser.parse_args()
            producto.id_categoria = data['id_categoria']
            producto.id_usuario = data['id_usuario']
            producto.imagen = data['imagen']
            producto.nombre = data['nombre']
            producto.descripcion = data['descripcion']
            producto.stock = data['stock']
            producto.precio = data['precio']
            producto.precio_oferta = data['precio_oferta']

            producto.guardar_bd()

            return {
                'ok':True,
                'content':producto.mostrar_json(),
                'message':None
            }

        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el producto.'
            }

    def delete(self, id_producto):
        producto = ProductoModel.query.filter_by(id=id_producto).first()
        if producto:
            if producto.estado == 1:
                producto.estado = 0
                producto.guardar_bd()
                return {
                    'ok':True,
                    'content':None,
                    'message':'El producto fue eliminado correctamente.'
                }
            else:
                return {
                    'ok':False,
                    'content':None,
                    'message':'El producto ya se encuentra eliminado.'
                }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el producto.'
            }, 400

class EncontrarLibroController(Resource):
    def get(self, palabra):
        resultado = LibroModel.query.filter(LibroModel.nombre.like('%'+palabra+'%')).all()
        if resultado:
            respuesta = []
            for libro in resultado:
                respuesta.append(libro.mostrar_json())
            return{
                'Ok':True,
                'content':respuesta,
                'message':''
            }
        else:
            return{
                'Ok':False,
                'content':None,
                'message':'No se encontro ninguna coincidencia'
            }, 404