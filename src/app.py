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

John = {
    "first_name": "John",
    "last_name": jackson_family.last_name,
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}

Jane = {
    "first_name": "Jane",
    "last_name": jackson_family.last_name,
    "age": 35,
    "lucky_numbers": [10, 14, 3]
}

Jimmy = {
    "first_name": "Jimmy",
    "last_name": jackson_family.last_name,
    "age": 5,
    "lucky_numbers": [1]
}

jackson_family.add_member(John)
jackson_family.add_member(Jane)
jackson_family.add_member(Jimmy)


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
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200



@app.route('/member', methods=['POST'])  # agregar informacion
def add_member():
    new_member = request.json
    print(new_member)

    jackson_family.add_member(new_member)
    return jsonify({"done" : "usuario creado JEJEJEJE"})



@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    eliminar_familiar = jackson_family.delete_member(member_id)
    if "done" in eliminar_familiar:
        return jsonify(eliminar_familiar), 200
        # return jsonify({"eliminar_familiar": "el borrado funcionó"}), 200
    # return jsonify({"msg":"familiar not found"}),400
    return jsonify({"msg": "Member not found"}), 400
    


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
