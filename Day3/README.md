OOP in Python  

This repository contains my completed Object-Oriented Programming (OOP) tasks in Python, covering class creation, inheritance, multiple inheritance, encapsulation, and polymorphism.  

📌 Task 1: Class Creation (Dog Class) 
- Defined a `Dog` class with attributes **name** and **age**.  
- Implemented methods:  
  - `bark()` → Prints a barking message.  
  - `sleep()` → Prints a sleeping message.  
- Created and tested a `Dog` instance.  

✔ Output: A Dog object that can bark and sleep.  

---

📌 Task 2: Constructor Usage  
- Modified the `Dog` class to initialize attributes via the constructor.  
- Created multiple instances with different values.  
- Printed attributes to confirm dynamic initialization.  

✔ Output: Different Dog objects with correctly assigned attributes.  

---

📌 Task 3: Inheritance (Puppy Class) 
- Created a `Puppy` class that **inherits** from `Dog`.  
- Added a new method `play()` for the puppy.  
- Verified that `Puppy` instances can use all `Dog` methods.  

✔ Output: A Puppy object that can bark, sleep, and play.  

---

📌 Task 4: Multiple Inheritance (Hybrid Class) 
- Created a `Cat` class with `meow()` and `purr()`.  
- Defined a `Hybrid` class inheriting from **both** `Dog` and `Cat`.  
- Created a `Hybrid` object and tested methods from both parent classes.  

✔ Output: A Hybrid object that behaves like both a Dog and a Cat.  

---

📌 Task 5: Encapsulation (Robot Class)  
- Created a `Robot` class with:  
  - **Private attribute** `__energy_level` (not directly accessible).  
  - **Protected attribute** `_model`.  
- Implemented getter (`get_energy()`) and setter (`set_energy()`) methods for controlled access.  
- Added `charge()` method to modify energy safely.  

✔ Output: Encapsulated attributes with restricted direct access.  

---

📌 Task 6: Polymorphism (Animal Class) 
- Defined an `Animal` base class with `speak()` as an abstract method.  
- Created `Dog` and `Cat` subclasses, each overriding `speak()`.  
- Implemented a function `animal_speak()` that dynamically calls `speak()`.  
- Passed instances of `Dog` and `Cat` to observe different behaviors.  

✔ Output: Different sounds for different animal types, demonstrating polymorphism.  


