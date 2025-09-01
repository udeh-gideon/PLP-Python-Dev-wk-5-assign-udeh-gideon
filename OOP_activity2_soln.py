# My Solution to Python Dev Week 5 Activity 2 Question
# Polymorphism Challenge Accepted!
class Vehicle:
    def move(self):
        pass # Base method (to be overwritten)

# Car class
class Car(Vehicle):
    def move(self):
        print('Driving on the road 🚗...')
    
# Plane class
class Plane(Vehicle):
    def move(self):
        print('Flying in the sky ✈️...')

# Boat class
class Boat(Vehicle):
    def move(self):
        print('Sailing on the water ⛵...')

# Brief Demo
if __name__ == '__main__':
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        v.move() # Polymorphism in action