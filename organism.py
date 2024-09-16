class Organism: # PARENT CLASS

    alive = True


class Animal(Organism): # CHILD CLASS OF ORGANISM
    def eat(self):
        print('this animal is eating')

class Dog(Animal): # SUB CHILD CLASS OF ANIMAL 
    def bark(self):
        print('this dog is barking')


dog = Dog()
dog.alive
dog.eat()
dog.bark()

