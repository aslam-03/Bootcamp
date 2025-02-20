# class Animal:
#     def speak(self):
#         print("hi im jimmy")
# class dog(Animal):
#     def speak(self):
#         print("hi im dog")
# class cat(Animal):
#     def speak(self):
#         print("hi im cat")
# a=[Animal(),dog(),cat()]
# for i in a:
#     i.speak()

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
