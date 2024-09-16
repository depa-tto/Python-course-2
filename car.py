class Car:

    wheels = 4 # defaul value. this is an example of class varible, because the make, model, year and the color coul be different,
               # but all the cars have 4 wheels 

    def __init__(self, make, model, year, color):    # init stands for initialize. THIS IS THE CONSTRUCTOR
        self.make = make # instance varible
        self.model = model # instance varible
        self.year = year # instance varible
        self.color = color # instance varible

    def drive(self): # self refers to the object that is using this method
        print('this ' + self.model + ' is driving')

    def stop(self): # self refers to the object that is using this method
        print('this ' + self.model + ' is stopped')


# so the instance variable is declared inside the constructor and they can be given unique values
# instead, the class variable is declared within a class but outside the constructor and in thi way we can 
# assign a default value for all the unique objects that are created 
        
        

