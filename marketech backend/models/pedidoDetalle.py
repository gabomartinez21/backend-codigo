from base_de_datos import base_de_datos
class PedidoDetalleModel(base_de_datos.Model):
    __tablename__="pedido_detalle"
    id = base_de_datos.Column("id", base_de_datos.Integer, primary_key=True)
    id_pedido = base_de_datos.Column(base_de_datos.Integer, base_de_datos.ForeignKey('pedidos.id'), nullable=False)
    id_producto = base_de_datos.Column(base_de_datos.Integer, base_de_datos.ForeignKey('productos.id'), nullable=False)
    cantidad = base_de_datos.Column("cantidad", base_de_datos.Integer, nullable=False)
    subtotal = base_de_datos.Column("subtotal", base_de_datos.Numeric)
    estado_pedido = base_de_datos.Column("estado_pedido", base_de_datos.String(50))
    creado_el = base_de_datos.Column("creado_el", base_de_datos.Datetime, base_de_datos.datetime.datetime.utcnow)
    actualizado_el = base_de_datos.Column("actualizado_el", base_de_datos.Datetime)
    estado = base_de_datos.Column(base_de_datos.Boolean, default=True)
    
    def __init__(self, estado):
        self.estado = estado

