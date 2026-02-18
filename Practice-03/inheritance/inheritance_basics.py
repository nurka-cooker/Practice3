class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()