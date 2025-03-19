from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo_electronico = db.Column(db.String(100), unique=True, nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo_electronico': self.correo_electronico,
            'rol': self.rol
        }

class Tramite(db.Model):
    nt = db.Column(db.String(50), primary_key=True)
    ano = db.Column(db.Integer, nullable=False)
    responsable_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_atencion = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'nt': self.nt,
            'ano': self.ano,
            'responsable_id': self.responsable_id,
            'estado': self.estado,
            'fecha_creacion': self.fecha_creacion,
            'fecha_atencion': self.fecha_atencion
        }

class Alerta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tramite_id = db.Column(db.String(50), db.ForeignKey('tramite.nt'), nullable=False)
    responsable_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fecha_envio = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(50), nullable=False)

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tramite_id = db.Column(db.String(50), db.ForeignKey('tramite.nt'), nullable=False)
    responsable_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fecha_derivacion = db.Column(db.DateTime, nullable=False)
    fecha_atencion = db.Column(db.DateTime)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    mensaje = db.Column(db.String(500), nullable=False)
    fecha_envio = db.Column(db.DateTime, nullable=False)
