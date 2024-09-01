# Зверушка со свойствами
# Демонстрирует свойства
class Critter(object):
    """Виртуальный питомец."""
    def __init__(self, name):
        print("Появилась на свет новая зверушка!")
        self.__name = name

    @property
    def name(self): # свойство объекта
        return self.__name

    @name.setter # метод называется так же, как и свойство. Это абсолютное условие.
    # метод-сеттер должен носить то же имя, что и свойство.
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой")
        else:
            self.__name = new_name
            print("Имя успешно изменено")

    def talk(self):
        print(f"\nПривет. Меня зовут {self.name}.\n")


# основная часть
crit = Critter("Бобик")
crit.talk()
print("\nМою зверушку зовут", end=" ")
print(crit.name)
print("\nПробую изменить имя зверушки на Мурзик...")
crit.name = "Мурзик"
print("\nМою зверушку зовут", end=" ")
print(crit.name)
print("\nТеперь предприму попытку заменить имя зверушки на пустою строку...")
crit.name = ""
print("\nМою зверушку зовут", end=" ")
print(crit.name)
input("\n\nPress the enter key to exit.")