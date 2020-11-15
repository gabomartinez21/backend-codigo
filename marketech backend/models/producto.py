from base_de_datos import base_de_datos
class ProductoModel(base_de_datos.Model):
    __tablename__="productos"
    id = base_de_datos.Column("id",base_de_datos.Integer, primary_key=True)
    id_categoria = base_de_datos.Column(base_de_datos.Integer, base_de_datos.ForeignKey('categorias.id'), nullable=False)
    id_usuario = base_de_datos.Column(base_de_datos.Integer, base_de_datos.ForeignKey('usuarios.id'), nullable=False)
    imagen = base_de_datos.Column("imagen", base_de_datos.String(255), nullable=False)
    nombre = base_de_datos.Column("nombre", base_de_datos.String(255), nullable=False)
    descripcion = base_de_datos.Column("descripcion", base_de_datos.Text, nullable=False)
    stock = base_de_datos.Column("stock", base_de_datos.Integer, nullable=False)
    precio = base_de_datos.Column("precio", base_de_datos.Numeric)
    precio_oferta = base_de_datos.Column("precio_oferta", base_de_datos.Numeric)
    creado_el = base_de_datos.Column("creado_el", base_de_datos.DateTime, default=base_de_datos.func.current_timestamp())
    actualizado_el = base_de_datos.Column("actualizado_el", base_de_datos.DateTime)
    estado = base_de_datos.Column(base_de_datos.Boolean, default=True)

    def __init__(self, id_categoria, id_usuario, imagen, nombre, descripcion, stock, precio, precio_oferta):
        self.id_categoria = id_categoria
        self.id_usuario = id_usuario
        self.imagen = imagen
        self.nombre = nombre
        self.descripcion = descripcion
        self.stock = stock
        self.precio = precio
        self.precio_oferta = precio_oferta
    
    def guardar_bd(self):
        base_de_datos.session.add(self)
        base_de_datos.session.commit()

    def mostrar_json(self):
        return {
            'id':self.id,
            'id_categoria':self.id_categoria,
            'id_usuario': self.id_usuario,
            'imagen':self.imagen,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'stock':self.stock,
            'precio':float(self.precio),
            'precio_oferta':float(self.precio_oferta),
            'estado':self.estado,
        }