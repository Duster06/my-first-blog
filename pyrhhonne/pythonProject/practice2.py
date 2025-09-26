#def print_person(name, age):
#    print(f"Name: {name}")
#    print(f"Age: {age}")
from cgitb import reset

from pyexpat.errors import messages


#print_person("anek", 57)

#def kakdela(name="joshuando"):
#    print(f"Sondy chotam, {name}")




#kakdela()
#kakdela("bob")


#def chotam(name="Tomy", age=18):
#    print(f"Name: {name}  Age: {age}")

#chotam()  # Name: Tom  Age: 18
#chotam("Bodyby")  # Name: Bob  Age: 18
#chotam("Samson", 37)  # Name: Sam  Age: 37

#def func(name, /, age, company="alawar"):
#    print(f"Name: {name} Age: {age} Company: {company}")
#
#func("Tom", company="jetulasteu", age = 90)
#func("anthony", 41)


#def sum(*numbers):
#    result = 0
#    for n in numbers:
#        result += n
#        print(f"sum = {result}")


#sum(1, 2, 3, 4, 5,)
#sum(3, 4, 5, 6)

#def get_message():
#    return "putanginamo"


#def get_message():
#    return "hello kaitpas"

#message = get_message()
#print(message)


#def double(number):
#    return 2 * number
#
#result1 = double(4)
#result2 = double(5)
#print(f"result1 = {result1}")
#print(f"result2 = {result2}")


#def print_person(name, age):
 #   if age > 120 or age < 1:
  #      print("Invalid age")
   #     return
    #print(f"Name: {name}  Age: {age}")


#print_person("Tom", 22)
#print_person("Bob", -102)


#def defa(): print("deaf")
#def defan(): print("makentohen")

#message = defa
#message()
#message = defan
#message()

#def sum(a, b): return a + b
#def multiply(a, b): return a * b

#operation = sum
#result = operation(1220, 128)
#print(result)
#operation = multiply
#print(operation(945, 132))


#def sum(a, b): return a + b


#def subtract(a, b): return a - b


#def multiply(a, b): return a * b


#def select_operation(choice):
#    if choice == 1:
#        return sum
#    elif choice == 2:
#        return subtract
#    else:
#        return multiply


#operation = select_operation(1)  # operation = sum
#print(operation(102, 36))  # 16

#operation = select_operation(2)  # operation = subtract
#print(operation(120, 62))  # 4

#operation = select_operation(3)  # operation = multiply
#print(operation(1544, 63))  # 60


#message = lambda: print("ahpar")

#message() # ahpar


#square = lambda n: n * n

#print(square(4))  #16
#print(square(5))  #25

#def do_operation(a, b, operation):
#    result = operation(a, b)
#    print(f"result = {result}")

#do_operation(5, 4, lambda a, b: a + b)
#do_operation(5, 4, lambda a, b: a * b)

#def select_operation(choice):
#    if choice == 1:
#        return lambda a, b: a + b
#    elif choice == 2:
#        return lambda a, b: a - b
#    else:
#        return lambda a, b: a * b


#operation = select_operation(1)
#print(operation(10, 6))

#operation = select_operation(2)
#print(operation(10, 6))

#operation = select_operation(3)
#print(operation(10, 6))

#a = 2
#b = 2.5
#c = a + b
#print(c)

#a = "14"
#b = 5
#c = int(a) + b
#print(c)  # budet  19 tipo da


#a = "7"
#b = 3
#c = float(a) * b
#print(c) # 21 budeta

#age = "15"
#message = "Age: " + str(age)
#print(message)


#name = "Mirobor"


#def say_hi():
#    print("Jesus re", name)


#def say_bye():
#    print("Sau bol", name)


#say_hi()
#say_bye()

def say_hi():
    name = "Kerei"
    surname ="johnson"
    print("Hello", name, surname)


def say_bye():
    name = "Janibek"
    print("Good bye", name)


say_hi()
say_bye()


def outer():  # внешняя функция
    n = 5

    def inner():  # вложенная функция
        print(n)

    inner()  # 5
    print(n)


outer()  # 5


def outer():  # внешняя функция
    n = 12# лексическое окружение - локальная переменная

    def inner():  # локальная функция
        nonlocal n
        n += 10 # операции с лексическим окружением
        print(n)

    return inner


fn = outer()  # fn = inner, так как функция outer возвращает функцию inner
# вызываем внутреннюю функцию inner
fn()
fn()
fn()

def inner():      # локальная функция
    nonlocal n
    n += 1        # операции с лексическим окружением
    print(n)

















































































































































































































