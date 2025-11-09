class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello Mr. {self.name}"


p1 =  Person("Dheeraj",22)

print(p1.greet())