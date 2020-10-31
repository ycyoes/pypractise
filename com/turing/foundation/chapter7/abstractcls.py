from abc import ABC, abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass
# Talker()

class Knigget(Talker):
    def talk(self):
        print("Ni!")

k = Knigget()
isinstance(k, Talker)
print(isinstance(k, Talker))
k.talk()

