from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def set_state(self, state):
        pass

class TV(Device):
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.channel = None
    
    def turn_on(self):
        self.is_on = True
        print(f'{self.brand} TV: Включен')
    
    def turn_off(self):
        self.is_on = False
        print(f'{self.brand} TV: Выключен')
    
    def set_state(self, state):
        self.channel = state
        print(f'{self.brand} TV: Канал переключен на {state}')

class Light(Device):
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.brightness = None
    
    def turn_on(self):
        self.is_on = True
        print(f'{self.brand} Light: Включен')
    
    def turn_off(self):
        self.is_on = False
        print(f'{self.brand} Light: Выключен')
    
    def set_state(self, state):
        self.brightness = state
        print(f'{self.brand} Light: Яркость установлена на {state}')

class SonyTV(TV):
    def __init__(self):
        super().__init__('Sony')

class SamsungTV(TV):
    def __init__(self):
        super().__init__('Samsung')

class PhilipsLight(Light):
    def __init__(self):
        super().__init__('Philips')

class IKEALight(Light):
    def __init__(self):
        super().__init__('IKEA')

class RemoteControl:
    def __init__(self, device):
        self.device = device
    
    def turn_on(self):
        self.device.turn_on()
    
    def turn_off(self):
        self.device.turn_off()
    
    def set_state(self, state):
        self.device.set_state(state)