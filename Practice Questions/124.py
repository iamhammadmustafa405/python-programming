# 124: Temperature Converter
# Create a class that stores temperature privately in Celsius. Expose methods get_fahrenheit() and get_kelvin() without revealing the internal storage unit.

# The formula is:
# °F = (°C × 9/5) + 32
# For example, to convert 100°C to Fahrenheit: (100 × 9/5) + 32 = 180 + 32 = 212°F

class Temp:
    def __init__(self, __temp_cel):
        self.__temp_cel = __temp_cel
    

    def get_fahrenheit(self):
        return ((self.__temp_cel * 9/5) +32)
        
    
    def get_kelvin(self):
        return (self.__temp_cel + 273)
    
    def show_fahrenheit(self):
        print(f"The temperature in fahrenheit is : {self.get_fahrenheit()}")
    

    def show_kelvin(self):
        print(f"The temperature in kelvin is : {self.get_kelvin()}")


t1= Temp(67)
t1.get_fahrenheit()
t1.show_fahrenheit()
t1.get_kelvin()
t1.show_kelvin()