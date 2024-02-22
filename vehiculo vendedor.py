class Vehicle:
    def __init__(self,color,year):
        self.color= color
        self.year= year
    
    def describe(self):
        return f"{self.color}/{self.year}"

#class car

class Car(Vehicle):
    def __init__(self,color,year,carbrand,carmodel,classseller):
        Vehicle.__init__(self,color,year)
        self.carbrand= carbrand
        self.carmodel= carmodel
        self.classseller=classseller

    def describe(self):
        return f"color:{self.color} /año:{self.year} /marca:{self.carbrand} /modelo:{self.carmodel}/concesionario del carro:{self.classseller}"
    



#class ship

class Ship(Vehicle):
    def __init__(self,color,year,shipstorage,shipmodel,classseller):
        Vehicle.__init__(self,color,year)
        self.shipstorage= shipstorage
        self.shipmodel= shipmodel
        self.classseller= classseller

    def describe(self):
        return f"color:{self.color} /año:{self.year} /Almacenamiento:{self.shipstorage} /modelo:{self.shipmodel}/concesionario del barco:{self.classseller}"




#clase airplane

class Airplane(Vehicle):
    def __init__(self,color,year,passengers,airmodel,classseller):
        Vehicle.__init__(self,color,year)
        self.passengers= passengers
        self.airmodel= airmodel
        self.classseller= classseller

    def describe(self):
        return f"color:{self.color} /año:{self.year} /Numero de pasajeros:{self.passengers} /modelo:{self.airmodel}/concesionario del avión:{self.classseller}"

#class seller

class seller:
    def __init__(self,carseller,shipseller,airseller):
        self.carseller= carseller
        self.shipseller= shipseller
        self.airseller= airseller

    def show_attr(self):
        return "Los carros que compraste se encuentran en el Concesionario: {}, Los barcos que compraste se encuentran en el Concesionario:{}, Los aviones que compraste se encuentran en el Concesionario {}".format(self.carseller,self.shipseller,self.airseller)



#atributos seller

carseller = "M Car C.A."
shipseller = "M Ship C.A."
airseller = "M Airs C.A."



print("Que caracteristicas quieres que tengan los siguientes vehículos")




#atributos de vehicle

color=input("de que color quieres que sean los vehiculos?")
year=input("de que año quieres que sean los vehiculos?")



#atributos de car

print("Elige las caracteristicas de 2 carros")

carbrand1=input("de que marca quieres que sea el primer carro?")
carmodel1=input("de que modelo quieres que sea el primer carro?")

print("                                                                                                                                                   ")

carbrand2=input("de que marca quieres que sea el segundo carro?")
carmodel2=input("de que modelo quieres que sea el segundo carro?")

print("                                                                                                                                                   ")

car1=Car(color, year, carbrand1, carmodel1,carseller)

car2=Car(color, year, carbrand2, carmodel2,carseller)



#atributos de ship    


print("Elige las caracteristicas de 2 barcos")

shipstorage1=input("cuanto almacenamiento quieres que tenga el primer barco?")
shipmodel1=input("de que modelo quieres que sea el primer barco?")

print("                                                                                                                                                   ")

shipstorage2=input("cuanto almacenamiento quieres que tenga el segundo barco?")
shipmodel2=input("de que modelo quieres que sea el segundo barco?")

print("                                                                                                                                                   ")

ship1=Ship(color, year, shipstorage1, shipmodel1,shipseller)

ship2=Ship(color, year, shipstorage2, shipmodel2,shipseller)




#atributos de airplane   

print("Elige las caracteristicas de 2 aviones")


passengers1=input("cuanto es el maximo de pasajeros que quieres que tenga el primer avión?")
airmodel1=input("de que modelo quieres que sea el primer avión?")

print("                                                                                                                                                   ")

passengers2=input("cuanto es el maximo de pasajeros que quieres que tenga el segundo avión?")
airmodel2=input("de que modelo quieres que sea el segundo avión?")

print("                                                                                                                                                   ")

airplane1=Airplane(color, year, passengers1, airmodel1,airseller)

airplane2=Airplane(color, year, passengers2, airmodel2,airseller)

print("                                                                                                                                                                                                                                                                                           ")



#registro de los vehiculos

print("los vehiculos que registraste fueron:")


print("Carros registrados:")
print(car1.describe())
print(car2.describe())



print("Barcos registrados:")
print(ship1.describe())
print(ship2.describe())


print("Aviones registrados:")
print(airplane1.describe())
print(airplane2.describe())



print("                                                                                                                                                   ")

vender=input("Deseas comprar los vehículos registrados (si/no):" )

if vender== "si":
    venta=seller(carseller,shipseller,airseller)
    print("Gracias por su compra")
    print(venta.show_attr())
else:
    print("vuelva pronto")
    quit()