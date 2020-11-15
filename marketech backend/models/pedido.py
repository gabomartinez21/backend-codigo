from base_de_datos import base_de_datos
class PedidoModel(base_de_datos.Model):
    __tablename__="pedidos"
    id = base_de_datos.Column("id", base_de_datos.Integer, primary_key=True)
    id_usuario = base_de_datos.Column(base_de_datos.Integer, base_de_datos.ForeignKey('usuarios.id'), nullable=False)
    precio_total = base_de_datos.Column("precio_total", base_de_datos.Numeric)
    estado_pedido = base_de_datos.Column("estado_pedido", base_de_datos.String(50))
    creado_el = base_de_datos.Column("creado_el", base_de_datos.Datetime)
    actualizado_el = base_de_datos.Column("actualizado_el", base_de_datos.Datetime)
    estado = base_de_datos.Column(base_de_datos.Boolean, default=True)
    
    def __init__(self, estado):
        self.estado = estado

