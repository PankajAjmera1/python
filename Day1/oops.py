#Basic class & Object

class Car:
    def __init__(self,brand,model) :
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    @staticmethod
    def hello():
        return "Hello, World"
    @property
    def full_name(self):
        return f"{self.brand} {self.model}"
        

        

my_car = Car("Toyota","Corolla")  
print(my_car.brand)


print(my_car.model)
print(my_car.full_name())

print(Car.hello())
# print(my_car.hello())  #It will throw
# print(Car.full_name())  #It will throw

# print(my_car.full_name)  #It will throw
# print(Car.full_name)  #It will throw






#multiple inheritance

class Battery:
    def battery_info(self):
        return "1000mAh"

class Engine:
    def engine_info(self):
        return "1000cc"
    

class ElectricCarTwo(Battery,Engine ,Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
print(my_new_tesla.brand)
