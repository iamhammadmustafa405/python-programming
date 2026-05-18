# Polymorphism
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img= img
    
    def show_number(self):
        print(f"{self.real}i + {self.img}j")
    
    def __add__(self,num2):   # Dundar Methods
        new_real = (self.real + num2.real)
        new_img= (self.img + num2.img)   # This function is used for logic of adding the complex numbers.
        return Complex(new_real,new_img)
    
num1= Complex(4,5)
num2= Complex(7,8)
num3= num1 + num2
num3.show_number()