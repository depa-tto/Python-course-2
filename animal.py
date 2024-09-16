class Animal:

    alive = True

    def eat(self):   # remember the self !
        print('this animal is eating')

    def sleep(self):
        print('this animal is sleeping')


class Rabbit(Animal):# so rabbit is the child class and animal is the parent one. the class rabbit is going to inherit everything 
                      # that the class animal has 
    def run(self):
        print('this rabbit can run')


class Fish(Animal):
    def swim(self):
        print('this fish can swim')


class Hawk(Animal):
    def fly(self):
        print('this fish can fly')

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# so all the animal are alive and all of them eat and sleep, so this characteristics will be inherit by all the animals.
# instead only the rabbit can run, the fish swim and the hawk fly, so all the single animals will have thei own characteristics






