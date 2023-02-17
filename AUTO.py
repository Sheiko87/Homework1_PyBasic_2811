# 1
class Transport:
    def __init__(self, wheels, speed, number, power):
        self.__number = number
        self.__power = power
        self.__wheels = wheels
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def wheels(self):
        return self.__wheels

    @wheels.setter
    def wheels(self, wheels: int):
        self.__wheels = wheels

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power: int):
        self.__power = power

    def __str__(self):
        return (f'Количество колес : {self.__wheels}\nМакс. скорость : {self.__speed} км\ч\n'
                f'Госномер : {self.__number}\nМощность двигателя : {self.__power} л.с.')


class Auto(Transport):
    def __init__(self, wheels, speed, number, power, name):
        super().__init__(self, wheels, speed, number, power)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def __str__(self):
        return (f'{super().__str__()}\nМарка автомобиля : {self.__name}')


class Bus(Transport):
    def __init__(self, wheels, speed, number, power, passengers):
        super().__init__(wheels, speed, number, power)
        self.__passengers = passengers

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, passengers: int):
        self.__passengers = passengers

    def __str__(self):
        return (f'{super().__str__()}\nКолличество пассажиров : {self.__passengers}')


class Bicycle(Transport):
    def __init__(self, wheels, speed, weight):
        super().__init__(self, wheels, speed, number: None, power: None)
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    def __str__(self):
        return (f'{super().__str__()}\nВес велосипеда : {self.__weight}')


class Truck(Auto):
    def __init__(self, wheels, speed, number, power, name, tonnage):
        super().__init__(self, wheels, speed, number, power, name)
        self.__tonnage = tonnage

    @property
    def tonnage(self):
        return self.__tonnage

    @tonnage.setter
    def tonnage(self, tonnage: int):
        if 3 <= tonnage <= 10:
            self.__tonnage = tonnage

    def __str__(self):
        return (f'{super().__str__()}\nТоннаж грузовика - {self.__tonnage} тон')


class Motorbike(Bicycle):
    def __init__(self, wheels, speed, weight, signal):
        super().__init__(wheels, speed, weight)
        self.__signal = signal

    @property
    def signal(self):
        return self.signal

    @signal.setter
    def signal(self, volume: str):
        self.__signal = volume

    def __str__(self):
        return (f'{super().__str__()}\nСигнал :{self.__signal}')


# 2
class Animal:
    def __init__(self, name, weight, speed_run):
        self.__name = name
        self.__weight = weight
        self.__speed_run = speed_run

    @property
    def speed_run(self):
        return self.__speed_run

    @speed_run.setter
    def speed_run(self, speed: int):
        self.__speed_run = speed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    def __str__(self):
        return (f'Название животного : {self.__name}\nСкорость передвижения : {self.__speed_run} км\ч\n'
                f'Вес : {self.__weight} кг')


class Birds(Animal):
    def __init__(self, name, speed_run, weight, wings):
        super().__init__(self, name, speed_run, weight)
        self.__wings = wings

    @property
    def wings(self):
        return self.__wings

    @wings.setter
    def weight(self, wings=True):
        if wings == False:
            return (f'Это не птица!!')
        else:
            return (f'Это птица! Она умеет летать!')

    def __str__(self):
        return (f'{super().__str__()}\nКрылья :{self.__wings}')


class Reptiles(Animal):
    def __init__(self, name, weight, temperature):
        super().__init__(self, name, weight)
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature: int):
        if 15 <= temperature <= 21:
            return self.__temperature = temperature

    def __str__(self):
        return (f'{super().__str__()}\nТемпература тела :{self.__temperature}')


class Mammals(Animal):
    def __init__(self, name, weight, speed_run, milk_feeding:bool= True):
        super().__init__(self, name, weight, speed_run)
        self.__milk_feeding = milk_feeding

    @property
    def milk_feeding(self):
        return self.__milk_feeding

    @milk_feeding.setter
    def milk_feeding(self, milk_feeding:bool= True):
        if milk_feeding == False
            return str(f'f{self.__name} - это не млекопитающее!!')
        else:
            return self.__milk_feeding

    def __str__(self):
        return (f'{super().__str__()}\nВскармливание молоком :{self.__milk_feeding}')


class Dogs(Mammals):
    def __init__(self, name, weight, milk_feeding, wool):
        super().__init__(name,weight, milk_feeding)
        self.__wool = wool

    @property
    def wool(self):
        self.__wool

    @wool.setter
    def wool(self, wool:str):
        if wool == 'short':
            return str(f'{self.__wool} : "Эта собака гладкошерстная!')
        elif wool == 'long':
            return str(f'{self.__wool} : "Эта собака длинношерстная!')
        else:
            return 0

    def __str__(self):
        return (f'{super().__str__()}\nШерсть :{self.__wool}')

class Parrot(Birds):
    def __init__(self, name, speed_run, weight, wings, color):
        super().__init__(self, name, speed_run, weight, wings)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    def __str__(self):
        return (f'{super().__str__()}\nЦвет :{self.__color}')

class Snakes(Reptiles):
    def __init__(self, name, weight, temperature,legs: bool=False):
        super().__init__(self, name, weight,temperature)
        self.__legs = legs

    def legs(self,legs):
        if legs == True:
            return str('Это не змея!')
        else:
            return self.__legs

    def __str__(self):
        return (f'{super().__str__()}\nНаличие лап :{self.__legs}')