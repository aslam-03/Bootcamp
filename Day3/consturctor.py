class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
       
dog_1=Dog("Jimmy",5)
dog_2=Dog("Reo",6)
# for x in [dog_1,dog_2]:
#     print(dog_1.name,dog_2.name)
print(dog_1.name,dog_1.age)
print(dog_2.name,dog_2.age)