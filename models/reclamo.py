from base_de_datos import base_de_datos

class ReclamoModel(base_de_datos.Model):
    __tablename__="reclamos"
    id = base_de_datos.Column("id", base_de_datos.Integer, primary_key=True)
    id_cliente = base_de_datos.Column("id", base_de_datos.Integer, base_de_datos.ForeignKey('usuarios.id'), nullable=False)
    id_producto = base_de_datos.Column("id", base_de_datos.Integer, base_de_datos.ForeignKey('productos.id'), nullable=False)
    mensaje = base_de_datos.Column("id", base_de_datos.String(255), nullable=False)
    fechadecreacion = base_de_datos.Column("id", base_de_datos.Date, nullable=False)
    fechadeactualizacion = base_de_datos.Column("id", base_de_datos.Date, nullable=False)

    def __init__(self, id_cliente, id_producto, mensaje, fechadecreacion, fechadeactualizacion):
        self.id_cliente = id_cliente
        self.id_producto = id_producto
        self.mensaje = mensaje
        self.fechadecreacion = fechadecreacion
        self.fechadeactualizacion = fechadeactualizacion

    def guardarDB(self):
        base_de_datos.session.add(self)
        base_de_datos.session.commit()
    
    def mostrar_como_json(self):
        return {
            "id": self.id,
            "id_cliente": self.id_cliente,
            "id_producto": self.id_producto,
            "mensaje": self.mensaje
        }

