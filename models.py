from tkinter import CASCADE
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Personas(db.Model):
    __tablename__='personas'
    id= db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100), nullable=False)
    apellido=db.Column(db.String(100), nullable=True)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
    usuario_suscripcion_activa=db.Column(db.Boolean, nullable=True)
    artista_nombre_artistico=db.Column(db.String(100), nullable=False)
    artista_verificado=db.Column(db.Boolean, nullable=True)
    tipo_de_persona=db.Column(db.Boolean, nullable=False)
    facturas= db.relationship("Facturas")
    reproducciones= db.relationship("Reproducciones", cascade="all, delete-orphan")

    @classmethod
    def create(cls,nombre,apellido,email,password,usuario_suscripcion_activa,artista_nombre_artistico,artista_verificado,tipo_de_persona):
        persona=Personas(nombre=nombre,apellido=apellido,email=email,password=password,usuario_suscripcion_activa=usuario_suscripcion_activa,artista_nombre_artistico=artista_nombre_artistico,artista_verificado=artista_verificado,tipo_de_persona=tipo_de_persona)
        return persona.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return False
    def json(self):
        return{
            'id':self.id,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'email':self.email,
            'password':self.password,
            'usuario_suscripcion_activa':self.usuario_suscripcion_activa,
            'artista_nombre_artistico':self.artista_nombre_artistico,
            'artista_verificado':self.artista_verificado,
            'tipo_de_persona':self.tipo_de_persona,
        }


class Facturas(db.Model):
    __tablename__='facturas'
    id=db.Column(db.Integer, primary_key=True)
    monto_facturado=db.Column(db.Integer, nullable=True)
    fecha_facturacion=db.Column(db.Date, nullable=True)
    fecha_vencimiento=db.Column(db.Date, nullable=True)
    estado=db.Column(db.Boolean, nullable=True)
    metodo_de_pago=db.Column(db.String(100), nullable=True)
    fecha_hora_pago=db.Column(db.DateTime, nullable=True)
    id_usuario= db.Column(db.Integer,db.ForeignKey('personas.id'))

    @classmethod
    def create(cls,monto_facturado,fecha_facturacion,fecha_vencimiento,estado,metodo_de_pago,fecha_hora_pago,id_usuario):
        factura=Facturas(monto_facturado=monto_facturado,fecha_facturacion=fecha_facturacion,fecha_vencimiento=fecha_vencimiento,estado=estado,metodo_de_pago=metodo_de_pago,fecha_hora_pago=fecha_hora_pago,id_usuario=id_usuario)
        return factura.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return False
    def json(self):
        return{
            'id':self.id,
            'monto_facturado':self.monto_facturado,
            'fecha_facturacion':self.fecha_facturacion,
            'fecha_vencimiento':self.fecha_vencimiento,
            'estado':self.estado,
            'metodo_de_pago':self.metodo_de_pago,
            'fecha_hora_pago':self.fecha_hora_pago,
            'id_usuario':self.id_usuario,
        }



class Canciones(db.Model):
    __tablename__='canciones'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String, nullable=False)
    letra=db.Column(db.String, nullable=True)
    fecha_composicion=db.Column(db.Date, nullable=True)
    reproducciones= db.relationship("Reproducciones", cascade="all, delete-orphan")

    @classmethod
    def create(cls,nombre,letra,fecha_composicion):
        cancion=Canciones(nombre=nombre,letra=letra,fecha_composicion=fecha_composicion)
        return cancion.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return False
    def json(self):
        return{
            'id':self.id,
            'nombre':self.nombre,
            'letra':self.letra,
            'fecha_composicion':self.fecha_composicion,
        }


class Reproducciones(db.Model):
    __tablename__='reproducciones'
    id_usuario= db.Column(db.Integer,db.ForeignKey('personas.id'),primary_key=True)
    id_cancion= db.Column(db.Integer,db.ForeignKey('canciones.id'),primary_key=True)
    cantidad_reproducciones=db.Column(db.BigInteger,nullable=True)
    ultima_reproduccion=db.Column(db.DateTime,nullable=True)

    @classmethod
    def create(id_usuario,id_cancion,cantidad_reproducciones,ultima_reproduccion):
        cancion=Canciones(id_usuario=id_usuario,id_cancion=id_cancion,cantidad_reproducciones=cantidad_reproducciones,ultima_reproduccion=ultima_reproduccion)
        return cancion.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return False
    def json(self):
        return{
            'id_usuario':self.id_usuario,
            'id_cancion':self.id_cancion,
            'cantidad_reproducciones':self.cantidad_reproducciones,
            'ultima_reproduccion':self.ultima_reproduccion,
        }
