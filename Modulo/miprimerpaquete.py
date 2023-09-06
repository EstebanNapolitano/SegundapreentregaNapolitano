class Persona():
    def __init__(self, nom, ape, ed):
        self.nombre = nom
        self.apellido = ape
        self.edad = ed

    

class Cliente(Persona):

    def __init__(self, nom, ape, ed, client_id, saldo):
        super().__init__(nom, ape, ed)
        self.numero_de_cliente = client_id
        self.saldo = saldo

    def __str__(self):
        return f"{self.nombre} {self.apellido} su numero de cliente es {self.numero_de_cliente}. {self.tiene_deuda()}"
    
    def tiene_deuda(self):
        if self.saldo <= 0:
            return "Tiene deuda"
        else:
            return "No tiene deuda"

cliente1 = Cliente("Esteban", "Napolitano", 25, "123", -100)

print(cliente1)

