#def sayhello():
#    print("Приветствую нового пользователя, введите своё имя")
#
#def helloname():
#    name = input()
#    print("Приветствую вас - ",name)

#def sayage():
#    age = input()
#    ageg = 18
#    print("Тебе ",age,"лет")
#    if input() < ageg :
#        print("Ваш возраст мал, доступ запрещён")
#    else:
#        print("Добро пожаловать в систему")
#
#sayhello()
#helloname()
#sayage()


#print(6 + 5)
#print(11 - 10)
#print(5 * 6)
#print(24 / 6)

#def outer():  # внешняя функция
#    n = 5  # лексическое окружение - локальная переменная

#    def inner():  # локальная функция
#        nonlocal n
#        n += 1  # операции с лексическим окружением
#        print(n)

#    return inner


#fn = outer()
#fn()
#fn()
#fn()


#def multiply(n):
#    def inner(m): return n * m

#   return inner


#fn = multiply(5)
#print(fn(10))  # 50
#print(fn(6))  # 30
#print(fn(3))  # 15

#def check(input_func):
 #   def output_func(*args):
 #       name = args[0]
 #       age = args[1]
 #       if age < 0: age = 1
 #       input_func(name, age)

#    return output_func



#@check
#def print_person(name, age):
#    print(f"Name: {name}  Age: {age}")



#print_person("Tom", 66)
#print_person("Bob", 12)


# определение функции декоратора
#def check(input_func):
#    def output_func(*args):
#        result = input_func(*args)
#        if result < 0: result = 0
#        return result

#    return output_func



#@check
#def sum(a, b):
#    return a + b



#result1 = sum(10, 20)
#print(result1)  # 30

#result2 = sum(10, -20)
#print(result2)  # 0


#class Person:
#    def __init__(self):
#        print("Создание объекта Person")


#tom = Person()

#class Person:

#    def __init__(self, name, age):
#        self.name = name  # имя человека
#        self.age = age  # возраст человека


#Beneamine = Person("Beneamine", 52)

# обращение к атрибутам
# получение значений
#print(Beneamine.name)  # Beneamine
#print(Beneamine.age)  # 52
# изменение значения
#Beneamine.age = 102
#print(Beneamine.age)  # 102


#class Person:

#    def __init__(self, name, age):
#        self.name = name  # имя человека
#        self.age = age  # возраст человека


#Janibek = Person("Janibek", 222)
#kerei = Person("kerei", 21)

#print(Janibek.name)  # Janibek
#print(kerei.name)  # kerei

#class Person:

#    def __init__(self, name, age):
#        self.name = name  # имя человека
#        self.age = age  # возраст человека


#hillarione = Person("hillarione", 212)

#hillarione.company = "Microsoft"
#print(hillarione.company)  # Microsoft

#class Person:

    #def __init__(self, name):
    #    self.name = name
   #     print("Создан человек с именем", self.name)

  #  def __del__(self):
 #       print("Удален человек с именем", self.name)


#nirnibek = Person("barabere")


#class Person:
#    def __init__(self, name, age):
#        self.name = name  # устанавливаем имя
#        self.age = age  # устанавливаем возраст

#    def print_person(self):
#        print(f"Имя: {self.name}\tВозраст: {self.age}")


#tom = Person("Tom", 39)
#tom.name = "Condome_man"  # изменяем атрибут name
#tom.age = -19  # изменяем атрибут age
#tom.print_person()  # Имя: condome_man     Возраст: -19

#class Person:
#    def __init__(self, name, age):
#        self.__name = name  # устанавливаем имя
#        self.__age = age  # устанавливаем возраст

    # сеттер для установки возраста
#    def set_age(self, age):
#        if 0 < age < 110:
#            self.__age = age
#        else:
#            print("Недопустимый возраст")

    # геттер для получения возраста
#    def get_age(self):
#        return self.__age

#    # геттер для получения имени
#    def get_name(self):
#        return self.__name

#    def print_person(self):
#        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


#tom = Person("tom", 39)
#tom.print_person()  # Имя: Tom  Возраст: 39
#tom.set_age(-3486)  # Недопустимый возраст
#tom.set_age(25)
#tom.print_person()  # Имя: Tom  Возраст: 25


class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    # свойство-геттер
    @property
    def age(self):
        return self.__age

    # свойство-сеттер
    @age.setter
    def age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


tom = Person("Tom", 39)
tom.print_person()  # Имя: Tom  Возраст: 39
tom.age = -3486  # Недопустимый возраст  (Обращение к сеттеру)
print(tom.age)  # 39 (Обращение к геттеру)
tom.age = 25  # (Обращение к сеттеру)
tom.print_person()  # Имя: Tom  Возраст: 25