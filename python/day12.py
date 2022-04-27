class Car:
    no_of_seats = 4
    def __init__(self, b, m, s):
        self.start = False
        self.brand = b
        self.model = m 
        self.style = s 

    @staticmethod
    def intro():
        print("This is the object of car class")

    @classmethod
    def change_seat_no(cls, n):
        cls.no_of_seats = n

    def getdetails(self):
        return f"Details of {self.brand} {self.model}:- \nStyle : {self.style}\nEngine Start : {self.start}"

    def startcar(self):
        self.start = True 

    def stopcar(self):
        self.start = False 

    def checkcar(self):
        if self.start == True:
            return "The car's engine is working"

        else:
            return "The car's engine is not working"


alto = Car("Maruti", "Alto 800", "Hatchback")
# print(alto.getdetails())

alto.startcar()
alto.stopcar()
# print(alto.getdetails())
# print(alto.checkcar())

aventador = Car("Lamborghini", "Aventador S", "Roadster")
# print(aventador.getdetails())

aventador.change_seat_no(5)

# print(Car.no_of_seats)
# aventador.intro()


class SuperCar(Car):
    pass

chiron = SuperCar("Bugatti", "Chiron", "Super Car") 
chiron.intro()

class HyperCar(Car):
    pass 


p1 = HyperCar("McLaren", "P1", "Hyper Car")
p1.intro()

class SuperRickshaw(SuperCar):
    pass


"""
Single Inheritance - 1 Base Classes => 1 Child Class

Multiple Inheritance - Multiple Base Classes => 1 Child Class

Hierarchical Inheritance - 1 Base Class => Multiple child classes

Multilevel Inheritance - Inheritance at multiple levels(On multiple levels, some classes are being derived from another classes)

Hybrid Inheritance - When more than 1 type of Inheritance occur simultaneously
"""
