from base_datos import db
class PedidoModel(db.Model):
    __tablename__="pedidos"
    id = db.Column("id", db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    precio_total = db.Column("precio_total", db.Numeric)
    estado_pedido = db.Column("estado_pedido", db.String(50))
    creado_el = db.Column("creado_el", db.Datetime)
    actualizado_el = db.Column("actualizado_el", db.Datetime)
    estado = db.Column(db.Boolean, default=True)
    
    def __init__(self, estado):
        self.estado = estado

