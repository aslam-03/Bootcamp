class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(self.name," is barking")
    def sleep(self):
        print(self.name ,"is sleeping")
class puppy:

   def play(self):
      print(self.name,"is playing") 

class hybrid(Dog,puppy):
   def __init__(self,name,age,color):
    super().__init__(name,age)
    self.color=color
   
   def eat(self):
      print(self.name,"is eating")

dog_1=hybrid("jimmy",3,"orange")
dog_1.bark()
dog_1.sleep()
dog_1.play()
dog_1.eat()

print(dog_1.name,dog_1.age,dog_1.color)