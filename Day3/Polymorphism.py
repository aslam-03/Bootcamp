
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

def animal_speak(animal: Animal):
    print(animal.speak())


dog = Dog()
cat = Cat()
animal_speak(dog)  
animal_speak(cat)  
