class Employee:
    salary = "325457654"
    deppt = "IT" 


# Instance - Other name for objects. The Process of making objects is also called as instantiation

shivam = Employee()
shivam.post = "Developer"
ashish = Employee()

# print(Employee.salary)

# print(ashish.salary)
# print(shivam.salary)

akku = Employee()

ashish.deppt = "Finance"
akku.no_of_leaves = 5
print(ashish.deppt)

# print(akku.__dict__)

# print(ashish.post)
# Variables - Properties and Functions - Methods 

# Class Variables and Instance Variables

class Car:
    wheels = 4
    seats = 4
    window = 4
    engine = 1
    # Methods - Class Functions

    def intro(self):
        return f"This car has {self.wheels} Wheels, {self.seats} Seats, {self.window} Windows and {self.engine} Engines"

    def getseats(self):
        return f"This car has {self.seats} seats"


nano = Car()
# print(nano.wheels, nano.seats, nano.window, nano.engine)
print(nano.intro())
print(nano.getseats())


huracan = Car()
huracan.seats = 2
huracan.window = 2
huracan.engine = 4
huracan.nos = True
print(huracan.getseats())
print(huracan.intro())

cian = Car()
print(cian.intro())
# print(huracan.wheels, huracan.seats, huracan.window, huracan.nos)

# Constructor - 


class Student:
    def __init__(self, f, l, age, std):
        self.firstname = f
        self.lastname = l
        self.age = age
        self.standard = std

    def getdetails(self):
        return f"Name: {self.firstname} {self.lastname}\nAge: {self.age}\nStandard: {self.standard}"

shuaib = Student("Mohd", "Shuaib", 23, 12)

# print(shuaib.getdetails())

shruti = Student("Shruti", "Saxena", 23, 12)

# print(shruti.getdetails())

# print(shuaib.age)



class TV:
    def __init__(self, bname, mname, pr, vol):
        self.brand = bname 
        self.model = mname 
        self.price = pr 
        self.volume = vol 

    def getdetails(self):
        return f"Brand: {self.brand}\nModel:  {self.model}\nPrice: {self.price}\nVolume: {self.volume}/10"

    def volumeUp(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print("Volume cannot be increased further")

    def volumeDown(self):
        self.volume -= 1


onePlus = TV("One Plus", "121x21", 31999, 8)


onePlus.volumeUp()
onePlus.volumeUp()
onePlus.volumeUp()
print(onePlus.getdetails())

mi = TV("Mi", "Mx-321", 24999, 2)

mi.volumeDown()
mi.volumeDown()
mi.volumeDown()
print(mi.getdetails())