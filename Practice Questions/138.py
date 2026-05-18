# 138: 5. Polymorphism with Dunder Method
# Create a class Book:

# Attribute: pages

# Create another class Movie:

# Attribute: duration

# Implement __len__() in both:

# Book → return number of pages
# Movie → return duration

class Book: 
    def __init__(self,pages):
        if pages <0:
            raise ValueError("Pages cannot be Negative!")
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"Book with {self.pages} Pages "
    




class Movie:
    def __init__(self,duration):
        if duration < 0:                              
            raise ValueError("Duration cannot be negative!")
        self.duration = duration
    
    def __len__(self):
        return self.duration
    
    def __str__(self):
        return f"Movie with {self.duration} hours duration"
    
b= Book(56)
m= Movie(4)

for media in [b,m]:
    print(f"{media}  --> Length: {len(media)}")