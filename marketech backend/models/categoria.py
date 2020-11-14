from base_de_datos import base_de_datos
class CategoriaModel(base_de_datos.Model):
    __tablename__="categorias"
    id = base_de_datos.Column("id",base_de_datos.Integer, primary_key=True)
    nombre = base_de_datos.Column("nombre", base_de_datos.String(255), nullable=False)
    creado_el = base_de_datos.Column("creado_el", base_de_datos.DateTime)
    actualizado_el = base_de_datos.Column("actualizado_el", base_de_datos.DateTime)
    estado = base_de_datos.Column(base_de_datos.Boolean, default=True)

    def __init__(self, nombre):
        self.nombre = nombre
    
    def guardar_bd(self):
        base_de_datos.session.add(self)
        base_de_datos.session.commit()
    
    def mostrar_json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'estado': self.estado
        }
    def __str__(self):
        return '%s, %s'%(self.id, self.nombre)