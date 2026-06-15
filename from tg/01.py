class User:
    def __init__(self, username: str, password: str) -> None:
        self.__username = username
        self.__password = password
    
    @property
    def username(self) -> str:
        return self.__username
    
    def check_password(self, password: str) -> bool:
        return self.__password == password
    
    def set_password(self, old_password: str, new_password: str) -> bool:
        if self.check_password(old_password):
            self.__password = new_password
            return True
        return False