from dogLayla import *


dog1 = Dog("German Pinscher", 1, 43.0, "Rizzo")  
dog2 = Dog("Golden Retriever", 3, 64.0, "Callypso")
dog3 = Dog("Chihuahua", 2, 15.6, "Cheeto")
dog4 = Dog("Blue Tick Hound", 4, 52.5)
dog5 = Dog("Black Laborator Retriever", 6, 73.0)


print(dog1)
print(dog3.age)

print(dog2.get_age())

print(Dog.sum_ages())
