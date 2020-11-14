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
        "apellido",
        type=str,
        required=True,
        help="Ingrese un apellido valido"
    )
    parser.add_argument(
        "fechadenacimiento",
        type=str,
        required=True,
        help="Ingrese una fecha de nacimiento valida"
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
        "avatar",
        type=str,
        required=False,
        help="Ingrese una imagen valida"
    )
    parser.add_argument(
        "direccion",
        type=str,
        required=True,
        help="Ingrese una direccion valida"
    )
    parser.add_argument(
        "fechadecreacion",
        type=date,
        required=False,
        help="La fecha de creacion no se agrego correctamente"
    )
    parser.add_argument(
        "fechadeactualizacion",
        type=date,
        required=False,
        help="La fecha de actualizacion no se agrego correctamente"
    )

    def post(self):
        data = self.parser.parse_args()

        nombre = data["nombre"]
        apellido = data["apellido"]
        fechadenacimiento = data["fechadenacimiento"]
        correo = data["correo"]
        contrasena = data["contrasena"]
        telefono = data["telefono"]
        descripcion = data["descripcion"]
        sexo = data["sexo"]
        avatar = data["avatar"]
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
            nuevousuario = UsuarioModel(nombre,apellido,fechadenacimiento,correo,contrasena,telefono,descripcion,sexo,avatar,direccion,date.today(),date.today())

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
        print(usuariousandolaaplicacion.nombre)

        if usuariousandolaaplicacion:
            return {
                "ok":True,
                "content": usuariousandolaaplicacion.mostrar_como_json(),
                "message": "el usuario fue obtenido exitosamente"
            },200
        else:
            return {
                "ok":False,
                "content": None,
                "message": "el usuario con el nombre {} no fue encontrado".format(nombre)
            },404

class InformaciondeUsuario(Resource):
    
    def put(self,nombre):
        usuarioparaactualizar = UsuarioModel.query.filter_by(nombre=nombre).first()
        print(usuarioparaactualizar.nombre)
        
        if usuarioparaactualizar:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "nombre",
                type=str,
                required=True,
                help="Ingrese un nombre valido"
            )
            parser.add_argument(
                "apellido",
                type=str,
                required=True,
                help="Ingrese un apellido valido"
            )
            parser.add_argument(
                "fechadenacimiento",
                type=str,
                required=True,
                help="Ingrese una fecha de nacimiento valida"
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
                "avatar",
                type=str,
                required=False,
                help="Ingrese una imagen valida"
            )
            parser.add_argument(
                "direccion",
                type=str,
                required=True,
                help="Ingrese una direccion valida"
            )
            parser.add_argument(
                "fechadeactualizacion",
                type=str,
                required=False,
                help="La fecha de actualizacion no se agrego correctamente"
            )

            data = parser.parse_args()
            usuarioparaactualizar.nombre = data["nombre"]
            usuarioparaactualizar.apellido = data["apellido"]
            usuarioparaactualizar.fechadenacimiento = data["fechadenacimiento"]
            usuarioparaactualizar.correo = data["correo"]
            usuarioparaactualizar.contrasena = data["contrasena"]
            usuarioparaactualizar.telefono = data["telefono"]
            usuarioparaactualizar.descripcion = data["descripcion"]
            usuarioparaactualizar.sexo = data["sexo"]
            usuarioparaactualizar.avatar = data["avatar"]
            usuarioparaactualizar.direccion = data["direccion"]
            usuarioparaactualizar.fechadeactualizacion = date.today()
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





    

