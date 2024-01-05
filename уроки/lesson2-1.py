# ООП - Объектно оорентированное программирование
#  class - все внутренности класса 
#  Правила class - Названия всегда начниа.тся с большой буквы

class Human:

    # свойсто класса - это переменная внутри класса(эта переменная будет присваеваться всем экземплярам класса)
    head = '11'

# магические методы - тот же метод(функция внутри класса), начинается и заканчивается __
    # конструктор класса init
    def __init__(self, name, age, nikname, power):
        self.name = name
        self.age = age
        self.nikname = nikname
        self.power = power
    
    

    def __str__(self) -> str:
        return f'Nik: {self.nikname}, Name: {self.name}, Ability: {self.power}'

    # любая функция внутри класса это - метод
    def Hi(self):
        print(self.age * 2)

# Переменная созданная на основе класса называется - экземпляр либо объект класса
human = Human('beka', 20, 'T9', 'писать стихи')
human2 = Human('Ibragim', 14, 'quizi', 'играть в игры')
print(human)
human2.RT='Расширение территории'
human.Hi()
print(human2.RT)