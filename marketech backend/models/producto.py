from base_datos import db
class ProductoModel(db.Model):
    __tablename__="productos"
    id = db.Column("id",db.Integer, primary_key=True, auto_increment=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    imagen = db.Column("imagen", db.String(255), nullable=False)
    nombre = db.Column("nombre", db.String(255), nullable=False)
    descripcion = db.Column("descripcion", db.Text, nullable=False)
    stock = db.Column("stock", db.Integer, nullable=False)
    precio = db.Column("precio", db.Numeric)
    precio_oferta = db.Column("precio_oferta", db.Numeric)
    creado_el = db.Column("creado_el", db.DateTime, default=db.func.current_timestamp())
    actualizado_el = db.Column("actualizado_el", db.DateTime)
    estado = db.Column(db.Boolean, default=True)

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
        db.session.add(self)
        db.session.commit()

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