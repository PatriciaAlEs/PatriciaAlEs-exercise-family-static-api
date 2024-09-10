"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

# Se inicia la aplicacion de flask
app = Flask(__name__)
# Cosas standar
app.url_map.strict_slashes = False
# Metodo de cross origin referrer security
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



# ENDPOINTS 
# GET | POST | PUT | DELETE | PATCH

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = [ {
        "family": members
    }]
    # devolvemos el END POINT jsonify(nuestra_informacion), codigo status
    # 404 - Not found
    # 200 - ok
    # 400 - son errores 
    # 500 - error del servidor (nosotros somos el servidor)
    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])  # agregar informacion
def add_member():
    new_member = request.json
    print(new_member)

    jackson_family.add_member(new_member)
    return jsonify({"done" : "usuario creado JEJEJEJE"})


# @app.route('/members', methods=['PUT'])

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    eliminar_familiar = jackson_family.delete_member(member_id)
    if not eliminar_familiar:
        return jsonify({"familiar not found"}),400
    return jsonify({"hecho": "el borrado funcionó"}), 200

@app.route('/member/<int:member_id>', methods=['PUT'])
def update_family_member(member_id):
    new_member = request.json
    print(member_id)
    update_member_id = jackson_family.update_member(member_id, new_member)
    if not update_member_id:
        return jsonify({"msg", "no se encontró el miembro"}), 400
    return jsonify({"donde": " se actualizó"})

@app.route('/member/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    miembro_encontrado = jackson_family.get_member(member_id)
    if not miembro_encontrado:
        return jsonify({"msg":"no se encontró al miembro"})
    return jsonify(miembro_encontrado), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
