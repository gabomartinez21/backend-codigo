from flask_restful import Resource, reqparse
from models.usuario import ReclamoModel
from models.usuario import UsuarioModel
from models.producto import ProductoModel
from datetime import date
class AgregarReclamo(Resourse):

    parser = reqparse.RequestParser()
    parser.add_request(
        "id_cliente",
        type=int,
        required=True,
        help="Ingrese un ID de cliente valido"
    )
    parser.add_request(
        "id_producto",
        type=int,
        required=True,
        help="Ingrese un ID de producto valido"
    )
    parser.add_request(
        "mensaje",
        type=str,
        required=True,
        help="Ingrese mensaje del reclamo"
    )
    parser.add_request(
        "fechadecreacion",
        type=date,
        required=False,
        help="La fecha de creacion no se agrego correctamente"
    )
    parser.add_request(
        "fechadeactualizacion",
        type=date,
        required=False,
        help="La fecha de actualización no se agrego correctamente"
    )

    def get(self, id_reclamo):
        reclamo = ReclamoModel.query.filter_by(id=id_reclamo).first()
        informacion = reclamo.mostrar_json()
        if reclamo:
            return {
                'ok':True,
                'content':informacion,
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el reclamo.'
            }, 404

    def post(self):
        data = self.parser.parse_args()

        id_cliente = data['id_cliente']
        id_producto = data['id_producto']
        mensaje = data['mensaje']

        reclamo = ReclamoModel(id_cliente, id_producto, mensaje, date.today(),date.today())
        print(reclamo)

        try:
            reclamo.guardarDB()
            return {
                'ok':True,
                'message':'El reclamo se guardó exitosamente.',
                'content': reclamo.mostrar_como_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el reclamo.'
            },500

