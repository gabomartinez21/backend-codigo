from base_de_datos import base_de_datos

class UsuarioModel(base_de_datos.Model):
    __tablename__="Usuarios"
    id = base_de_datos.Column("id",base_de_datos.Integer,primary_key=True)
    nombre = base_de_datos.Column("nombre",base_de_datos.String(225),nullable=False)
    apellido = base_de_datos.Column("apellido",base_de_datos.String(225),nullable=False)
    fechadenacimiento = base_de_datos.Column("fechadenacimiento",base_de_datos.Date,nullable=False)
    correo = base_de_datos.Column("correo",base_de_datos.String(225),nullable=False)
    contrasena = base_de_datos.Column("contrasena",base_de_datos.String(225),nullable=False)
    telefono = base_de_datos.Column("telefono",base_de_datos.Integer,nullable=False)
    descripcion = base_de_datos.Column("descripcion",base_de_datos.Text,nullable=False)
    sexo = base_de_datos.Column("sexo",base_de_datos.String(50),nullable=False)
    avatar = base_de_datos.Column("avatar",base_de_datos.String(225),nullable=False)
    direccion = base_de_datos.Column("direccion",base_de_datos.String(225),nullable=False)
    fechadecreacion = base_de_datos.Column("fechadecreacion",base_de_datos.Date,nullable=False)
    fechadeactualizacion = base_de_datos.Column("fechadeactualizacion",base_de_datos.Date,nullable=False)

    def __init__(self,nombre,apellido,fechadenacimiento,correo,contrasena,telefono,descripcion,sexo,avatar,direccion,fechadecreacion,fechadeactualizacion):
        self.nombre = nombre
        self.apellido = apellido
        self.fechadenacimiento = fechadenacimiento
        self.correo = correo
        self.contrasena = contrasena
        self.telefono = telefono
        self.descripcion = descripcion
        self.sexo = sexo
        self.avatar = avatar
        self.direccion = direccion
        self.fechadecreacion = fechadecreacion
        self.fechadeactualizacion = fechadeactualizacion
    