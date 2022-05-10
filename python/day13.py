class Phone:
    smart = False
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model 
        self.price = price

    def print_details(self):
        return f"Brand: {self.brand} Model: {self.model} Price: {self.price}"


class SmartPhone(Phone):
    smart = True
    def __init__(self, brand, model, price, camera, battery, processor):
        super().__init__(brand, model, price)
        self.camera = camera
        self.battery = battery 
        self.processor = processor
    

    def intro(self):
        return super().print_details()


abc = SmartPhone("ABC", "XYZ123", 23999, "64MP", "5250 mAh", "SD888")
print(abc.intro())


class A:
    @staticmethod
    def intro():
        return f"This is the object of A class"

class B(A):
    @staticmethod 
    def intro():
        return 2 + 3
        
b = B()
print(b.intro())
