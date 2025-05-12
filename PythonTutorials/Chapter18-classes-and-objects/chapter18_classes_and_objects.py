# they r like blueprints
# we create objects from classes, so they r blueprint for objects.

# naming convention: use capital letter for class name

# we set properties of class via init method (initializer function).

class Vehicle:
    # inside this, there will be properties lke make-model, no. of doors.
    # also there can be actions that vhicle can take.
    
    def __init__(self, make, model): #self is required, rest whatever u wanna put.
        self.make = make
        self.model = model
    
    # self -> referring to itself.
    def moves(self):
        print('moves along..')
        
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

# creating object from the class
# my_car = Vehicle()
# earlier we can call Vehicle like that becoz there was no init method but now there is a init method we can't call directly.
my_car = Vehicle('Tesla', 'Model 3')

print(my_car.make + " " + my_car.model) #retrieving those value from obj which i have created.
# but instead of doing this, we generally use a getter function.

# as we have a getter function, we'll use
my_car.get_make_model()

# now we can call move method on my_car
my_car.moves()


# we can create more cars from same class.
your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()


# ######################################
# INHERITANCE

class Airplane(Vehicle): #will receive vehicle class
    def __init__(self, make, model, faa_id):
        self.make = make
        self.model = model
        # or instead of writing these 2 lines, we can simply inherit from parent
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print("Flies along")

class Truck(Vehicle): #will receive vehicle class
    def moves(self):
        print("Rumbles along")

class GolfCart(Vehicle): #will receive vehicle class
    pass #as class can't be empty so it will receive (inherit) everything of vehicle class as it is...


cessna = Airplane('Cessna', 'SkyHawk', 24)
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

# all 3 classes inheriting from vehicle class 

# #########################################
# Polymorphism
# ability to perform diff in response to same inputs...

print("\n\n")

for vehicle in (my_car, your_car, cessna, mack, golfwagon):
    vehicle.get_make_model()
    vehicle.moves()