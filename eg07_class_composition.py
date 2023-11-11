class Dog():
    def __init__(self, name, breed, owner) -> None:
        self.name=name
        self.breed=breed
        self.owner=owner
    
class Person():
    def __init__(self, name) -> None:
        self.name=name

mick=Person("Mick Tyson")
dog=Dog("stanley", "Bulldog", mick)
print(dog.name)
print(dog.owner.name)
