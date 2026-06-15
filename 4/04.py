class User:
    def __init__(self, name: str) -> None:
        self.name = name 

    def send_message(self, user: 'User', message: str) -> None:
        pass

    def post(self, message: str) -> None:
        pass

    def info(self) -> str:
        return ''
    
    def describe(self) -> None:
        print(self.name, self.info())

class Person(User):
    def __init__(self, name: str, birthday: str) -> None:
        self.name = name
        self.birthday = birthday 

    def info(self) -> str:
        return f'Дата рождения: {self.birthday}'
    
    def subscribe(self, user: User) -> None:
        pass 

class Community(User):
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = self.description

    def info(self) -> str:
        return f'Описание: {self.description}'