# Моя зверущка
# Виртуальный питомец, о котором вы можете заботиться
import random


class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        hunger = random.randint(0, 5)
        self.hunger = hunger
        boredom = random.randint(0, 5)
        self.boredom = boredom

    def __str__(self):
        line = "Critter object\n"
        line += "Имя: " + self.name + "\n"
        line += "Уровень голода: " + str(self.hunger) + "\n"
        line += "Уровень уныния: " + str(self.boredom) + "\n"
        line += f"Общий уровень несчастья {self.name}:" + str(self.boredom + self.hunger) + "\n"
        return line

    def __pass_time(self):
        """Закрытый метод, работа которого увеличивает уровень голода и уныния.
        Этот метод вызывается каждый раз после того, как зверушка ест, играет или беседует с хозяином;
        Этот метод изображает течение времени;
        Метод закрытый, т.к. его должны вызывать лишь другие методы класса;
        """
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        """Отражает самочувствие зверушки. Вычисляется сложением атрибутов hunger и boredom объекта класса Critter;
        Возвращает строку: -прекрасно, неплохо, не сказать, чтобы хорошо, ужасно, исходя из суммы атрибутов;
        """
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать, чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        """Метод talk узнает значение свойства mood объекта класса Critter.
        Сообщает о самочувствии зверушки, после чего вызывается метод __pass_time();
        """
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood, "\n")
        self.__pass_time()

    def eat(self, food=4):
        """Метод eat уменьшает уровень голода зверька на величину, переданную параметру food.
        Если не передавать никакого значения, то по умолчанию food окажется равным 4;
        Программа следит за уровнем голода, не позволяя ему оказаться отрицательным числом;
        В конце, вызывается __pass_time();
        """
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        """Метод play() снижает уровень уныния зверька на величину, переданную параметру fun.
        Если не передавать никакого значения, то по умолчанию fun окажется равным 4;
        Программа следит за уровнем голода, не позволяя ему оказаться отрицательным числом;
        В конце, вызывается __pass_time();
        """
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    # @property
    # def name(self):
    #     return self.name
    #
    # @name.setter
    # def name(self, new_name):
    #     str(input()) == new_name
    #     if new_name == "":
    #         print("Имя зверюшки не может быть пустой строкой")
    #     else:
    #         self.name = new_name
    #         print(f"Имя успешно изменено, теперь вашу зверушку зовут {self.name}")


def main():
    """В начале работы ПО получает из пользовательского ввода имя зверька и инстанцирует класс Critter.
    """
    crit_name = input("Как вы назовете свою первую зверушку?\nПоле для ввода: ")
    print("Появилась на свет новая зверушка! Её зовут -", crit_name)
    crit1_name = input("Как вы назовете свою вторую зверушку?\nПоле для ввода: ")
    print("Появилась на свет новая зверушка! Её зовут -", crit1_name)
    crit2_name = input("Как вы назовете свою третью зверушку?\nПоле для ввода: ")
    print("Появилась на свет новая зверушка! Её зовут -", crit2_name)
    crit = Critter(crit_name)
    crit1 = Critter(crit1_name)
    crit2 = Critter(crit2_name)

    choice = None
    while choice != "0":
        print(f"""
        Мои зверушки {crit_name}, {crit1_name}, {crit2_name}
        1 - Узнать о самочувствии зверушки
        2 - Покормить зверька
        3 - Поиграть со зверушкой
        4 - Изменить имя зверушки
        0 - Выйти
        """)
        choice = input("Ваш выбор: ")
        print()
        # Выход
        if choice == "0":
            print("До свидания.")
        # беседа со зверушкой
        elif choice == "1":
            crit.talk()
            crit1.talk()
            crit2.talk()
        # Кормление зверушки
        elif choice == "2":
            food = int(input("Хотите покормить зверушку? Дерзайте! Пусть зверёк наестся!\n"
                             "Передайте лакомства в размере от 1 до 5 штучек: "))
            if food < 1:
                print(f"Нечего дразнить {crit_name, crit1_name, crit2_name} пустыми обещаниями!")
            elif food > 5:
                print(f"Куда {crit_name, crit1_name, crit2_name} столько вкусняшек, "
                      f"поберегите здоровье {crit_name, crit1_name, crit2_name}!")
            else:
                while food < 5 and food > 1:
                    food = int(input("Хотите покормить зверушек? Дерзайте! Пусть зверята наедятся!\n"
                                     "Передайте лакомства в размере от 1 до 5 штучек: "))
                crit.eat()
                crit1.eat()
                crit2.eat()
        # Игра со зверушкой
        elif choice == "3":
            fun = int(input(f"Как долго вы хотите поиграть с {crit_name, crit1_name, crit2_name} или почесать у "
                                    f"{crit_name, crit1_name, crit2_name} за ушком?\n"
                                    f"Приступайте к игре с {crit_name, crit1_name, crit2_name}, "
                                    f"сколько минут от 1 до 5 у вас есть на игру? "))
            if fun < 1:
                print(f"Сыграете с {crit_name} в другой раз! Счастливо!")
            elif fun > 5:
                print(f"{crit_name, crit1_name, crit2_name} сегодня целый день работал - бэзил, мурчал, а также кезил!\n"
                      f"Поиграй с {crit_name, crit1_name, crit2_name} во что-то менее утомительное...")
            else:
                while fun < 5 and fun > 1:
                    fun = int(input(f"Как долго вы хотите поиграть с {crit_name, crit1_name, crit2_name} или почесать у "
                                    f"{crit_name, crit1_name, crit2_name} за ушком?\n"
                                    f"Приступайте к игре с {crit_name, crit1_name, crit2_name}, "
                                    f"сколько минут от 1 до 5 у вас есть на игру? "))
            crit.play()
            crit1.play()
            crit2.play()
        # Изменение имени зверушки
        elif choice == "4":
            crit.name()
            crit1.name()
            crit2.name()
        # Вызов витальных показателей зверька.
        elif choice == "5":
            print(crit)
            print(crit1)
            print(crit2)
        # Непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)


main()
input("\n\nНажмите Enter, чтобы выйти")