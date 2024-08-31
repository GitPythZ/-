# Просто зверушка
# Демонстрирует простейшие классы и объект
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверушка!")
        self.name = name

    def __str__(self):
        rep = "Обэект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep

    def talk(self):
        print(f"Привет. Меня зовут {self.name}.\n")


# Основная часть
crit1 = Critter("Бобик")
crit1.talk()
crit2 = Critter("Мурзик")
crit2.talk()
print("Вывод объекта crit1 на экран:")
print(crit1)
print("Непосредственный доступ к атрибуту crit1.name")
print(crit1.name)
input("\n\nНажмите Enter, чтобы выйти")

