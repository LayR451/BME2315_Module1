# print("Hello World")

# my_string = "Hello Tripp"
# print(my_string)

# Making a constructor/special method to list different attributes a data type can have (or different categories wihtin the data)
class Dog:
    all_dogs = []

    def __init__(self, breed: str, age: float, weight: float, name: str = "n/a", breedgroup: str = "n/a"): 
        self.breed = breed
        self.age = age
        self.weight = weight
        self.name = name
        self.breedgroup = breedgroup
        Dog.all_dogs.append(self)

    @classmethod
    def sum_ages(cls):
            total = 0
            for dog in Dog.all_dogs:
                total += dog.age
            return total

    def __repr__(self):  
        return f"{self.name}: ({self.breed} | {self.breedgroup} | {self.age} | {self.weight})" 
    
    def get_age(self): 
        return self.age 

