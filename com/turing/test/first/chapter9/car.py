class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def update_odometer(self, mileage):
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
print(my_new_car.odometer_reading)
my_new_car.odometer_reading = 23
print(my_new_car.odometer_reading)
my_new_car.update_odometer(26)
print(my_new_car.odometer_reading)
