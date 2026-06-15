class Weapon:
    def __init__(self, name: str, damage: float, range: float):
        self.__name = name
        self.__damage = damage
        self.__range = range
    
    def hit(self, actor: 'BaseCharacter', target: 'BaseCharacter'):
        if not target.is_alive():
            print('Враг уже повержен')
            return
        actor_x, actor_y = actor.get_coords()
        target_x, target_y = target.get_coords()
        distance = ((actor_x - target_x) ** 2 + (actor_y - target_y) ** 2) ** 0.5
        if distance > self.__range:
            print(f'Враг слишком далеко для оружия {self.__name}')
            return
        print(f'Врагу нанесен урон оружием {self.__name} в размере {self.__damage}')
        target.get_damage(self.__damage)
    
    def __str__(self):
        return self.__name

class BaseCharacter:
    def __init__(self, pos_x: float, pos_y: float, hp: float):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__hp = hp
    
    def move(self, delta_x: float, delta_y: float):
        self.__pos_x += delta_x
        self.__pos_y += delta_y
    
    def is_alive(self):
        return self.__hp > 0
    
    def get_damage(self, amount: float):
        self.__hp -= amount
    
    def get_coords(self):
        return (self.__pos_x, self.__pos_y)

class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x: float, pos_y: float, weapon: Weapon, hp: float):
        super().__init__(pos_x, pos_y, hp)
        self.__weapon = weapon
    
    def hit(self, target: BaseCharacter):
        if isinstance(target, MainHero):
            self.__weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')
    
    def __str__(self):
        return f'Враг на позиции {self.get_coords()} с оружием {self.__weapon}'

class MainHero(BaseCharacter):
    MAX_HP = 200
    
    def __init__(self, pos_x: float, pos_y: float, name: str, hp: float):
        super().__init__(pos_x, pos_y, hp)
        self.__name = name
        self.__weapons: list[Weapon] = []
        self.__current_weapon_index = -1
    
    def hit(self, target: BaseCharacter):
        if not self.__weapons:
            print('Я безоружен')
            return
        if isinstance(target, BaseEnemy):
            self.__weapons[self.__current_weapon_index].hit(self, target)
        else:
            print('Могу ударить только врага')
    
    def add_weapon(self, weapon: Weapon):
        if isinstance(weapon, Weapon):
            self.__weapons.append(weapon)
            if len(self.__weapons) == 1:
                self.__current_weapon_index = 0
            print(f'Подобрал {weapon}')
        else:
            print('Это не оружие')
    
    def next_weapon(self):
        if not self.__weapons:
            print('Я безоружен')
        elif len(self.__weapons) == 1:
            print('У меня только одно оружие')
        else:
            self.__current_weapon_index = (self.__current_weapon_index + 1) % len(self.__weapons)
            print(f'Сменил оружие на {self.__weapons[self.__current_weapon_index]}')
    
    def heal(self, amount: float):
        self.__hp = min(self.__hp + amount, self.MAX_HP)
        print(f'Полечился, теперь здоровья {self.__hp}')