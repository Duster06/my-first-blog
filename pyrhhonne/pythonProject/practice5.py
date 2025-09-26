
#class Counter:
#    def __init__(self, value):
#        self.value = value

#    def __add__(self, other):
#        return Counter(self.value + other.value)

#counter1 = Counter(50)
#counter2 = Counter(132)
#counter3 = counter1 + counter2
#print(counter3.value)
# крутое сложение каунтер

#class Counter:
#    def __init__(self, value):
#        self.value = value

#    def __add__(self, other):
#        return self.value + other

#counter1 = Counter(653)
#result = counter1 + 132
#print(result)   #785


#class Counter:
#    def __init__(self, value):
#        self.value = value

#    def __gt__(self, other):
#        return self.value > other.value

#    def __lt__(self, other):
#        return self.value < other.value


#counter1 = Counter(1)
#counter2 = Counter(2)

#if counter1 < counter2:
#    print("counter1 больше чем counter2")
#elif counter1 < counter2:
#    print("counter1 меньше чем counter2")
#else:
#    print("counter1 и counter2 равны")

#class Counter:
#    pass
#def __init__(self, value):
#    self.value = value

#    def __eq__(self, other): return self.value == other.value

#    def __ne__(self, other): return not (self == other)

#    def __gt__(self, other): return self.value > other.value

#    def __le__(self, other): return not (self > other)

#    def __lt__(self, other): return self.value < other.value

#    def __ge__(self, other): return not (self < other)


#c1 = Counter(115)
#c2 = Counter(22)

#print(c1 == c2)
#print(c1 != c2)

#print(c1 < c2)
#print(c1 >= c2)
#false
#true
#false
#true


#import abc


#class Shape(abc.ABC):
#    @abc.abstractmethod
#    def area(self): pass  # площадь фигуры


# класс прямоугольника
#class Rectangle(Shape):
#    def __init__(self, width, height):
#        self.width = width
#        self.height = height

#    def area(self): return self.width * self.height


# класс круга
#class Circle(Shape):
#    def __init__(self, radius):
#        self.radius = radius

#    def area(self): return self.radius * self.radius * 3.14


#def print_area(shape):
#    print("Area:", shape.area())


#rect = Rectangle(30, 50)
#circle = Circle(30)
#print_area(rect)  # Area: 1500
#print_area(circle)  # Area: 2826.0


#try:
#    number = int(input("Введите число: "))
#    print("Введенное число:", number)
#except:
#    print("Преобразование прошло неудачно")
#finally:
#    print("Блок try завершил выполнение")
#print("Завершение программы")


#try:
#    age = int(input("Введите возраст: "))
#    if age > 110 or age < 1:
#        raise Exception("Некорректный возраст")
#    print("Ваш возраст:", age)
#except ValueError:
#    print("Введены некорректные данные")
#except Exception as e:
#    print(e)
#print("Завершение программы")

#class PersonAgeException(Exception):
#    def __init__(self, age, minage, maxage):
#        self.age = age
#        self.minage = minage
#        self.maxage = maxage

#    def __str__(self):
#        return f"Недопустимое значение: {self.age}. " \
#               f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"


#class Person:
#    def __init__(self, name, age):
#        self.__name = name  # устанавливаем имя
#        minage, maxage = 1, 110
#        if minage < age < maxage:  # устанавливаем возраст, если передано корректное значение
#            self.__age = age
#        else:  # иначе генерируем исключение
#            raise PersonAgeException(age, minage, maxage)

#    def display_info(self):
#        print(f"Имя: {self.__name}  Возраст: {self.__age}")


#try:
#    tom = Person("Tom", 37)
#    tom.display_info()  # Имя: Tom  Возраст: 37

#    bob = Person("Bob", -23)
#    bob.display_info()
#except PersonAgeException as e:
#    print(e)  # Недопустимое значение: -23. Возраст должен быть в диапазоне от 1 до 110

