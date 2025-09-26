#print(round(2.545, 2))
#print(round(2.555, 2))
#print(round(2.565, 2))
#print(round(2.575, 2))

#print(round(2.655, 2))
#print(round(2.665, 2))
#print(round(2.675, 2))

#number = 3 + 4 * 5 ** 2 + 7
#print(number)  # 110

#number = 10
#number += 5
#print(number)  # 15

#number -= 3
#print(number)  # 12

#number *= 4
#print(number)  # 48

#first_number = 2.0001
#second_number = 5
#third_number = first_number / second_number
#print(third_number) # 0.40002000000000004

#print(round(2.554, 2))      # 2.55
#print(round(2.5551, 2))      # 2.56
#print(round(2.554999, 2))   # 2.55
#print(round(2.499, 2))      # 2.5


#print(round(2.545, 2))  # 2.54
#print(round(2.555, 2))  # 2.56 - округление до четного
#print(round(2.565, 2))  # 2.56
#print(round(2.575, 2))  # 2.58

#print(round(2.655, 2))  # 2.65 - округление не до четного
#print(round(2.665, 2))  # 2.67
#print(round(2.675, 2))  # 2.67

#number = 609013 # в двоичной форме 10010100101011110101
#print(f"number = {number:0b}")  # number = 10010100101011110101

#x1 = 2  # 010
#y1 = 5  # 101
#z1 = x1 & y1
#print(f"z1 = {z1}")  # z1 = 0

#x2 = 4  # 100
#y2 = 5  # 101
#z2 = x2 & y2
#print(f"z2 = {z2}")  # z2 = 4
#print(f"z2 = {z2:0b}")  # z2 = 100

#x1 = 2  # 010
#y1 = 5  # 101
#z1 = x1 | y1  # 111

#print(f"z1 = {z1}")  # z1 = 7
#print(f"z1 = {z1:0b}")  # z1 = 111

#x2 = 4  # 100
#y2 = 5  # 101
#z2 = x2 | y2  # 101
#print(f"z2 = {z2}")  # z2 = 5
#print(f"z2 = {z2:0b}")  # z2 = 101

#x = 9       #  1001
#y = 5       #  0101
#z = x ^ y   #  1100
#print(f"z = {z}")       # z = 12
#print(f"z = {z:0b}")   # z = 1100

#x = 45  # Значение, которое надо зашифровать - в двоичной форме 101101
#key = 102  # Пусть это будет ключ - в двоичной форме 1100110

#encrypt = x ^ key  # Результатом будет число 1001011 или 75
#print(f"Зашифрованное число: {encrypt}")

#decrypt = encrypt ^ key  # Результатом будет исходное число 45
#print(f"Расшифрованное число: {decrypt}")

#x = +94
#y = ~x;
#print(f"y: {y}")  # -95

#a = 22  # в двоичной форме 10110
#b = 2
#c = a << b  # Сдвиг числа 10110 влево на 2 разряда, равно 1011000 или 88 в десятичной системе
#print(c)  # 88

#d = a >> b  # Сдвиг числа 10110 вправо на 2 разряда, равно 101 или 5 в десятичной системе
#print(d)  # 5

#a = 5
#b = 6
#result = 5 == 6  # сохраняем результат операции в переменную
#print(result)  # False - 5 не равно 6
#print(a != b)  # True
#print(a > b)  # False - 5 меньше 6
#print(a < b)  # True

#bool1 = True
#bool2 = False
#print(bool1 == bool2)  # False - bool1 не равно bool2

#age = 19
#weight = 54.7
#result = age > 23 and weight == 60
#print(result) # False

#result = 7 and "w"
#print(result)  # w, так как 7 равно True, поэтому возвращается значение последнего операнда

#result = 0 and "w"
#print(result)  # 0, так как 0 эквивалентно False

#age = 14
#isMarried = True
#result = age > 21 or isMarried
#print(result)  # True, так как выражение isMarried = True

#age = 20
#isMarried = True
#print(not age > 21)  # True
#print(not isMarried)  # False
#print(not 4)  # False
#print(not 0)  # True

#message = "kill 'em all!"
#kill = "kill"
#print(kill in message)  # True - подстрока kill есть в строке "kill 'em all!"

#gold = "gold"
#print(gold in message)  # False - подстроки "gold" нет в строке "kill 'em all!"

#language = "farsi"
#if language == "english":
#    print("Emotion")
#print("Killer")

#language = "russian"
#if language == "english":
 #   print("Hello")
#else:
#    print("Привет")
#print("End")

#language = "norman"
#if language == "kipchak":
#    print("Hello")
#    print("World")
#elif language == "norman":
#    print("Hallo")
#    print("Welt")
#else:
#    print("Привет")
#    print("мир")

#language = "english"
#daytime = "morning"
#if language == "english":
#    print("English")
#    if daytime == "morning":
#        print("Good morning")
#    else:
#        print("Good evening")

#language = "russian"
#daytime = "morning"
#if language == "english":
#    if daytime == "morning":
#        print("Good morning")
#    else:
#        print("Good evening")
#else:
#    if daytime == "morning":
#        print("Доброе утро")
#    else:
#        print("Добрый вечер")

#number = 7

#while number < 12:
#    print(f"number = {number}")
#    number += 1
#print("program has been completed")

#number = 53

#while number < 68:
#    print(f"number = {number}")
#    number += 5
#else:
#    print(f"number = {number}. Работа цикла завершена")
#print("Работа программы завершена")

#message = "Born to kill"

#for c in message:
#    print(c)

#message = "Hello"
#for c in message:
#    print(c)
#else:
#    print(f"Последний символ: {c}. Цикл завершен");
#print("Работа программы завершена")  # инструкция не имеет отступа, поэтому не относится к else


#i = 1
#j = 1
#while i < 10:
#    while j < 10:
#       print(i * j, end="\t")
#        j += 1
#    print("\n")
#   j = 1
#    i += 1

#number = 2#
#while number < 5:
# number += 1
#   if number == 3 :    # если number = 3, выходим из цикла
#       break
#   print(f"number = {number}")

#def say_hello():
#  print("Hello")


#print("Bye")


#def say_samyonemen():
#    print("samyonemen")
#
#def bachel(): print("Bachele is marker of kantonian democratic republick")
#def say_eneryon():
#    print("eneryon")

#say_samyonemen()
#say_eneryon()
#bachel()


#def print_messages():
#    #определение локальных функций
#    def say_sumimamasen(): print("sumimasen")
#    def say_sayonara(): print("sayonara")
#    #call local function
#    say_sumimamasen()
#    say_sayonara()

#call function print_message
#print_messages()

#say_sumimasen() #say_sumimasen function out of print_messages function does not work

#def main():
#   say_hello()
#    say_goodbye()


#def say_hello():
#    print("Hello")


#def say_goodbye():
#    print("Good Bye")


# Вызов функции main
#main()

def say_hello(name):
    print(f"Hello, {name}")


say_hello("Tom")
say_hello("Bob")
say_hello("Alice")
