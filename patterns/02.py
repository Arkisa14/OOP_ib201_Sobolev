from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class ElectricCar(Car):
    def drive(self):
        print('Driving an electric car.')

class PetrolCar(Car):
    def drive(self):
        print('Driving a petrol car.')

class HybridCar(Car):
    def drive(self):
        print('Driving a hybrid car.')

class CarFactory(ABC):
    @abstractmethod
    def produce_car(self):
        pass

class ElectricCarFactory(CarFactory):
    def produce_car(self):
        return ElectricCar()

class PetrolCarFactory(CarFactory):
    def produce_car(self):
        return PetrolCar()

class HybridCarFactory(CarFactory):
    def produce_car(self):
        return HybridCar()
    

