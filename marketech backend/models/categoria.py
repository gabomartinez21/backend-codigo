from base_datos import db
class CategoriaModel(db.Model):
    __tablename__="categorias"
    id = db.Column("id",db.Integer, primary_key=True)
    nombre = db.Column("nombre", db.String(255), nullable=False)
    creado_el = db.Column("creado_el", db.DateTime)
    actualizado_el = db.Column("actualizado_el", db.DateTime)
    estado = db.Column(db.Boolean, default=True)

    def __init__(self, nombre):
        self.nombre = nombre
    
    def guardar_bd(self):
        db.session.add(self)
        db.session.commit()
    
    def mostrar_json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'estado': self.estado
        }
    def __str__(self):
        return '%s, %s'%(self.id, self.nombre)