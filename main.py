from calendar import month
from flask import Flask, jsonify,request
from config import config
from models import Canciones, Facturas, Reproducciones, db, Personas

from datetime import datetime
from datetime import timedelta


def create_app(enviroment):
	app = Flask(__name__)
	app.config['JSON_AS_ASCII'] = False
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app


# Accedemos a la clase config del archivo config.py
enviroment = config['development']
app = create_app(enviroment)


@app.route('/')
def holamundo():
    return 'Hola Mundo!'
#PERSONAS
#===============================================================================#
@app.route('/api/personas', methods=['GET'])
def get_personas():
    personas = [persona.json() for persona in Personas.query.all()]
    return jsonify(personas)


#===============================================================================#
@app.route('/api/personas/<id>', methods=['DELETE'])
def delete_persona(id):
    persona = Personas.query.filter_by(id=id).first()
    persona.delete()
    return jsonify({'mensaje':'Persona borrada'})
#===============================================================================#

@app.route('/api/personas', methods=['POST'])
def put_persona():
    json = request.get_json()
    persona = Personas.create(json['nombre'],json['apellido'],json['email'],json['password'],json['usuario_suscripcion_activa'],json['artista_nombre_artistico'],json['artista_verificado'],json['tipo_de_persona'])
    response = jsonify(persona.json())
    return response

#===============================================================================#
@app.route('/api/personas/<id>', methods=['PUT'])
def editar_persona(id):
    json = request.get_json()
    persona = Personas.query.filter_by(id=id).first()
    persona.nombre = json['nombre']
    persona.apellido = json['apellido']
    persona.email = json['email']
    persona.password=json['password']
    persona.usuario_suscripcion_activa=json['usuario_suscripcion_activa']
    persona.artista_verificado=json['artista_verificado']
    persona.tipo_de_persona=json['tipo_de_persona']
    persona.update()
    return jsonify(persona.json())



#FACTURAS
#===============================================================================#
@app.route('/api/facturas', methods=['GET'])
def get_facturas():
    facturas = [factura.json() for factura in Facturas.query.all()]
    return jsonify(facturas)


#===============================================================================#
@app.route('/api/facturas/<id>', methods=['DELETE'])
def delete_factura(id):
    persona = Facturas.query.filter_by(id=id).first()
    persona.delete()
    return jsonify({'mensaje':'Factura borrada'})
#===============================================================================#

@app.route('/api/facturas', methods=['POST'])
def put_factura():
    json = request.get_json()
    facturas = Facturas.create(json['monto_facturado'],json['fecha_facturacion'],json['fecha_vencimiento'],json['estado'],json['metodo_de_pago'],json['fecha_hora_pago'],json['id_usuario'])
    response = jsonify(facturas.json())
    return response

#===============================================================================#
@app.route('/api/facturas/<id>', methods=['PUT'])
def editar_factura(id):
    json = request.get_json()
    factura = Facturas.query.filter_by(id=id).first()
    factura.monto_facturado = json['monto_facturado']
    factura.fecha_facturacion = json['fecha_facturacion']
    factura.fecha_vencimiento = json['fecha_vencimiento']
    factura.estado = json['estado']
    factura.metodo_de_pago = json['metodo_de_pago']
    factura.fecha_hora_pago = json['fecha_hora_pago']
    factura.id_usuario = json['id_usuario']
    factura.update()
    return jsonify(factura.json())


#CANCIONES
#===============================================================================#
@app.route('/api/canciones', methods=['GET'])
def get_canciones():
    canciones = [cancion.json() for cancion in Canciones.query.all()]
    return jsonify(canciones)


#===============================================================================#
@app.route('/api/canciones/<id>', methods=['DELETE'])
def delete_cancion(id):
    cancion = Canciones.query.filter_by(id=id).first()
    cancion.delete()
    return jsonify({'mensaje':'Cancion borrada'})
#===============================================================================#

@app.route('/api/canciones', methods=['POST'])
def put_cancion():
    json = request.get_json()
    canciones = Canciones.create(json['nombre'],json['letra'],json['fecha_composicion'])
    response = jsonify(canciones.json())
    return response

#===============================================================================#
@app.route('/api/canciones/<id>', methods=['PUT'])
def editar_cancion(id):
    json = request.get_json()
    cancion = Canciones.query.filter_by(id=id).first()
    cancion.nombre = json['nombre']
    cancion.letra = json['letra']
    cancion.fecha_composicion = json['fecha_composicion']
    cancion.update()
    return jsonify(cancion.json())


#REPRODUCCIONES
#===============================================================================#
@app.route('/api/reproducciones', methods=['GET'])
def get_reproducciones():
    reproducciones = [reproduccion.json() for reproduccion in Reproducciones.query.all()]
    return jsonify(reproducciones)


#===============================================================================#
@app.route('/api/reproducciones/<id_usuario>/<id_cancion>', methods=['DELETE'])
def delete_reproduccion(id_usuario,id_cancion):
    reproduccion = Reproducciones.query.filter_by(id_usuario=id_usuario).filter_by(id_cancion=id_cancion).first()
    reproduccion.delete()
    return reproduccion({'mensaje':'Reproduccion borrada'})
#===============================================================================#

@app.route('/api/reproducciones', methods=['POST'])
def put_reproduccion():
    json = request.get_json()
    reproducciones = Reproducciones.create(json["id_usuario"],json['id_cancion'],json['cantidad_reproducciones'],json['ultima_reproduccion'])
    response = jsonify(reproducciones.json())
    return response


#ENDPOINS
#===============================================================================#
@app.route('/api/reproducciones/<id_usuario>/<id_cancion>', methods=['PUT'])
def editar_reproduccion(id_usuario,id_cancion):
    json = request.get_json()
    reproduccion = Reproducciones.query.filter_by(id_usuario=id_usuario).filter_by(id_cancion=id_cancion).first()
    reproduccion.cantidad_reproducciones = json['cantidad_reproducciones']
    reproduccion.ultima_reproduccion = json['ultima_reproduccion']
    reproduccion.update()
    return jsonify(reproduccion.json())

#===============================================================================#
@app.route('/api/personas/<id>/facturas', methods=['GET'])
def facturas_pagadas(id):

    query=db.text('select id,monto_facturado,fecha_facturacion,fecha_vencimiento from facturas '
                        'where id_usuario ='+id+' and estado = false')
    result = db.session.execute(query)
    facturas = {"facturas":[]}
    for row in result:
            facturas["mensaje"]="El usuario tiene facturas vencidas"
            facturas["facturas"].append({"id_factura":row[0],"monto_factura":row[1],"fecha_facturacion":row[2],"fecha_vencimiento":row[3]})
    if len(facturas["facturas"])==0:
        facturas.pop("facturas",None)
        facturas["mensaje"]="el usuario no tiene facturas pendientes."
    response=jsonify(facturas)
    return response

#===============================================================================#
@app.route('/api/facturas/sum', methods=['GET'])
def deuda():
    query=db.text("select sum(monto_facturado) from facturas "
                        "where estado = 'false' "
                        "group by id_usuario")
    result = db.session.execute(query)
    deudas = {"qty_personas":0,"qty_dinero":0}
    for row in result:
        deudas["qty_personas"]+=1
        deudas["qty_dinero"]+=row[0]
    response=jsonify(deudas)
    return response

#===============================================================================#
@app.route('/api/facturas/ganancias', methods=['GET'])
def ganancias():
    fechaactual=datetime.now()
    un_mes_antes= fechaactual - timedelta(days=30)
    query=db.text("select sum(monto_facturado) from facturas "
                    "where fecha_hora_pago>'"+un_mes_antes.strftime("%Y-%m-%d")+"'" )
    result = db.session.execute(query)
    ganancias={"qty_dinero":0}
    for row in result:
        ganancias["qty_dinero"]+=row[0]
    response=jsonify(ganancias)
    return response

#===============================================================================#
@app.route('/api/personas/<id>/masReprod', methods=['GET'])
def maxRepro(id):
    query=db.text("select id_cancion,nombre,cantidad_reproducciones from reproducciones inner join canciones on canciones.id = reproducciones.id_cancion "
                        "where id_usuario ="+id+" "
                        "order by cantidad_reproducciones desc "
                        "limit 10 ")
    result = db.session.execute(query)
    TopCanciones={"top_ten":[]}
    for row in result:
        TopCanciones["top_ten"].append({"id_cancion":row[0],"nombre_cancion":row[1],"reproducciones":row[2]})
    if len(TopCanciones["top_ten"])==0:
        TopCanciones.pop("top_ten",None)
        TopCanciones["mensaje"]="El usuario no a escuchado canciones"
    response=jsonify(TopCanciones)
    return response


#===============================================================================#
@app.route('/api/canciones/max', methods=['GET'])
def CancionesMax():
    query=db.text("select id_cancion,nombre,sum from (select id_cancion,sum(cantidad_reproducciones) from reproducciones "
                        "group by id_cancion) as SumaRC inner join canciones on SumaRC.id_cancion = canciones.id "
                        "order by sum desc "
                        "limit 10 ")
    result = db.session.execute(query)
    TopCanciones={"top_ten":[]}
    for row in result:
        TopCanciones["top_ten"].append({"id_cancion":row[0],"nombre_cancion":row[1],"reproducciones_Totales":row[2]})
    if len(TopCanciones["top_ten"])==0:
        TopCanciones.pop("top_ten",None)
        TopCanciones["mensaje"]="No hay canciones reproducidas"
    response=jsonify(TopCanciones)
    return response




if __name__ == '__main__':
	app.run(debug=True)
