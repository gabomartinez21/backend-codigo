from base_datos import db
class PedidoDetalleModel(db.Model):
    __tablename__="pedido_detalle"
    id = db.Column("id", db.Integer, primary_key=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column("cantidad", db.Integer, nullable=False)
    subtotal = db.Column("subtotal", db.Numeric)
    estado_pedido = db.Column("estado_pedido", db.String(50))
    creado_el = db.Column("creado_el", db.Datetime, db.datetime.datetime.utcnow)
    actualizado_el = db.Column("actualizado_el", db.Datetime)
    estado = db.Column(db.Boolean, default=True)
    
    def __init__(self, estado):
        self.estado = estado

