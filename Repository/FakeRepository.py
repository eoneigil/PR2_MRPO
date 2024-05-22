from abc import ABC, abstractmethod

class FakeRepository(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def get_all(self):
        pass
