
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
        self._members = [
        {
            "id": self._generate_id(), 
            "first_name": "John", 
            "last_name": self.last_name, 
            "age": "33 years old",
            "lucky_numbers" : [7, 13, 22]   
        },

       {
            "id": self._generate_id(),
            "first_name": "Jane", 
            "last_name": self.last_name, 
            "age": "35 years old",
            "lucky_numbers" : [10, 14, 3]
        },

         {
            "id": self._generate_id(), 
            "first_name": "Jimmy", 
            "last_name": self.last_name, 
            "age": "5 years old",
            "lucky_numbers" : [1]
        }
                    ]


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
        ## Recorre la lista y elimina el miembro con el id proporcionado
        for member in self._members:   # itera (recorre) en los diccionarios de cada miembro
            if member['id'] == id:     #compara el id del diccionario (member['id'] con el id al que hacemos referencia en el parametro)
                self._members.remove(member)
                return True
                # sale del for porque ya encontró y no tiene sentido seguir buscando
        return print(f"No existe el miembro con el id {id}")
        #fuera del bucle se imprime el mensaje despues de haber revisado todos los miembros y no haber encontrado ninguno 
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
