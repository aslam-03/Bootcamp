class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(self.name," is barking")
    def sleep(self):
        print(self.name ,"is sleeping")
        
class puppy(Dog):
   def __init__(self,name,age):
    super().__init__(name,age) 

   def play(self):
      print(self.name,"is playing") 
dog_1=puppy("Jimmy",5)

dog_1.bark()
dog_1.sleep()
dog_1.play()
