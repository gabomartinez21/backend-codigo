from flask_restful import Resource,reqparse
from models.usuario import UsuarioModel
from datetime import date

class IniciodeSesion(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "nombre",
            type=str,
            required=True,
            help="Ingrese un nombre valido"
        )
        parser.add_argument(
            "correo",
            type=str,
            required=True,
            help="Ingrese un correo valido"
        )
        parser.add_argument(
            "contrasena",
            type=str,
            required=True,
            help="ingrese una contrasena valida"
        )

        data = parser.parse_args()
        nombre = data["nombre"]
        correo = data["correo"]
        contrasena = data["contrasena"]

        nombre_usuario = UsuarioModel.query.filter_by(nombre=nombre).first()
        correo_usuario = UsuarioModel.query.filter_by(correo=correo).first()
        contrasena_usuario = UsuarioModel.query.filter_by(contrasena=contrasena).first()

        if nombre_usuario and correo_usuario and contrasena_usuario:
            return {
                "ok": True,
                "content": nombre_usuario.mostrar_como_json(),
                "message": "El usuario {} fue encontrado exitosamente y se puede iniciar sesion".format(nombre)
            },200
        else:
            return {
                "ok": True,
                "content": None,
                "message": "El usuario con el nombre {}, con el correo {} y con la contrasena {} no existe o no se logro encontrar".format(nombre,correo,contrasena)
            },404

class CrearCuenta(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "nombre",
        type=str,
        required=True,
        help="Ingrese un nombre valido"
    )
    parser.add_argument(
        "apellido_paterno",
        type=str,
        required=True,
        help="Ingrese un apellido valido"
    )
    parser.add_argument(
        "apellido_materno",
        type=str,
        required=True,
        help="Ingrese un apellido valido"
    )
    parser.add_argument(
        "correo",
        type=str,
        required=True,
        help="Ingrese un correo valido"
    )
    parser.add_argument(
        "contrasena",
        type=str,
        required=True,
        help="Ingrese una contrasena valida"
    )
    parser.add_argument(
        "telefono",
        type=int,
        required=True,
        help="Ingrese un telefono valido"
    )
    parser.add_argument(
        "descripcion",
        type=str,
        required=True,
        help="Ingrese una descripcion valida"
    )
    parser.add_argument(
        "sexo",
        type=str,
        required=True,
        help="Ingrese un sexo valido"
    )
    parser.add_argument(
        "direccion",
        type=str,
        required=True,
        help="Ingrese una direccion valida"
    )

    def post(self):
        data = self.parser.parse_args()

        nombre = data["nombre"]
        apellido_paterno = data["apellido_paterno"]
        apellido_materno = data["apellido_materno"]
        correo = data["correo"]
        contrasena = data["contrasena"]
        telefono = data["telefono"]
        descripcion = data["descripcion"]
        sexo = data["sexo"]
        direccion = data["direccion"]

        verificadordenombre = UsuarioModel.query.filter_by(nombre=nombre).first()
        verificadordecorreo = UsuarioModel.query.filter_by(correo=correo).first()
        verificadordetelefono = UsuarioModel.query.filter_by(telefono=telefono).first()

        if verificadordenombre and verificadordecorreo and verificadordetelefono:
            return {
                "ok": False,
                "content": None,
                "message": "el nombre y el correo ingresado ya estan en uso"
            }
        
        elif verificadordenombre:
            return {
                "ok": False,
                "content": None,
                "message": "el nombre ingresado ya esta en uso"
            }
        
        elif verificadordecorreo:
            return {
                "ok": False,
                "content": None,
                "message": "el correo ingresado ya esta en uso"
            }

        elif verificadordetelefono:
            return {
                "ok": False,
                "content": None,
                "message": "el telefono ingresado ya esta en uso"
            }

        else:
            nuevousuario = UsuarioModel(nombre,apellido_paterno, apellido_materno,correo,contrasena,telefono,descripcion,sexo,direccion)

            try:
                nuevousuario.guardar_en_la_basededatos()
                print(nuevousuario)
                return {
                    "ok": True,
                    "content": nuevousuario.mostrar_como_json(),
                    "message":"el usuario fue agregado a la base de datos exitosamente"
                },201
            except:
                    return{
                        "ok": False,
                        "content": None,
                        "message": "Ocurrio un error al guardar el usuario en la base de datos"
                    },500

class BusquedadeUsuario(Resource):

    def get(self,nombre):
        usuariousandolaaplicacion = UsuarioModel.query.filter_by(nombre=nombre).first()
        #usuariousandolaaplicacion = UsuarioModel.query.filter(UsuarioModel.nombre.like("%{}%".format(nombre))).all()
        #Category.query.filter(Category.title.like(category_param_value + "%")).all()

        if usuariousandolaaplicacion:
            return {
                "ok":True,
                "content": usuariousandolaaplicacion.mostrar_como_json(),
                "message": "Usuario obtenido exitosamente."
            },200
        else:
            return {
                "ok":False,
                "content": None,
                "message": "No hubo resultados."
            },404

class InformaciondeUsuario(Resource):
    
    def put(self,id_usuario):
        usuarioparaactualizar = UsuarioModel.query.filter_by(id=id_usuario).first()
        
        if usuarioparaactualizar:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "nombre",
                type=str,
                required=True,
                help="Ingrese un nombre valido"
            )
            parser.add_argument(
                "apellido_paterno",
                type=str,
                required=True,
                help="Ingrese un apellido paterno valido"
            )
            parser.add_argument(
                "apellido_materno",
                type=str,
                required=True,
                help="Ingrese un apellido paterno valido"
            )
            parser.add_argument(
                "correo",
                type=str,
                required=True,
                help="Ingrese un correo valido"
            )
            parser.add_argument(
                "contrasena",
                type=str,
                required=True,
                help="Ingrese una contrasena valida"
            )
            parser.add_argument(
                "telefono",
                type=int,
                required=True,
                help="Ingrese un telefono valido"
            )
            parser.add_argument(
                "descripcion",
                type=str,
                required=True,
                help="Ingrese una descripcion valida"
            )
            parser.add_argument(
                "sexo",
                type=str,
                required=True,
                help="Ingrese un sexo valido"
            )
            parser.add_argument(
                "direccion",
                type=str,
                required=True,
                help="Ingrese una direccion valida"
            )

            data = parser.parse_args()
            usuarioparaactualizar.nombre = data["nombre"]
            usuarioparaactualizar.apellido_paterno = data["apellido_paterno"]
            usuarioparaactualizar.apellido_materno = data["apellido_materno"]
            usuarioparaactualizar.correo = data["correo"]
            usuarioparaactualizar.contrasena = data["contrasena"]
            usuarioparaactualizar.telefono = data["telefono"]
            usuarioparaactualizar.descripcion = data["descripcion"]
            usuarioparaactualizar.sexo = data["sexo"]
            usuarioparaactualizar.direccion = data["direccion"]
            usuarioparaactualizar.guardar_en_la_basededatos()

            return {
                "ok": True,
                "content": usuarioparaactualizar.mostrar_como_json(),
                "message": "el usuario {} fue actualizado exitosamente".format(usuarioparaactualizar.nombre)
            }

        else:
            return {
                "ok": False,
                "content": None,
                "message": "el usuario con el nombre {} no fue encontrado".format(usuarioparaactualizar.nombre)
            }





    

