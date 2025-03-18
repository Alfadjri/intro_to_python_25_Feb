from abc import ABC , abstractmethod

class Person(ABC):
    def __init__(self, nama , umur):
        super().__init__()
        self._name = nama
        self.__age = umur
        
    @abstractmethod
    def get_detail(self):
        pass

    def getUmur(self):
        return self.__age
    
    def setUmur(self, umur):
        if umur > 0:
            self.__age = umur
        else:
            raise ValueError("Umur harus bernilai positif")
        