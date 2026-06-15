from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def read_data(self):
        pass

class FileDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_data(self):
        with open(self.file_path, 'r') as file:
            return file.read()

class DatabaseDataSource:
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    def fetch_data(self):
        return f'Data from database with connection: {self.connection_string}'

class DatabaseAdapter(DataSource):
    def __init__(self, database_source):
        self.database_source = database_source
    
    def read_data(self):
        return self.database_source.fetch_data()