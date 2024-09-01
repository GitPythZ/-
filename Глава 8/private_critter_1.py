class Critter(object):
    """Виртуальный питомец."""

    def __init__(self, name, mood):
        print("Появилась на свет новая зверушка!")
        self.name = name # открытый атрибут
        self.__mood = mood # закрытый атрибут, при добавлении "__" перед именем атрибута. Верно и для атрибута класса
        # как, например, total из "классово верной зверушки".
        # Доступ к закрытым атрибутам вне класса невозможен.

    def talk(self):
        print(f"\nПривет. Меня зовут {self.name}.\n")
        print("Сейчас я чувствую себя", self.__mood, "\n")

    def __private_method(self): # Закрытый метод, доступен для остальных методов класса.
        print("Это закрытый метод!")
# Предполагается, что закрытые методы(атрибуты) найдут применение лишь внутри методов самого объекта.

    def public_method(self):
        print("Это открытый метод")
        self.__private_method()


crit = Critter("Mursik", "Well")
# print(crit.mood) # AttributeError: 'Critter' object has no attribute 'mood'
# print(crit.__mood) # AttributeError: 'Critter' object has no attribute 'mood'
# print(crit._Critter__mood) # Well
crit.talk()
crit.public_method()

input("\n\nPress the enter key to exit.")
