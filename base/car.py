class Car():
    ''' Car model '''

    def __init__(self, model, year, engine_vol, price, mileage):
        ''' Initialization of car attributes '''
        self.model = model
        self.year = year
        self.engine_vol = engine_vol
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def car_description(self):
        ''' Get car attributes '''
        description = "Model: " + self.model \
                      + " >  year " + str(self.year) + \
                      " engine volume " + str(self.engine_vol) + \
                      " price " + str(self.price) + "_USD" + \
                      " mileage " + str(self.mileage) + \
                      " wheels " + str(self.wheels)
        print(description)

class Truck(Car):
    ''' Truck model '''

    def __init__(self, model, year, engine_vol, price, mileage):
        ''' Initialize attributes for parent class '''
        super().__init__(model, year, engine_vol, price, mileage)
        self.wheels = 8

car = Car("Toyota Camry", 2012, 2400, 9245, 87234)
car.car_description()

truck = Truck("Volvo VNL780", 2003, 12700, 44704, 2517315)
truck.car_description()