#%%
class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)

class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return Car.drive(self)
tiffany_car = Car('Tesla', 'Model S')
tiffany_car.model
#%%
tiffany_car.gas = 10
tiffany_car.drive()
#%%
tiffany_car.drive()
#%%
tiffany_car.fill_gas()

# %%
tiffany_car.gas
# %%
Car.gas
# %%
christoper_car = Car('Tesla', 'Model S')
christoper_car.wheels = 2
christoper_car.wheels
# %%
Car.num_wheels
# %%
christoper_car.drive()
# %%
Car.drive()
# %%
Car.drive(christoper_car)
# %%
alex_car = MonsterTruck('Monster', 'Batmobile')
alex_car.drive()
# %%
Car.drive(alex_car)
# %%
MonsterTruck.drive(alex_car)
# %%
Car.rev(alex_car)
# %%
