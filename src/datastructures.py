
"""
actualice este archivo para implementar los siguientes métodos ya declarados:
- add_member: debe agregar un miembro a la lista self._members
- eliminar_miembro: debe eliminar un miembro de la lista self._members
- update_member: debe actualizar un miembro de la lista self._members
- get_member: debe devolver un miembro de la lista self._members
"""

"""
DICCIONARIO, VALORES
+ id: Int
+ first_name: String
+ last_name: String (Siempre Jackson)
+ age: Int > 0
+ lucky_numbers: List of integers
"""
from random import randint

class FamilyStructure:

    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [ ]


# Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    
# solo lectura: use este método para generar ID de miembros aleatorios al agregar miembros a la lista
    def _generateId(self):
        return randint(0, 99999999)



    def add_member(self, member):
        if not member.get("id"):
            member['id'] = self._generate_id()
        self._members.append(member)
        pass



    def delete_member(self, id):
        for member in self._members:   
            if member['id'] == id:    
                self._members.remove(member)
                return {"done": True}
            
        return {"msg": f"No existe el miembro con el id {id}"}
    pass



    def get_member(self, id):
        for family_member in self._members:
            if family_member['id'] == id:
                return family_member
            
        return False         # Devuelve el diccionario del miembro encontrado
    pass



    def update_member(self, id, member):
        print("Actualizando", id)
        for family_member in self._members:
            if family_member['id'] == id:
                self._members.remove(family_member)
                member["id"] = id
                self._members.append(member)
                return True

        return False 
  
    


    # este método está hecho, devuelve una lista con todos los miembros de la familia
    def get_all_members(self):
        return self._members
