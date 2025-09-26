#class Person:

#    def __init__(self, name):
#        self.__name = name  # имя человека

#    @property
#    def name(self):
#        return self.__name

#    def display_info(self):
#        print(f"Name: {self.__name} ")


#class Employee(Person):

#    def work(self):
#        print(f"{self.name} works")


#Tolige = Employee("Lofree")
#print(Tolige.name)  # Lofree
#Tolige.display_info()  # Name: Lofree
#Tolige.work()  # Lofree works


#  класс работника
#class Killer:
#    def work(self):
#        print("Killer kills")


#  класс студента
#class Student:
#    def study(self):
#        print("Student studies")


#class WorkingStudent(Killer, Student):  # Наследование от классов Employee и Student
#    pass



#tom = WorkingStudent()
#tom.work()
#tom.study()


#class Person:

#    def __init__(self, name):
#        self.__name = name  # имя человека

#    @property
#    def name(self):
#        return self.__name

#    def display_info(self):
#        print(f"Name: {self.__name}")


#class Employee(Person):

#    def __init__(self, name, company):
#        super().__init__(name)
#        self.company = company

#    def display_info(self):
#        super().display_info()
#        print(f"Company: {self.company}")

#    def work(self):
#        print(f"{self.name} works")


#tom = Employee("Жонибек", "Люляби инсистресс")
#tom.display_info()  # Name: Жонибек
# Company: Люляби инсистресс


#class Person:

#    def __init__(self, name):
#        self.__name = name  # имя человека

#    @property
#    def name(self):
#        return self.__name

#    def do_nothing(self):
#        print(f"{self.name} does nothing")


#  класс работника
#class Racer(Person):

#    def work(self):
#        print(f"{self.name} driving")


#  класс студента
#class Student(Person):

 #   def study(self):
 #       print(f"{self.name} studies")


#def act(person):
#    if isinstance(person, Student):
#        person.study()
#    elif isinstance(person, Racer):
#        person.work()
#    elif isinstance(person, Person):
#        person.do_nothing()


#tom = Racer("Блендамет")
#bob = Student("Лакалют")
#sam = Person("Колгате")

#act(tom)  # Tom works
#act(bob)  # Bob studies
#act(sam)  # Sam does nothing



#программа какая то канто ну шукуан
import random

def угадай_число():
    загаданное_число = random.randint(1, 100)
    попытки = 0
    print("Min nulek kanto un 1 dor 100. Doin duolis!")

    while True:
        try:
            ввод = int(input("Ty jukko: "))
            попытки += 1

            if ввод < загаданное_число:
                print("Kanto saletu.")
            elif ввод > загаданное_число:
                print("Kanto hiretu.")
            else:
                print(f"Kanto no nikor {загаданное_число} fur {попытки} zaless.")
                break
        except ValueError:
            print("Kanto kakertu.")

# Запуск игры
угадай_число()
