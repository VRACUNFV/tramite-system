from flask import Blueprint, request, jsonify
from .models import db, Usuario, Tramite, Alerta, Historico, Chat

api = Blueprint('api', __name__)

@api.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@api.route('/tramites', methods=['POST'])
def create_tramite():
    data = request.get_json()
    nuevo_tramite = Tramite(
        nt=data['nt'],
        ano=data['ano'],
        responsable_id=data['responsable_id'],
        estado='Pendiente',
        fecha_creacion=datetime.utcnow()
    )
    db.session.add(nuevo_tramite)
    db.session.commit()
    return jsonify(nuevo_tramite.to_dict()), 201
