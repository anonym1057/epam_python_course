import abc


class Vehicle(metaclass=abc.ABCMeta):
    """
    Abstract class describing the vehicle
    """
    def __init__(self, wheel, model, year, mileage, base_price):
        self.wheel = wheel
        self.year = year
        self.model = model
        self.mileage = mileage
        self.base_price = base_price

    @abc.abstractmethod
    def vehicle_type(self):
        """
        Abctract function. Return type vehicle.
        :return: str
        """
        pass

    @property
    def is_motocycle(self):
        """
        Function  identifies vihicle is motocycle or not
        :return:bool: True - vehicle is motocycle. False - otherwise
        """
        return self.wheel == 2

    @property
    def purchase_price(self):
        """
            Calculate price of the vehicle
        :return: boo: price of the vehicle
        """
        return self.base_price - 0.1 * self.mileage
        pass


class Car(Vehicle):
    """
    Class of car
    """
    def __init__(self, model, year, mileage, base_price):
        super().__init__(4, model, year, mileage, base_price)

    def vehicle_type(self):
        return "Car"


class Motocycle(Vehicle):
    """
    Class of motocycle
    """
    def __init__(self, model, year, mileage, base_price):
        super().__init__(2, model, year, mileage, base_price)

    def vehicle_type(self):
        return "Motocycle"


class Truck(Vehicle):
    """
    Class of truck
    """
    def __init__(self, model, year, mileage, base_price):
        super().__init__(4, model, year, mileage, base_price)

    def vehicle_type(self):
        return "Truck"


class Bus(Vehicle):
    """
    Class of bus
    """
    def __init__(self, model, year, mileage, base_price):
        super().__init__(4, model, year, mileage, base_price)

    def vehicle_type(self):
        return "Bus"


if __name__ == '__main__':
    car = Car("SuperCar", 2000, 1_000, 3 * 10e6)
    moto = Motocycle("Moto", 1970, 10_000, 4 * 10e6)

    print("car type: ", car.vehicle_type())
    print("is motocycle: ", car.is_motocycle)
    print("purchase: ", car.purchase_price)
    print("motocycle type: ", moto.vehicle_type())
    print("is motocycle: ", moto.is_motocycle)
    print("purchase: ", moto.purchase_price)
