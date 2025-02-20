class Robot:
    def __init__(self,energy_level,model):
        self.__energy_level=energy_level
        self._model=model

    # def boosting(self,boost):
    #     if boost>0:
    #         self.__energy_level=boost+ self.__energy_level
    #         print(f"{self.__energy_level}")
    #     else:
    #         print("give positive value")
    
    # def draining(self, drain):
    #     if 0 < drain <= self.__energy_level:
    #         self.__energy_level -= drain
    #         print(f"{self.__energy_level}")
    #     else:
    #         print("Insufficient enregy")
    def get_energy(self):
        return self.__energy_level
    
    def set_energy(self,boost):
        if boost>0:
            self.__energy_level=boost+ self.__energy_level
            print(f"{self.__energy_level}")
        else:
            print("give positive value")

    def mod(self):
        print(self._model)
    
em=Robot(300,2.0)
em.set_energy(50)
print(em.get_energy())
em.mod()



