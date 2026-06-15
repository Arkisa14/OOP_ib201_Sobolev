from abc import ABC, abstractmethod

class System(ABC):
    @abstractmethod
    def get_status(self) -> str:
        pass

class LightingSystem(System):
    def __init__(self):
        self._main_light = False
        self._dimmed_light = False
    
    def turn_on_main(self) -> str:
        self._main_light = True
        return 'Основное освещение включено'
    
    def turn_off_main(self) -> str:
        self._main_light = False
        return 'Основное освещение выключено'
    
    def turn_on_dimmed(self) -> str:
        self._dimmed_light = True
        return 'Приглушенный свет включен'
    
    def turn_off_dimmed(self) -> str:
        self._dimmed_light = False
        return 'Приглушенный свет выключен'
    
    def turn_off_all(self) -> str:
        self._main_light = False
        self._dimmed_light = False
        return 'Всё освещение выключено'
    
    def get_status(self) -> str:
        return f'Освещение: основной свет - {self._main_light}, приглушенный - {self._dimmed_light}'

class ClimateSystem(System):
    def __init__(self):
        self._temperature = 22
        self._mode = 'normal'
    
    def set_comfort_temp(self) -> str:
        self._temperature = 23
        self._mode = 'normal'
        return 'Установлена комфортная температура 23°C'
    
    def set_party_temp(self) -> str:
        self._temperature = 20
        self._mode = 'party'
        return 'Установлена температура для вечеринки 20°C'
    
    def set_night_temp(self) -> str:
        self._temperature = 18
        self._mode = 'night'
        return 'Температура снижена до 18°C'
    
    def turn_off(self) -> str:
        self._mode = 'off'
        return 'Климат-контроль выключен'
    
    def get_status(self) -> str:
        return f'Климат: температура {self._temperature}°C, режим {self._mode}'

class SecuritySystem(System):
    def __init__(self):
        self._alarm = False
        self._sensors = False
    
    def deactivate(self) -> str:
        self._alarm = False
        self._sensors = False
        return 'Сигнализация отключена'
    
    def activate(self) -> str:
        self._alarm = True
        self._sensors = True
        return 'Сигнализация активирована'
    
    def get_status(self) -> str:
        return f'Безопасность: сигнализация - {self._alarm}, датчики - {self._sensors}'

class MultimediaSystem(System):
    def __init__(self):
        self._music = False
        self._tv = False
        self._volume = 0
    
    def turn_on_music(self) -> str:
        self._music = True
        self._volume = 50
        return 'Музыка включена'
    
    def turn_off_music(self) -> str:
        self._music = False
        self._volume = 0
        return 'Музыка выключена'
    
    def turn_off_all(self) -> str:
        self._music = False
        self._tv = False
        self._volume = 0
        return 'Вся мультимедиа выключена'
    
    def get_status(self) -> str:
        return f'Мультимедиа: музыка - {self._music}, ТВ - {self._tv}, громкость - {self._volume}'

class SmartHomeFacade:
    def __init__(self):
        self._lighting = LightingSystem()
        self._climate = ClimateSystem()
        self._security = SecuritySystem()
        self._multimedia = MultimediaSystem()
    
    def home_mode(self) -> list[str]:
        results = []
        results.append(self._lighting.turn_on_main())
        results.append(self._climate.set_comfort_temp())
        results.append(self._security.deactivate())
        results.append(self._multimedia.turn_off_all())
        return results
    
    def away_mode(self) -> list[str]:
        results = []
        results.append(self._lighting.turn_off_all())
        results.append(self._climate.turn_off())
        results.append(self._security.activate())
        results.append(self._multimedia.turn_off_all())
        return results
    
    def party_mode(self) -> list[str]:
        results = []
        results.append(self._lighting.turn_on_dimmed())
        results.append(self._climate.set_party_temp())
        results.append(self._security.deactivate())
        results.append(self._multimedia.turn_on_music())
        return results
    
    def night_mode(self) -> list[str]:
        results = []
        results.append(self._lighting.turn_off_main())
        results.append(self._climate.set_night_temp())
        results.append(self._security.activate())
        results.append(self._multimedia.turn_off_all())
        return results
    
    def get_all_systems_status(self) -> str:
        return '\n'.join([
            self._lighting.get_status(),
            self._climate.get_status(),
            self._security.get_status(),
            self._multimedia.get_status()
        ])