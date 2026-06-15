from abc import ABC, abstractmethod

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def __str__(self):
        return self.engine_type

class Transmission:
    def __init__(self, transmission_type):
        self.transmission_type = transmission_type
    
    def __str__(self):
        return self.transmission_type

class Body:
    def __init__(self, body_type):
        self.body_type = body_type
    
    def __str__(self):
        return self.body_type

class Car:
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.body = None
        self.color = None
        self.brand = None
        self.model = None
    
    def __str__(self):
        return f'{self.brand} {self.model} ({self.color}, {self.engine}, {self.transmission}, {self.body})'

class CarBuilder(ABC):
    def __init__(self):
        self.car = Car()
    
    @abstractmethod
    def set_brand(self):
        pass
    
    @abstractmethod
    def set_model(self):
        pass
    
    @abstractmethod
    def set_engine(self):
        pass
    
    @abstractmethod
    def set_transmission(self):
        pass
    
    @abstractmethod
    def set_body(self):
        pass
    
    @abstractmethod
    def set_color(self):
        pass
    
    def get_car(self):
        return self.car

class SedanBuilder(CarBuilder):
    def set_brand(self):
        self.car.brand = 'Toyota'
    
    def set_model(self):
        self.car.model = 'Camry'
    
    def set_engine(self):
        self.car.engine = Engine('Бензиновый 2.5L')
    
    def set_transmission(self):
        self.car.transmission = Transmission('Автоматическая')
    
    def set_body(self):
        self.car.body = Body('Седан')
    
    def set_color(self):
        self.car.color = 'Черный'

class SUVBuilder(CarBuilder):
    def set_brand(self):
        self.car.brand = 'Honda'
    
    def set_model(self):
        self.car.model = 'CR-V'
    
    def set_engine(self):
        self.car.engine = Engine('Бензиновый 1.5L Turbo')
    
    def set_transmission(self):
        self.car.transmission = Transmission('Вариатор')
    
    def set_body(self):
        self.car.body = Body('Кроссовер')
    
    def set_color(self):
        self.car.color = 'Белый'

class SportsCarBuilder(CarBuilder):
    def set_brand(self):
        self.car.brand = 'Porsche'
    
    def set_model(self):
        self.car.model = '911'
    
    def set_engine(self):
        self.car.engine = Engine('Бензиновый 3.0L Turbo')
    
    def set_transmission(self):
        self.car.transmission = Transmission('Роботизированная')
    
    def set_body(self):
        self.car.body = Body('Купе')
    
    def set_color(self):
        self.car.color = 'Красный'

class CarDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def construct_car(self):
        self.builder.set_brand()
        self.builder.set_model()
        self.builder.set_engine()
        self.builder.set_transmission()
        self.builder.set_body()
        self.builder.set_color()
        return self.builder.get_car()